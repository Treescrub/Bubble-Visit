import json
import logging

logger = logging.getLogger(__name__)


def get_windows_path() -> str:
    return "~/Saved Games/Frontier Developments/Elite Dangerous"


def is_journal_file(name: str) -> bool:
    return name.startswith("Journal.") and name.endswith(".log")


def read_events(journal_path):
    with open(journal_path, encoding="utf-8") as journal_file:
        for line in journal_file:
            event = json.loads(line)

            yield event
