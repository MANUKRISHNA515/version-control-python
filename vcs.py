import os
import sys
import hashlib
import shutil
import datetime
from checkout import checkout
from diff import diff
from branch import create_branch, switch_branch
from merge import merge
def init():
    if not os.path.exists('.vcs'):
        os.makedirs('.vcs')
        os.makedirs('.vcs/commits')
        print("Initialized empty VCS repository in .vcs/")
    else:
        print("Repository already exists!")

def add(file_name):
    with open('.vcs/staged_files.txt', 'a') as f:
        f.write(file_name + "\n")
    print(f"Added {file_name} to tracking.")

def commit(message):
    commit_hash = hashlib.sha1(str(datetime.datetime.now()).encode()).hexdigest()[:7]
    commit_path = f".vcs/commits/{commit_hash}"
    os.makedirs(commit_path)

    with open('.vcs/staged_files.txt', 'r') as f:
        files = f.readlines()

    for file in files:
        file = file.strip()
        if os.path.exists(file):
            shutil.copy(file, commit_path)
    
    with open(f"{commit_path}/message.txt", 'w') as f:
        f.write(message)

    print(f"Committed changes with hash {commit_hash}")

def log():
    commits = os.listdir('.vcs/commits')
    for commit in commits:
        with open(f".vcs/commits/{commit}/message.txt", "r") as f:
            message = f.read()
        print(f"Commit {commit}: {message}")

if __name__ == "__main__":
    command = sys.argv[1]

    if command == "init":
        init()
    elif command == "add":
        add(sys.argv[2])
    elif command == "commit":
        commit(sys.argv[2])
    elif command == "log":
        log()
    else:
        print("Unknown command")
elif command == "checkout":
    if len(sys.argv) < 3:
        print("Usage: python vc.py checkout <commit_hash>")
    else:
        checkout(sys.argv[2])
elif command == "diff":
    if len(sys.argv) < 4:
        print("Usage: python vc.py diff <file_name> <commit_hash>")
    else:
        diff(sys.argv[2], sys.argv[3])
elif command == "branch":
    if len(sys.argv) < 4:
        print("Usage: python vc.py branch <create/switch> <branch_name>")
    else:
        action = sys.argv[2]
        branch_name = sys.argv[3]
        if action == "create":
            create_branch(branch_name)
        elif action == "switch":
            switch_branch(branch_name)
elif command == "merge":
    if len(sys.argv) < 3:
        print("Usage: python vc.py merge <branch_name>")
    else:
        merge(sys.argv[2])
