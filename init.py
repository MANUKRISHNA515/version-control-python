import os

def init():
    if not os.path.exists('.vcs'):
        os.makedirs('.vcs')
        os.makedirs('.vcs/commits')
        print("Initialized empty VCS repository in .vcs/")
    else:
        print("Repository already exists!")

if __name__ == "__main__":
    init()
