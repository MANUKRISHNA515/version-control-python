import os
import shutil
import sys

def checkout(commit_hash):
    commit_path = f".vcs/commits/{commit_hash}"
    
    if not os.path.exists(commit_path):
        print("Commit not found!")
        return

    files = os.listdir(commit_path)
    for file in files:
        if file != "message.txt":  # Ignore commit message
            shutil.copy(f"{commit_path}/{file}", file)
            print(f"Restored {file} from commit {commit_hash}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python checkout.py <commit_hash>")
    else:
        checkout(sys.argv[1])
