import json
import logging

logger = logging.getLogger(__name__)


def get_windows_path() -> str:
    return "~/Saved Games/Frontier Developments/Elite Dangerous"


def is_journal_file(name: str) -> bool:
    return name.startswith("Journal.") and name.endswith(".log")


def read_events(journal_path):
    with open(journal_path) as journal_file:
        try:
            for line in journal_file:
                event = json.loads(line)

                yield event
        except UnicodeDecodeError as error:
            logger.exception(f"Unicode decoding error in journal '{journal_path}'", exc_info=error)
