
def github_auto():
    import os
    # from git import Repo
    branch = os.system("git rev-parse --abbrev-ref HEAD")
    commit = raw_input('Commit Message? ')
    print(commit)
    print(branch)
    os.system("git add .")
    os.system("git commit hi")
    os.system("git push origin ")

github_auto()

