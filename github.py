
def github_auto():
    # commit_answer = ""
    # print "Commit Message?"
    commit = str(raw_input('Commit Message? '))
    print(commit)
    import os
    os.system("git add .")
    os.system("git commit hi")
    os.system("git push origin ")

github_auto()

