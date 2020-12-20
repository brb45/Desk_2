# The Jira REST API enables you to interact with Jira programmatically.
#
# Use this API to build apps,
# script interactions with Jira,
# or develop any other type of integration.
#
# This page documents the REST
# resources available in Jira Cloud, including the HTTP response codes and example requests and responses.

# Personal data that is used to identify users, such as username and userKey,
# has been removed from the Jira Cloud REST APIs.
#
# In addition,
# other personal data (for example, email) is now restricted
# by a user's profile settings
# http://host:port/context/rest/api-name/api-version/resource-name

# Json format of Jra-9
url = 'https://jira.atlassian.com/rest/api/latest/issue/JRA-9'
url = "https://jira.atlassian.com/rest/api/latest/issue/JRA-9?expand=names,renderedFields"
# web-based JRA-9
url = 'https://jira.atlassian.com/browse/JRASERVER-9'

# The log-in page uses cookie-based authentication, so if you are using JIRA in a browser
# you can call REST from Javascript on the page and rely on the authentication that the browser has established

# curl -D- -u {username}:{password} -X POST -H "X-Atlassian-Token: nocheck" -F "file=@{path/to/image}" http://{base-url}/rest/api/2/issue/{issue-key}/attachments
url = 'http://{base-url}/rest/api/2/issue/{issue-key}/attachments'

# The URIs for resources have the following structure:
#
# https://<site-url>/rest/api/3/<resource-name>
#
# For example, https://your-domain.atlassian.net/rest/api/3/issue/DEMO-1

# Expansion
# The Jira REST API uses resource expansion, which means that some parts of a resource are not returned
# unless specified in the request. This simplifies responses and minimizes network traffic.
# For example, the following request expands the names and renderedFields properties for the JRACLOUD-34423 issue:

# GET issue/JRACLOUD-34423?expand=names,renderedFields

# https://jira.litepoint.com/
# https://jira.litepoint.com/secure/Dashboard.jspa
# https://jira.litepoint.com/secure/Dashboard.jspa

