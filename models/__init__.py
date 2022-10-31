#!/usr/bin/python3
"""initialization file for models"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
