#!/usr/bin/python3
# ----------------------
# Imports
#
import os

# ----------------------
# Globals
#
LINE_LENGTH = 80


# ----------------------
# Definitions
#
def apply_markdown_line_length(path: str) -> bool:
    if not os.path.isdir(path) or not os.path.exists(path):
        return False

    for root, _, files in os.walk(path):
        for file in files:
            if not file.endswith(".md"):
                continue

            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                lines = f.readlines()
            for i, line in enumerate(lines):
                if len(line) > LINE_LENGTH and ". " in line:
                    lines[i] = line.replace(". ", ".\n")
            with open(file_path, "w") as f:
                f.writelines(lines)

    return True


# ----------------------
# Execution
#
if __name__ == '__main__':
    evmos_repo = "/Users/malte/test/evmos"
    apply_markdown_line_length(evmos_repo)
