import platformdirs
import os


DATABASE_FILENAME = "data.sqlite"
APP_NAME = "BubbleVisit"


def data_folder_path():
    return platformdirs.user_data_path(appname=APP_NAME, appauthor=False)


def database_path():
    return os.path.join(data_folder_path(), DATABASE_FILENAME)
