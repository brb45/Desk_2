# How OAuth works #
# Making API calls with OAuth is a two step process:
#
# You use persistent credentials, like your API key and secret (or sometimes username and password),
# to get a temporary OAuth token. This is a private, short-term password-like string.
# Instead of your persistent credentials, you pass along your OAuth token to make all of your API calls.
# Getting the OAuth token itself requires an API call. OAuth tokens typically expire
# after a short period of time—often an hour or a day.


# https://api.petfinder.com/v2/oauth2/token
# curl -d "grant_type=client_credentials&client_id={CLIENT-ID}&client_secret={CLIENT-SECRET}" https://api.petfinder.com/v2/oauth2/token

"""
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "a1b2c3d4e5"
}
"""

# https://api.petfinder.com/v2/{CATEGORY}/{ACTION}?{parameter_1}={value_1}&{parameter_2}={value_2}
# curl -H "Authorization: Bearer {YOUR_ACCESS_TOKEN}" GET https://api.petfinder.com/v2/{CATEGORY}/{ACTION}?{parameter_1}={value_1}&{parameter_2}={value_2}

# Call the API
# This is a POST request, because we need the API to generate a new token for us
fetch('https://api.petfinder.com/v2/oauth2/token', {
	method: 'POST',
	body: 'grant_type=client_credentials&client_id=' + key + '&client_secret=' + secret,
	headers: {
		'Content-Type': 'application/x-www-form-urlencoded'
	}
});

# GET
# Return a second API call
# This one uses the token we received for authentication
fetch('https://api.petfinder.com/v2/animals?organization=' + org + '&status=' + status, {
		headers: {
			'Authorization': data.token_type + ' ' + data.access_token,
			'Content-Type': 'application/x-www-form-urlencoded'
		}
	});

# Return a second API call
# 	This one uses the token we received for authentication
	return fetch('https://api.petfinder.com/v2/animals?organization=' + org + '&status=' + status, {
		headers: {
			'Authorization': data.token_type + ' ' + data.access_token,
			'Content-Type': 'application/x-www-form-urlencoded'
		}
	});

# how to use the same OAuth token to make additional API calls.
# To reuse our token, we need to save it somewhere
# First, let’s create variables for the token itself, the tokenType, and when it expires.
# Token
# var token, tokenType, expires;

# In our OAuth API call, once we get a token back, we’ll store the token details to those variables.
# The data.access_token will get assigned to token, and the data.token_type will get assigned to tokenType.
"""
{
  "token_type": "Bearer",
  "expires_in": 3600,
  "access_token": "a1b2c3d4e5"
}
"""

# If the existing token is still valid, we can skip getting a new one and immediately call our getPets() helper method.

