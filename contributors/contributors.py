# -*- coding: utf-8 -*-

"""
1. Get list of repos desired to be checked for sprinters
2. For each repo:
    A. Get a list of committers
    B. Get a list of those who filed new issues
    C. Get a list of those who submitted unnaccepted pull requests
    D. Combine lists into a Python set
3. Generate a RST (or markdown) list from the data. Each element includes
    A. GitHub username
    B. Personal name if different
    C. Link to user profile on GitHub

"""

from datetime import datetime
from os import environ

from github3 import login


def get_contribitors(repo_names, since=None, until=None):
    """
    :param repo_names: List of GitHub repos, each named thus:
                        ['audreyr/cookiecutter', 'pydanny/contributors']
    """
    gh = login(token=environ.get('GITHUB_API_SECRET'))

    contributors = set([])
    links = ""
    output = []

    print('Starting aggregating sprinters across projects')
    for repo_name in repo_names.split(','):
        print('\nFetching data for', repo_name)
        user_name, repo_name = repo_name.split('/')
        repo = gh.repository(user_name, repo_name)
        for commit in repo.commits(since=since, until=until):
            print('.', end='', flush=True)
            if commit.author is not None:
                contributors.add(str(commit.author))

    print('\nBuilding output')
    for contributor in contributors:
        print('.', end='', flush=True)
        user = gh.user(contributor)
        if user.name.strip():
            output.append("  * {name} (`@{username}`_)".format(
                    name=user.name,
                    username=user.login
                )
            )
        else:
            output.append("  * `@{username}`_".format(username=user.login))

        links += ".. _`@{username}`: {html_url}\n".format(
            username=user.login,
            html_url=user.html_url
        )
    output = sorted(output, key=lambda x: x.replace('@', '').replace('`', '').lower())
    return '\n'.join(output) + '\n' + links

if __name__ == "__main__":
    since = datetime(2016, 6, 2)
    until = datetime.now()
    repo_names = ['audreyr/cookiecutter', 'pydanny/cookiecutter-django']
    output = main(repo_names, since=since, until=until)
    print('\nSaving results to output.rst')
    with open('output.rst', 'w') as f:
        f.write(output)
