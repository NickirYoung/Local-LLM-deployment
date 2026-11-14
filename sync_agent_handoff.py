#!/usr/bin/env python3
"""Synchronize the Markdown deployment brief with its canonical HTML source."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
import sys


RUNBOOK_NAME = "vllm-windows11-deployment-runbook.html"


class HandoffParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.capturing = False
        self.matches = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag == "pre" and dict(attrs).get("id") == "code-agent":
            self.matches += 1
            self.capturing = True

    def handle_endtag(self, tag):
        if tag == "pre":
            self.capturing = False

    def handle_data(self, data):
        if self.capturing:
            self.parts.append(data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check", action="store_true", help="Fail if AGENT_HANDOFF.md is out of date."
    )
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    source = root / RUNBOOK_NAME
    target = root / "AGENT_HANDOFF.md"

    try:
        document = HandoffParser()
        document.feed(source.read_text(encoding="utf-8"))
        document.close()
        brief = "".join(document.parts).strip()
        if document.matches != 1 or not brief:
            raise ValueError("Expected one nonempty HTML element: pre#code-agent")

        expected = (
            "# Deployment agent handoff\n\n"
            "Use this brief alongside the [complete HTML runbook](./"
            + RUNBOOK_NAME
            + ").\n\n"
            "> Generated from the runbook's `code-agent` element. To change the "
            "brief, edit the HTML and run `python3 tools/sync_agent_handoff.py`.\n\n"
            + brief
            + "\n"
        )

        if args.check:
            actual = target.read_text(encoding="utf-8") if target.exists() else None
            if actual != expected:
                print(
                    "AGENT_HANDOFF.md is out of date. "
                    "Run: python3 tools/sync_agent_handoff.py",
                    file=sys.stderr,
                )
                return 1
            print("AGENT_HANDOFF.md matches the HTML runbook.")
            return 0

        with target.open("w", encoding="utf-8", newline="\n") as output:
            output.write(expected)
        print("Updated AGENT_HANDOFF.md from the HTML runbook.")
        return 0
    except (OSError, ValueError) as error:
        print("Handoff synchronization failed: " + str(error), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
