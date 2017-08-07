import git

REPOS = [
]


def main():
    for repo in REPOS:
        pull(repo)


def pull(repo):
    print("Pulling git repo:" + repo)
    g = git.cmd.Git(repo)
    g.pull()


if __name__ == '__main__':
    main()
