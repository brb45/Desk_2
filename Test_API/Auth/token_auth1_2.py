##2. Token Authentication

import requests, json #, jsonpath
from requests.auth import HTTPBasicAuth

def return_token():
    file = "C:\\Users\jsun\Desktop\QA\Weekly\\token.txt"
    with open(file) as fout:
        token = fout.read()
    token  = token.split()
    return token


# description = 'Created with api'
#
# payload = {'name': repo, 'description': description, 'auto_init': 'true'}
#
# login = requests.post('https://api.github.com/' + 'user/repos', auth=(user,token), data=json.dumps(payload))
## Create a repo
url = 'https://api.github.com/user/repos'

def authentication_post(url):
    token = return_token()[1]
    user = return_token()[0]
    repo = 'auto_repo_1'
    description = 'Created with api'
    payload = {'name': repo, 'description': description, 'auto_init': 'true'}

    headers = {'Authorization': 'token ' + token}
    data = json.dumps(payload)

    response = requests.post(url, data = data, headers=headers)
    response_dic = response.json()
    print(response_dic)

    print(response.status_code)


    print("-------------------------------------")
    header_response = response.headers
    print(header_response)


authentication_post(url)
# C:\Users\jsun\Documents\Desk_2\venv_3.7.2\Scripts\python.exe C:/Users/jsun/Documents/Desk_2/Test_API/Auth/token_auth1_2.py
# {'id': 339253375, 'node_id': 'MDEwOlJlcG9zaXRvcnkzMzkyNTMzNzU=', 'name': 'auto_repo', 'full_name': 'brb45/auto_repo', 'private': False, 'owner': {'login': 'brb45', 'id': 10520787, 'node_id': 'MDQ6VXNlcjEwNTIwNzg3', 'avatar_url': 'https://avatars.githubusercontent.com/u/10520787?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/brb45', 'html_url': 'https://github.com/brb45', 'followers_url': 'https://api.github.com/users/brb45/followers', 'following_url': 'https://api.github.com/users/brb45/following{/other_user}', 'gists_url': 'https://api.github.com/users/brb45/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/brb45/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/brb45/subscriptions', 'organizations_url': 'https://api.github.com/users/brb45/orgs', 'repos_url': 'https://api.github.com/users/brb45/repos', 'events_url': 'https://api.github.com/users/brb45/events{/privacy}', 'received_events_url': 'https://api.github.com/users/brb45/received_events', 'type': 'User', 'site_admin': False}, 'html_url': 'https://github.com/brb45/auto_repo', 'description': 'Created with api', 'fork': False, 'url': 'https://api.github.com/repos/brb45/auto_repo', 'forks_url': 'https://api.github.com/repos/brb45/auto_repo/forks', 'keys_url': 'https://api.github.com/repos/brb45/auto_repo/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/brb45/auto_repo/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/brb45/auto_repo/teams', 'hooks_url': 'https://api.github.com/repos/brb45/auto_repo/hooks', 'issue_events_url': 'https://api.github.com/repos/brb45/auto_repo/issues/events{/number}', 'events_url': 'https://api.github.com/repos/brb45/auto_repo/events', 'assignees_url': 'https://api.github.com/repos/brb45/auto_repo/assignees{/user}', 'branches_url': 'https://api.github.com/repos/brb45/auto_repo/branches{/branch}', 'tags_url': 'https://api.github.com/repos/brb45/auto_repo/tags', 'blobs_url': 'https://api.github.com/repos/brb45/auto_repo/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/brb45/auto_repo/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/brb45/auto_repo/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/brb45/auto_repo/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/brb45/auto_repo/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/brb45/auto_repo/languages', 'stargazers_url': 'https://api.github.com/repos/brb45/auto_repo/stargazers', 'contributors_url': 'https://api.github.com/repos/brb45/auto_repo/contributors', 'subscribers_url': 'https://api.github.com/repos/brb45/auto_repo/subscribers', 'subscription_url': 'https://api.github.com/repos/brb45/auto_repo/subscription', 'commits_url': 'https://api.github.com/repos/brb45/auto_repo/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/brb45/auto_repo/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/brb45/auto_repo/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/brb45/auto_repo/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/brb45/auto_repo/contents/{+path}', 'compare_url': 'https://api.github.com/repos/brb45/auto_repo/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/brb45/auto_repo/merges', 'archive_url': 'https://api.github.com/repos/brb45/auto_repo/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/brb45/auto_repo/downloads', 'issues_url': 'https://api.github.com/repos/brb45/auto_repo/issues{/number}', 'pulls_url': 'https://api.github.com/repos/brb45/auto_repo/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/brb45/auto_repo/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/brb45/auto_repo/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/brb45/auto_repo/labels{/name}', 'releases_url': 'https://api.github.com/repos/brb45/auto_repo/releases{/id}', 'deployments_url': 'https://api.github.com/repos/brb45/auto_repo/deployments', 'created_at': '2021-02-16T01:22:12Z', 'updated_at': '2021-02-16T01:22:12Z', 'pushed_at': '2021-02-16T01:22:13Z', 'git_url': 'git://github.com/brb45/auto_repo.git', 'ssh_url': 'git@github.com:brb45/auto_repo.git', 'clone_url': 'https://github.com/brb45/auto_repo.git', 'svn_url': 'https://github.com/brb45/auto_repo', 'homepage': None, 'size': 0, 'stargazers_count': 0, 'watchers_count': 0, 'language': None, 'has_issues': True, 'has_projects': True, 'has_downloads': True, 'has_wiki': True, 'has_pages': False, 'forks_count': 0, 'mirror_url': None, 'archived': False, 'disabled': False, 'open_issues_count': 0, 'license': None, 'forks': 0, 'open_issues': 0, 'watchers': 0, 'default_branch': 'main', 'permissions': {'admin': True, 'push': True, 'pull': True}, 'allow_squash_merge': True, 'allow_merge_commit': True, 'allow_rebase_merge': True, 'delete_branch_on_merge': False, 'network_count': 0, 'subscribers_count': 1}
# 201
# -------------------------------------
# {'Date': 'Tue, 16 Feb 2021 01:22:13 GMT', 'Content-Type': 'application/json; charset=utf-8', 'Content-Length': '4792', 'Server': 'GitHub.com', 'Cache-Control': 'private, max-age=60, s-maxage=60', 'Vary': 'Accept, Authorization, Cookie, X-GitHub-OTP, Accept-Encoding, Accept, X-Requested-With, Accept-Encoding', 'ETag': '"4da16e47760d19856e28f9db20d1557c51faee89cee09cb4a0e53fc27a4a1706"', 'X-OAuth-Scopes': 'gist, public_repo, user', 'X-Accepted-OAuth-Scopes': 'public_repo, repo', 'Location': 'https://api.github.com/repos/brb45/auto_repo', 'X-GitHub-Media-Type': 'github.v3; format=json', 'X-RateLimit-Limit': '5000', 'X-RateLimit-Remaining': '4993', 'X-RateLimit-Reset': '1613441050', 'x-ratelimit-used': '7', 'Access-Control-Expose-Headers': 'ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset', 'Access-Control-Allow-Origin': '*', 'Strict-Transport-Security': 'max-age=31536000; includeSubdomains; preload', 'X-Frame-Options': 'deny', 'X-Content-Type-Options': 'nosniff', 'X-XSS-Protection': '1; mode=block', 'Referrer-Policy': 'origin-when-cross-origin, strict-origin-when-cross-origin', 'Content-Security-Policy': "default-src 'none'", 'X-GitHub-Request-Id': 'D28D:4284:85A958:9D6964:602B1E44'}
#



