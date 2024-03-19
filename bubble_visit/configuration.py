import platformdirs
from pathlib import Path


DATABASE_FILENAME = "data.sqlite"
APP_NAME = "BubbleVisit"


def data_folder_path() -> Path:
    return platformdirs.user_data_path(appname=APP_NAME, appauthor=False)


def get_config_dict() -> dict:
    pass


def database_path() -> Path:
    return Path(data_folder_path()) / DATABASE_FILENAME
