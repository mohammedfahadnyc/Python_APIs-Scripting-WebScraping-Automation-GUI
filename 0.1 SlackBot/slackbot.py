# import requests
# from slack_bolt import App
# from flask import Flask, jsonify

# SLACK_APP_TOKEN = os.environ.get['SLACK_APP_TOKEN']  # basic info -app level token - add scope
# SLACK_BOT_TOKEN = os.environ.get['SLACK_BOT_TOKEN]  # oauth bot token
# SLACK_USER_TOKEN = os.environ.get['SLACK_USER_TOKEN'] #oauth user token                    

# app = Flask(__name__)



# @app.route('/')
# def home():
#     return "Hello"


# # take user_id as a url-parameter and returns user's channels

# @app.route('/user/<user_id>')
# def find_user_id(user_id):
#     headers = {
#         'Authorization': 'Bearer SLACK_USER_TOKEN'}
#     params = {'user': user_id}
#     data = requests.get(url='https://slack.com/api/users.conversations', headers=headers, params=params).json()
#     # print(data)
#     channels = data['channels']
#     channel_id = []
#     channel_name = []
#     for channel in channels:
#         channel_id.append(channel['id'])
#         channel_name.append(channel['name'])
#     print(channel_id)
#     print(channel_name)
#     return jsonify(user=user_id, channels=channel_name)

                                 
                                
# #2 Add new user to all of hl's channels via url parameter using hl and new user's id                                 

# @app.route('/add/<user_id>/<member_id>')
# def add_member(user_id, member_id):
#     # channels = ['C03JZJLDY7R', 'C03KE4UAWM9', 'C03KE9G8W9G', 'C03L3V5MVEU', 'C03L3VBK03A', 'C03LJJ37SVD', 'C03LZ6BA63U']

#     # getting all the channels of the HL
#     headers = {
#         'Authorization': 'Bearer SLACK_USER_TOKEN'}
#     params = {'user': user_id}
#     data = requests.get(url='https://slack.com/api/users.conversations', headers=headers, params=params).json()
#     # print(data)
#     channels = data['channels']
#     channel_id = []
#     channel_name = []
#     for channel in channels:
#         channel_id.append(channel['id'])
#         channel_name.append(channel['name'])
#     # added channels to channel list
#     print(channel_id)
#     print(channel_name)

#     # Adding user to the channels
#     for (channel, channel_name) in zip(channel_id[5:], channel_name[5:]):
#         params = {'channel': f'{channel}', 'users': ['U03LT7U5DBP']}
#         add = requests.post(url='https://slack.com/api/conversations.invite', headers=headers, params=params).json()
#         # if added, json response will be {'ok': True}, if already in group the json response would be {'ok': False, 'error': 'already_in_channel'}
#         #      print(add)
#         #      print("\n")
#         #      print(add['ok'])
#         if add['ok'] == True:
#             print((f"Successfully added to the channel {channel_name}"))
#             # return (f"Successfully added to the channel {channel_name}")
#         elif add['ok'] == False:
#             print(f"Already in {channel_name}")
#             # return (f"Already in {channel_name}")

#     return ("Added Successfully")


# if __name__ == '__main__':
#     app.run(debug=True, port=8080)









# #testing slack api's


# #1. Getting channels of a user

# # headers = {
# #     'Authorization': 'Bearer SLACK_USER_TOKEN'}
# # params = {'user': 'member_id_goes_here'}
# # data = requests.get(url='https://slack.com/api/users.conversations', headers=headers, params=params).json()
# # # print(data)
# # channels = data['channels']
# # channel_id = []
# # channel_name = []
# # for channel in channels:
# #     channel_id.append(channel['id'])
# #     channel_name.append(channel['name'])
# #  added channels to channel list
# # print(channel_id)
# # print(channel_name)



# # 2. Add new user to the public channels the HL is a part of
# # import requests
# # headers = {'Authorization': 'Bearer SLACK_USER_TOKEN'}
# # channels = ['C03JZJLDY7R', 'C03KE4UAWM9', 'C03KE9G8W9G', 'C03L3V5MVEU', 'C03L3VBK03A', 'C03LJJ37SVD', 'C03LZ6BA63U']
# # for channel in channels[5:] :
# #     params = {'channel': f'{channel}', 'users':['U03LT7U5DBP']}
# #     add = requests.post(url='https://slack.com/api/conversations.invite',headers=headers,params=params).json()

