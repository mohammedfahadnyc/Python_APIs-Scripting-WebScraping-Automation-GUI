import requests
from slack_bolt import App
from flask import Flask, jsonify

SLACK_APP_TOKEN = os.environ.get['SLACK_APP_TOKEN']  # basic info -app level token - add scope
SLACK_BOT_TOKEN = os.environ.get['SLACK_BOT_TOKEN]  # oauth bot token
SLACK_USER_TOKEN = os.environ.get['SLACK_USER_TOKEN'] #oauth user token                    

app = Flask(__name__)



@app.route('/')
def home():
    return "Hello"


# take user_id as a url-parameter and returns user's channels

@app.route('/user/<user_id>')
def find_user_id(user_id):
    headers = {
        'Authorization': 'Bearer SLACK_USER_TOKEN'}
    params = {'user': user_id}
    data = requests.get(url='https://slack.com/api/users.conversations', headers=headers, params=params).json()
    # print(data)
    channels = data['channels']
    channel_id = []
    channel_name = []
    for channel in channels:
        channel_id.append(channel['id'])
        channel_name.append(channel['name'])
    print(channel_id)
    print(channel_name)
    return jsonify(user=user_id, channels=channel_name)

                                 
                                
#2 Add new user to all of hl's channels via url parameter using hl and new user's id                                 

@app.route('/add/<user_id>/<member_id>')
def add_member(user_id, member_id):
    # channels = ['C03JZJLDY7R', 'C03KE4UAWM9', 'C03KE9G8W9G', 'C03L3V5MVEU', 'C03L3VBK03A', 'C03LJJ37SVD', 'C03LZ6BA63U']

    # getting all the channels of the HL
    headers = {
        'Authorization': 'Bearer SLACK_USER_TOKEN'}
    params = {'user': user_id}
    data = requests.get(url='https://slack.com/api/users.conversations', headers=headers, params=params).json()
    # print(data)
    channels = data['channels']
    channel_id = []
    channel_name = []
    for channel in channels:
        channel_id.append(channel['id'])
        channel_name.append(channel['name'])
    # added channels to channel list
    print(channel_id)
    print(channel_name)

    # Adding user to the channels
    for (channel, channel_name) in zip(channel_id[5:], channel_name[5:]):
        params = {'channel': f'{channel}', 'users': ['U03LT7U5DBP']}
        add = requests.post(url='https://slack.com/api/conversations.invite', headers=headers, params=params).json()
        # if added, json response will be {'ok': True}, if already in group the json response would be {'ok': False, 'error': 'already_in_channel'}
        #      print(add)
        #      print("\n")
        #      print(add['ok'])
        if add['ok'] == True:
            print((f"Successfully added to the channel {channel_name}"))
            # return (f"Successfully added to the channel {channel_name}")
        elif add['ok'] == False:
            print(f"Already in {channel_name}")
            # return (f"Already in {channel_name}")

    return ("Added Successfully")


if __name__ == '__main__':
    app.run(debug=True, port=8080)









#testing slack api's


#1. Getting channels of a user

# headers = {
#     'Authorization': 'Bearer SLACK_USER_TOKEN'}
# params = {'user': 'member_id_goes_here'}
# data = requests.get(url='https://slack.com/api/users.conversations', headers=headers, params=params).json()
# # print(data)
# channels = data['channels']
# channel_id = []
# channel_name = []
# for channel in channels:
#     channel_id.append(channel['id'])
#     channel_name.append(channel['name'])
#  added channels to channel list
# print(channel_id)
# print(channel_name)



# 2. Add new user to the public channels the HL is a part of
# import requests
# headers = {'Authorization': 'Bearer SLACK_USER_TOKEN'}
# channels = ['C03JZJLDY7R', 'C03KE4UAWM9', 'C03KE9G8W9G', 'C03L3V5MVEU', 'C03L3VBK03A', 'C03LJJ37SVD', 'C03LZ6BA63U']
# for channel in channels[5:] :
#     params = {'channel': f'{channel}', 'users':['U03LT7U5DBP']}
#     add = requests.post(url='https://slack.com/api/conversations.invite',headers=headers,params=params).json()

# #if added, json response will be {'ok': True},
# if already in group the json response would be {'ok': False, 'error': 'already_in_channel'}

#     if add['ok'] == True :
#         print (f"Successfully added to the channel {channel}")
#     elif add['ok'] == False :
#         print(f"Already in {channel}")
