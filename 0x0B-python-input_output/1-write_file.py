#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
