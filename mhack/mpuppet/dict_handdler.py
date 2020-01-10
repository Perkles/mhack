from urllib import parse

def get_gh_authentication_token(input_dict):
    response = []
    input_dict = parse.parse_qs(parse.urlsplit(input_dict.text).path)
    for key, value in input_dict.items():
        if (key == 'access_token'):
            response.append(str(value).replace('[', '').replace("'", '').replace("]", ''))
        elif (key == 'token_type'):
            response.append(str(value).replace('[', '').replace("'", '').replace("]", ''))
    return response

# Whould be better have a function who takes a arbitrarie number of values
# ... and returnes the match values.
def extract_from(data_type, the_subject):
    for key, value in data_type.items():
        if (key == the_subject):
            return value