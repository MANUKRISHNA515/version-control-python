import os
import sys
import difflib

def diff(file_name, commit_hash):
    commit_path = f".vcs/commits/{commit_hash}/{file_name}"

    if not os.path.exists(commit_path):
        print("File not found in the given commit.")
        return

    with open(file_name, "r") as f1, open(commit_path, "r") as f2:
        original = f1.readlines()
        committed = f2.readlines()

    diff_result = list(difflib.unified_diff(committed, original, fromfile="committed", tofile="current"))
    
    if diff_result:
        print("Differences:")
        for line in diff_result:
            print(line, end="")
    else:
        print("No changes.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python diff.py <file_name> <commit_hash>")
    else:
        diff(sys.argv[1], sys.argv[2])

