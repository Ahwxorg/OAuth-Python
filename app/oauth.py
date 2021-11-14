import requests

class OAuth(object):
    client_id = "CLIENT ID"
    client_secret = "CLIENT SECRET"
    scope = "identify"
    redirect_url = "https://example.com/login"
    discord_login_url = "https://discord.com/api/oauth2/authorize?client_id={}&redirect_uri={}&response_type=code&scope={}".format(client_id, redirect_url, scope)
    discord_token_url = "https://discord.com/api/oauth2/token"
    discord_api_url = "https://discord.com/api"

    @staticmethod
    def get_user(code):
        data = {
            'client_id': OAuth.client_id,
            'client_secret': OAuth.client_secret,
            'grant_type': "authorization_code",
            'code': code,
            'redirect_uri': OAuth.redirect_url,
            'scope': OAuth.scope
        }

        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        access_token = requests.post(url = OAuth.discord_token_url, data = data, headers = headers)
        json = access_token.json()
        url = OAuth.discord_api_url + "/users/@me"
        headers = {
            "Authorization": "Bearer {}".format(json.get("access_token"))
        }
        user_object = requests.get(url = url, headers = headers)
        user_json = user_object.json()
        return user_json
