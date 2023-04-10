import os

SCORES_FILE_NAME = "scores.txt"
BAD_RETURN_CODE = 101


def screen_cleaner():
    if os.name == "posix":
        os.system("clear")
    elif os.name in ("nt", "dos", "ce"):
        os.system("cls")