# # #if added, json response will be {'ok': True},
# # if already in group the json response would be {'ok': False, 'error': 'already_in_channel'}

# #     if add['ok'] == True :
# #         print (f"Successfully added to the channel {channel}")
# #     elif add['ok'] == False :
# #         print(f"Already in {channel}")
                                 
                                 
                                 
# #3. Handling Slash Commands
#     #use slash commands
# # @app.route('/slash',methods=["GET","POST"])
# # def slash():
# #       #sents all the dictionary key val pair
# #     if request.method == "POST" :
# #         data = request.form
# #         user_id = data.get('user_id')
# #         channel_id = data.get('channel_id')
# #         #client.chat_postmessage(channel=channel_id,text="I got the command")
# #         return Response(),200
# #     return ("Simple get request")

                                 

# #extracting userid from /slash command payload
# #data = ImmutableMultiDict([('token', 'qrxsSTRiBNwmHkpBbg4Y20T6'), ('team_id', 'T03KB9JUJ77'), ('team_domain', 'slackbottest-jc28549'), ('channel_id', 'C03L3VBK03A'), ('channel_name', 'test'), ('user_id', 'U03JZJFT1N3'), ('user_name', 'fahadmohammed299299'), ('command', '/slash'), ('text', '<@U03LT7U5DBP|fahadbiznes>'), ('api_app_id', 'A03KSSHPL65'), ('is_enterprise_install', 'false'), ('response_url', 'https://hooks.slack.com/commands/T03KB9JUJ77/3814495845920/rXxVNnnOFFVPt2ZTXgZksDWw'), ('trigger_id', '3784130504694.3657324970245.070398f317dae4af941ee5066c022027')]).to_dict()
# #userid = data['text'].split('|')[0].split('@')[1]






#3-4-5

import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_find_user_channels_valid_user_id(client):
    user_id = 'valid_user_id'
    response = client.get(f'/find-user-channels/{user_id}')
    assert response.status_code == 200
    # Assert the expected response based on the valid user ID

def test_find_user_channels_invalid_user_id(client):
    user_id = 'invalid_user_id'
    response = client.get(f'/find-user-channels/{user_id}')
    assert response.status_code == 400
    # Assert the error response based on the invalid user ID

def test_find_user_channels_error_communicating_with_server(client, monkeypatch):
    def mock_get(*args, **kwargs):
        raise Exception("Error communicating with the server")

    monkeypatch.setattr('requests.get', mock_get)

    user_id = 'valid_user_id'
    response = client.get(f'/find-user-channels/{user_id}')
    assert response.status_code == 500
    # Assert the error response when there is an error communicating with the server

def test_add_member_success(client):
    user_id = 'valid_user_id'
    channel_id = 'valid_channel_id'
    response = client.post(f'/add-member/{user_id}/{channel_id}')
    assert response.status_code == 200
    # Assert the expected response based on the successful addition of a user to a channel

def test_add_member_error_communicating_with_server(client, monkeypatch):
    def mock_post(*args, **kwargs):
        raise Exception("Error communicating with the server")

    monkeypatch.setattr('requests.post', mock_post)

    user_id = 'valid_user_id'
    channel_id = 'valid_channel_id'
    response = client.post(f'/add-member/{user_id}/{channel_id}')
    assert response.status_code == 500
    # Assert the error response when there is an error communicating with the server

def test_find_user_all_channels_helper_valid_user_id():
    user_id = 'valid_user_id'
    result = find_user_all_channels_helper(user_id)
    assert result is not None
    # Assert the expected result based on the valid user ID

def test_find_user_all_channels_helper_invalid_user_id():
    user_id = 'invalid_user_id'
    result = find_user_all_channels_helper(user_id)
    assert result is None
    # Assert the expected result based on the invalid user ID


#6-7-8
import pytest
from app import (
    all_channels_parser,
    invite_helper,
    get_channels_helper
)

def test_all_channels_parser_valid_data():
    channel_data = {
        "ok": True,
        "channels": [
            {"id": "channel_id1", "name": "channel_name1"},
            {"id": "channel_id2", "name": "channel_name2"}
        ]
    }
    channel_ids, channel_names = all_channels_parser(channel_data)
    assert channel_ids == ["channel_id1", "channel_id2"]
    assert channel_names == ["channel_name1", "channel_name2"]

