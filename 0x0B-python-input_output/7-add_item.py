#!/usr/bin/python3
"""
adding and saving script
"""

import sys

if __name__ == "__main__":
    saving = __import__('5-save_to_json_file').save_to_json_file
    loading = __import__('6-load_from_json_file').load_from_json_file

    try:
        items = loading("add_item.json")
    except FileNotFoundError:
        items = []
    items.extend(sys.argv[1:])
    saving(items, "add_item.json")