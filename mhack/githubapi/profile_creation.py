import requests, json

def fill_profile_with_github_user_info(request):
    access_token = request.session.get('access_token')
    token_type = request.session.get('token_type')

    headers = {'Authorization': '{} {}'.format(token_type, access_token)}
    json_response = requests.get('https://api.github.com/user', headers=headers).json()
    print(depack(json_response))
    # github_id, name, avatar_url, email = depack(json_response)
    # print("github_id " + github_id)
    # print("name " + name)
    # print("avatar_url " + avatar_url)
    # print("email " + email)


def depack(json_response):
    for key, value in json_response.items():
        # print(key, value)
        results = []
        if (key == "id"):
            results.append(value)
        if (key == "name"):
            results.append(value)
        if (key == "avatar_url"):
            results.append(value)
        if (key == "email"):
            results.append(value)
    return results