def test_all_channels_parser_invalid_data():
    channel_data = {
        "ok": False,
        "error": "Invalid channel data"
    }
    channel_ids, channel_names = all_channels_parser(channel_data)
    assert channel_ids is None
    assert channel_names is None

def test_invite_helper_valid_parameters(monkeypatch):
    def mock_post(*args, **kwargs):
        # Simulate successful response from Slack API
        return {"ok": True}

    monkeypatch.setattr('requests.post', mock_post)

    user_id = "valid_user_id"
    channel_id = "valid_channel_id"
    trigger_id = "valid_trigger_id"
    header = {"Authorization": "Bearer valid_token"}
    invoker = "valid_invoker"

    response = invite_helper(user_id, channel_id, trigger_id, header, invoker)
    assert response["ok"] is True
    # Assert the expected response based on the valid parameters

def test_invite_helper_invalid_parameters(monkeypatch):
    def mock_post(*args, **kwargs):
        # Simulate error response from Slack API
        return {"ok": False, "error": "Invalid parameters"}

    monkeypatch.setattr('requests.post', mock_post)

    user_id = "invalid_user_id"
    channel_id = "invalid_channel_id"
    trigger_id = "invalid_trigger_id"
    header = {"Authorization": "Bearer invalid_token"}
    invoker = "invalid_invoker"

    response = invite_helper(user_id, channel_id, trigger_id, header, invoker)
    assert response["ok"] is False
    # Assert the error response based on the invalid parameters

def test_get_channels_helper_valid_parameters(monkeypatch):
    def mock_post(*args, **kwargs):
        # Simulate successful response from Slack API
        return {"ok": True, "channels": ["channel1", "channel2"]}

    monkeypatch.setattr('requests.post', mock_post)

    user_id = "valid_user_id"
    chat_channel = "valid_chat_channel"
    header = {"Authorization": "Bearer valid_token"}

    response = get_channels_helper(user_id, chat_channel, header)
    assert response["ok"] is True
    # Assert the expected response based on the valid parameters

def test_get_channels_helper_invalid_parameters(monkeypatch):
    def mock_post(*args, **kwargs):
        # Simulate error response from Slack API
        return {"ok": False, "error": "Invalid parameters"}

    monkeypatch.setattr('requests.post', mock_post)

    user_id = "invalid_user_id"
    chat_channel = "invalid_chat_channel"
    header = {"Authorization": "Bearer invalid_token"}

    response = get_channels_helper(user_id, chat_channel, header)
    assert response["ok"] is False
    # Assert the error response based on the invalid parameters

#9,10,11,12

import pytest
from app import (
    add_multiple_users_to_channels_async_helper,
    all_channels_modal,
    help_nodal,
    interaction_manager
)

def test_add_multiple_users_to_channels_async_helper_valid_parameters(monkeypatch):
    def mock_post(*args, **kwargs):
        # Simulate successful response from Slack API
        return {"ok": True}

    monkeypatch.setattr('requests.post', mock_post)

    invoking_user = "valid_invoking_user"
    channel_ids = ["channel_id1", "channel_id2"]
    user_ids = ["user_id1", "user_id2"]
    chat_channel = "valid_chat_channel"

    response = add_multiple_users_to_channels_async_helper(invoking_user, channel_ids, user_ids, chat_channel)
    assert response["ok"] is True
    # Assert the expected response based on the valid parameters

def test_add_multiple_users_to_channels_async_helper_invalid_parameters(monkeypatch):
    def mock_post(*args, **kwargs):
        # Simulate error response from Slack API
        return {"ok": False, "error": "Invalid parameters"}

    monkeypatch.setattr('requests.post', mock_post)

    invoking_user = "invalid_invoking_user"
    channel_ids = ["channel_id1", "channel_id2"]
    user_ids = ["user_id1", "user_id2"]
    chat_channel = "invalid_chat_channel"

    response = add_multiple_users_to_channels_async_helper(invoking_user, channel_ids, user_ids, chat_channel)
    assert response["ok"] is False
    # Assert the error response based on the invalid parameters

def test_all_channels_modal():
    # Write test to validate the behavior of the all_channels_modal function
    # You can use the test client to simulate the request and assert the response

def test_help_nodal():
    # Write test to validate the behavior of the help_nodal function
    # You can use the test client to simulate the request and assert the response

def test_interaction_manager():
    # Write test to validate the behavior of the interaction_manager function
    # You can use the test client to simulate the request and assert the response


