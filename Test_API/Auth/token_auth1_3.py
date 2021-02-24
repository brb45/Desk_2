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
## Delete a repo


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
# post response
# {'id': 339257801,
# 'node_id': 'MDEwOlJlcG9zaXRvcnkzMzkyNTc4MDE=',
# 'name': 'auto_repo_1',
# 'full_name': 'brb45/auto_repo_1',
# 'private': False,
# 'owner': {'login': 'brb45', 'id': 10520787, 'node_id': 'MDQ6VXNlcjEwNTIwNzg3', 'avatar_url': 'https://avatars.githubusercontent.com/u/10520787?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/brb45', 'html_url': 'https://github.com/brb45', 'followers_url': 'https://api.github.com/users/brb45/followers', 'following_url': 'https://api.github.com/users/brb45/following{/other_user}', 'gists_url': 'https://api.github.com/users/brb45/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/brb45/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/brb45/subscriptions', 'organizations_url': 'https://api.github.com/users/brb45/orgs', 'repos_url': 'https://api.github.com/users/brb45/repos', 'events_url': 'https://api.github.com/users/brb45/events{/privacy}', 'received_events_url': 'https://api.github.com/users/brb45/received_events', 'type': 'User', 'site_admin': False},
#  'html_url': 'https://github.com/brb45/auto_repo_1', 'description': 'Created with api', 'fork': False, 'url': 'https://api.github.com/repos/brb45/auto_repo_1', 'forks_url': 'https://api.github.com/repos/brb45/auto_repo_1/forks', 'keys_url': 'https://api.github.com/repos/brb45/auto_repo_1/keys{/key_id}', 'collaborators_url': 'https://api.github.com/repos/brb45/auto_repo_1/collaborators{/collaborator}', 'teams_url': 'https://api.github.com/repos/brb45/auto_repo_1/teams', 'hooks_url': 'https://api.github.com/repos/brb45/auto_repo_1/hooks', 'issue_events_url': 'https://api.github.com/repos/brb45/auto_repo_1/issues/events{/number}', 'events_url': 'https://api.github.com/repos/brb45/auto_repo_1/events', 'assignees_url': 'https://api.github.com/repos/brb45/auto_repo_1/assignees{/user}', 'branches_url': 'https://api.github.com/repos/brb45/auto_repo_1/branches{/branch}', 'tags_url': 'https://api.github.com/repos/brb45/auto_repo_1/tags', 'blobs_url': 'https://api.github.com/repos/brb45/auto_repo_1/git/blobs{/sha}', 'git_tags_url': 'https://api.github.com/repos/brb45/auto_repo_1/git/tags{/sha}', 'git_refs_url': 'https://api.github.com/repos/brb45/auto_repo_1/git/refs{/sha}', 'trees_url': 'https://api.github.com/repos/brb45/auto_repo_1/git/trees{/sha}', 'statuses_url': 'https://api.github.com/repos/brb45/auto_repo_1/statuses/{sha}', 'languages_url': 'https://api.github.com/repos/brb45/auto_repo_1/languages', 'stargazers_url': 'https://api.github.com/repos/brb45/auto_repo_1/stargazers', 'contributors_url': 'https://api.github.com/repos/brb45/auto_repo_1/contributors', 'subscribers_url': 'https://api.github.com/repos/brb45/auto_repo_1/subscribers', 'subscription_url': 'https://api.github.com/repos/brb45/auto_repo_1/subscription', 'commits_url': 'https://api.github.com/repos/brb45/auto_repo_1/commits{/sha}', 'git_commits_url': 'https://api.github.com/repos/brb45/auto_repo_1/git/commits{/sha}', 'comments_url': 'https://api.github.com/repos/brb45/auto_repo_1/comments{/number}', 'issue_comment_url': 'https://api.github.com/repos/brb45/auto_repo_1/issues/comments{/number}', 'contents_url': 'https://api.github.com/repos/brb45/auto_repo_1/contents/{+path}', 'compare_url': 'https://api.github.com/repos/brb45/auto_repo_1/compare/{base}...{head}', 'merges_url': 'https://api.github.com/repos/brb45/auto_repo_1/merges', 'archive_url': 'https://api.github.com/repos/brb45/auto_repo_1/{archive_format}{/ref}', 'downloads_url': 'https://api.github.com/repos/brb45/auto_repo_1/downloads', 'issues_url': 'https://api.github.com/repos/brb45/auto_repo_1/issues{/number}', 'pulls_url': 'https://api.github.com/repos/brb45/auto_repo_1/pulls{/number}', 'milestones_url': 'https://api.github.com/repos/brb45/auto_repo_1/milestones{/number}', 'notifications_url': 'https://api.github.com/repos/brb45/auto_repo_1/notifications{?since,all,participating}', 'labels_url': 'https://api.github.com/repos/brb45/auto_repo_1/labels{/name}', 'releases_url': 'https://api.github.com/repos/brb45/auto_repo_1/releases{/id}', 'deployments_url': 'https://api.github.com/repos/brb45/auto_repo_1/deployments', 'created_at': '2021-02-16T01:48:28Z', 'updated_at': '2021-02-16T01:48:28Z', 'pushed_at': '2021-02-16T01:48:29Z', 'git_url': 'git://github.com/brb45/auto_repo_1.git', 'ssh_url': 'git@github.com:brb45/auto_repo_1.git', 'clone_url': 'https://github.com/brb45/auto_repo_1.git', 'svn_url': 'https://github.com/brb45/auto_repo_1', 'homepage': None, 'size': 0, 'stargazers_count': 0, 'watchers_count': 0, 'language': None, 'has_issues': True, 'has_projects': True, 'has_downloads': True, 'has_wiki': True, 'has_pages': False, 'forks_count': 0, 'mirror_url': None, 'archived': False, 'disabled': False, 'open_issues_count': 0, 'license': None, 'forks': 0, 'open_issues': 0, 'watchers': 0, 'default_branch': 'main', 'permissions': {'admin': True, 'push': True, 'pull': True},
#  'allow_squash_merge': True, 'allow_merge_commit': True, 'allow_rebase_merge': True, 'delete_branch_on_merge': False, 'network_count': 0, 'subscribers_count': 1}

url_delete = 'https://api.github.com/repos/'
repo_to_delete = 'auto_repo_1'
def authentication_delete(url_delete, repo):
    token = return_token()[2]
    user = return_token()[0]

    url_delete += user + '/' + repo_to_delete
    headers = {'Authorization': 'token ' + token}

    response = requests.delete(url_delete, headers=headers)
    print(response.status_code)
    print("--------------------------")
    response_dic = response.json()
    print(response_dic)

    print("-------------------------------------")
    header_response = response.headers
    print(header_response)
authentication_delete(url_delete, repo_to_delete)

# 204

# response = requests.get('https://api.buildkite.com/v2/organizations/orgName/pipelines/pipelineName/builds/1230', headers={ 'Authorization': 'Bearer <your_token>' })
# print(response.json())

