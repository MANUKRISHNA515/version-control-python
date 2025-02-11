def log():
    commits = os.listdir('.vcs/commits')
    for commit in commits:
        with open(f".vcs/commits/{commit}/message.txt", "r") as f:
            message = f.read()
        print(f"Commit {commit}: {message}")

if __name__ == "__main__":
    log()
