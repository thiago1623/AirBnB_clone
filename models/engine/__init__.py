#!/usr/bin/python3
"""init class"""
import sys


if __name__ == "__main__":
    sys.path.append("..")
    from engine.file_storage import FileStorage
    from base_model import BaseModel

    storage = file_storage.FileStorage()
    storage.reload()
