import os
import shutil
import sys

def merge(branch_name):
    branch_path = f".vcs/branches/{branch_name}"

    if not os.path.exists(branch_path):
        print(f"Branch {branch_name} does not exist.")
        return

    current_branch = open(".vcs/HEAD").read().strip()

    if current_branch == branch_name:
        print("You are already on this branch.")
        return

    commit_dir = f".vcs/commits/"
    for commit in os.listdir(commit_dir):
        commit_path = os.path.join(commit_dir, commit)
        for file in os.listdir(commit_path):
            if file != "message.txt":
                shutil.copy(os.path.join(commit_path, file), file)
                print(f"Merged {file} from {branch_name}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python merge.py <branch_name>")
    else:
        merge(sys.argv[1])
