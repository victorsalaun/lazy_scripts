import git

# ADD GIT REPOS HERE
REPOS = [
]


def main():
    for repo in REPOS:
        pull(repo)


def pull(repo):
    print("\nPulling git repo:" + repo)
    g = git.cmd.Git(repo)
    print(g.pull())


if __name__ == '__main__':
    main()
