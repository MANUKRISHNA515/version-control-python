import os
import sys
import shutil

def create_branch(branch_name):
    branches_dir = ".vcs/branches"
    branch_path = f"{branches_dir}/{branch_name}"

    if not os.path.exists(branches_dir):
        os.makedirs(branches_dir)

    if os.path.exists(branch_path):
        print(f"Branch {branch_name} already exists.")
    else:
        shutil.copy(".vcs/HEAD", branch_path)
        print(f"Created branch {branch_name}")

def switch_branch(branch_name):
    branch_path = f".vcs/branches/{branch_name}"

    if not os.path.exists(branch_path):
        print(f"Branch {branch_name} does not exist.")
    else:
        shutil.copy(branch_path, ".vcs/HEAD")
        print(f"Switched to branch {branch_name}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python branch.py <create/switch> <branch_name>")
    else:
        action = sys.argv[1]
        branch_name = sys.argv[2]

        if action == "create":
            create_branch(branch_name)
        elif action == "switch":
            switch_branch(branch_name)
        else:
            print("Invalid command. Use 'create' or 'switch'.")

