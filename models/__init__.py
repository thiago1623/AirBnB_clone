#!/usr/bin/python3
import sys


if __name__ == "__main__":
    sys.path.append("..")
    from engine.file_storage import FileStorage

    storage = file_storage.FileStorage()
    storage.reload()
