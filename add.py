import os

def add(file_name):
    if not os.path.exists(file_name):
        print(f"Error: {file_name} does not exist!")
        return

    if not os.path.exists(".vcs"):
        print("Error: No VCS repository found. Run 'python vc.py init' first.")
        return

    staged_files_path = ".vcs/staged_files.txt"

    # Ensure staged_files.txt exists
    if not os.path.exists(staged_files_path):
        open(staged_files_path, 'w').close()

    # Avoid duplicate entries
    with open(staged_files_path, "r") as f:
        staged_files = f.readlines()

    if file_name + "\n" not in staged_files:
        with open(staged_files_path, "a") as f:
            f.write(file_name + "\n")
        print(f"Added {file_name} to tracking.")
    else:
        print(f"{file_name} is already tracked.")


