import os
import hashlib
import shutil
import datetime

def commit(message):
    if not os.path.exists(".vcs"):
        print("Error: No VCS repository found. Run 'python vc.py init' first.")
        return

    staged_files_path = ".vcs/staged_files.txt"

    if not os.path.exists(staged_files_path) or os.stat(staged_files_path).st_size == 0:
        print("No files have been added for commit!")
        return

    commit_hash = hashlib.sha1(str(datetime.datetime.now()).encode()).hexdigest()[:7]
    commit_path = f".vcs/commits/{commit_hash}"
    os.makedirs(commit_path)

    with open(staged_files_path, 'r') as f:
        files = f.readlines()

    for file in files:
        file = file.strip()
        if os.path.exists(file):
            shutil.copy(file, commit_path)
        else:
            print(f"Warning: {file} no longer exists. Skipping.")

    with open(f"{commit_path}/message.txt", "w") as f:
        f.write(message)

    # Clear staged files after committing
    open(staged_files_path, "w").close()

    print(f"Committed changes with hash {commit_hash}")


