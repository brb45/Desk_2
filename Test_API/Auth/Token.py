# Resource:
#
# POST /auth/v1/oauth/token
# GET  /auth/v1/validate_token
#
# Response:
# access_token, refresh_token, token_type (bearer), expires_in(second), scope("email access")

# Get a token
POST https://geobigdata.io/auth/v1/oauth/token/
Form data: {grant_type: password, username: email_address, password: userpasswd}


import requests

url = "https://geobigdata.io/auth/v1/oauth/token/"

response = requests.request("POST", url)

print(response.text)


# 200 OK
# {
#     "access_token": <access token string>
#     "scope": "read write",
#     "token_type": "Bearer",
#     "expires_in": 604800,
#     "refresh_token": <refresh token string>
# }

# Get a task definition
GET https://geobigdata.io/workflow/v1/tasks/name
https://geobigdata.io/workflows/v1/tasks/Getting_Started:0.0.1
#
# {
#   "containerDescriptors": [
#     {
#       "command": "",
#       "type": "DOCKER",
#       "properties": {
#         "image": "tdgp/hello_gbdx:latest"
#       }
#     }
#   ],
#   "description": "Get a personalized greeting to GBDX",
#   "inputPortDescriptors": [
#     {
#       "required": true,
#       "type": "string",
#       "description": "Enter your name here for a personalized greeting to the platform.",
#       "name": "your_name"
#     }
#   ],
#   "version": "0.0.1",
#   "outputPortDescriptors": [
#     {
#       "required": true,
#       "type": "txt",
#       "description": "The output directory of text file",
#       "name": "data"
#     }
#   ],
#   "properties": {
#     "isPublic": true,
#     "canPersist": true,
#     "timeout": 7200
#   },
#   "name": "Getting_Started"
# }
#
#
#  200 OK






















































