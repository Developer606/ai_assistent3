# from transformers import pipeline


# summariza = pipeline('summarization')

art = """A program is a set of instructions that a computer uses to perform a specific function. To use an analogy, a program is like a computer’s recipe. It contains a list of ingredients (called variables, which can represent numeric data, text, or images) and a list of directions (called statements) that tell the computer how to execute a specific task.

Programs are created using specific programming languages such as C++, Python, and Ruby. These are high level programming languages that are human-readable and writable. These languages are then translated into low level machine languages by compilers, interpreters, and assemblers within the computer system. Assembly language is a type of low level language that is one step above a machine language and technically can be written by a human, although it is usually much more cryptic and difficult to understand."""

# ps = summariza(art,max_length=130,min_length=30,do_sample=False)

# ast = ps[0]['summary_text']
# print(ast)
import base64
import json
import time
import traceback
import random

import requests

root_url = 'https://api.replicastudios.com'
client_id = 'kishor908853@gmail.com'
secret = 'kishor908853@'

txt = "Mom works. She never picks me up from school, and two miles is too close for a bus pickup, which is fine by me because I like cutting through the woods. Especially on autumn days, when the air is cool, and the flies and mosquitos are gone, and basketball practice hasn’t begun. I like the quiet. I like the wordlessness of the walk. A pretty sugar maple dressed in vivid orange frills beckons me off the path. I stand..."
audio_format = 'wav'


def get_access_token(client_id, secret):
    """
    Authenticates in /auth endpoint and returns the access token string.
    Note: token expires after an hour.
    """
    url = f"{root_url}/auth"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = f'client_id={client_id}&secret={secret}'
    response = requests.request("POST", url,
                                headers=headers,
                                data=payload)
    if response.status_code != 200:
        raise Exception(f'Auth failed. Response: {response.text}')
    # extract access_token from response
    jwt_access_token = response.json()['access_token']
    # print(f'Acquired JWT token: {jwt_access_token}\n')
    return jwt_access_token


def decode_jwt(access_token):
    """Takes raw JWT and returns the content of payload part as dictionary."""
    payload_b64 = access_token.split('.')[1]
    # fix base64 padding
    payload_b64 = payload_b64 + '=' * (4 - len(payload_b64) % 4)
    json_payload = base64.urlsafe_b64decode(payload_b64)
    payload_dict = json.loads(json_payload)
    return payload_dict


def get_voices(access_token):
    """Requests list of voices from /voice endpoint."""
    url = f"{root_url}/voice"
    response = requests.request("GET", url, headers={'Authorization': f'Bearer {access_token}'}, data={})
    voices = response.json()
    print(f'Found {len(voices)} voices.')
    return voices


def text_to_speech(access_token, txt, speaker_id, audio_format='wav'):
    """Returns audio URL for given text and speaker."""
    bit_rate = 128
    sample_rate = 22050
    url = f"{root_url}/speech"
    response = requests.request("GET", url,
                                params={'speaker_id': speaker_id,
                                        'txt': txt,
                                        'quality': 'low',
                                        'extension': audio_format,
                                        'bit_rate': bit_rate,
                                        'sample_rate': sample_rate},
                                headers={'Authorization': f'Bearer {access_token}'})
    response_text = response.text.encode('utf8')
    # print(response_text)
    response_json = json.loads(response_text)
    if response_json.get('error', None):
        print(f"\tERROR: {response_json['error']}, code: {response_json['error_code']}")
        raise Exception(f'Failed to generate "{txt}" with speaker {speaker_id}, error: {response_json["error_code"]}')
    if response_json.get('warning', None):
        print(f"\tWARNING: {response_json['warning']}")
    audio_url = response_json.get('url', None)
    return audio_url


if __name__ == '__main__':

    try:
        access_token = get_access_token(client_id, secret)

        access_token_payload = decode_jwt(access_token)
        exp = access_token_payload.get("exp")  # expiry in Epoch time
        permissions = access_token_payload.get("scopes")
        # print(f'Access token expiry: {time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(exp))}')
        # print(f'Permissions: {permissions}')
        if 'generate' not in permissions:
            raise Exception('Missing "generate" permission. Did you run out of credits?')

        voices = get_voices(access_token)

        # let's try to find Deckard, otherwise just use the first voice
        voice = next((voice for voice in voices if voice['name'] == 'Amber'), voices[590])

        # print(f'Using voice: {voice["name"]} {voice["uuid"]}')

        speaker_id = voice["uuid"]

        audio_url = text_to_speech(access_token, txt, speaker_id, audio_format)

        # print(f'Audio URL: {audio_url}')

        r = requests.get(audio_url)
        r = requests.get(audio_url)
        num = random.randint(0,10000000)
        re = str(num)
        filename = re+voice['name'] + '.' + audio_format
        # print(filename)
        with open(filename, 'wb') as f:

          f.write(r.content)
        # if 'Pink Dragon - Angry.wav' in filename:
        #   t= open("auudio\\Pink Dragon_Angry","w")
        #   t.writable(f)


        #   print(f'Saved to file: {filename}')

    except Exception as e:
        print(f'EXCEPTION: {e}')
        traceback.print_exc()
