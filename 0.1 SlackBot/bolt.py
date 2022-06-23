

import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler


SLACK_APP_TOKEN = "xapp-1-A03KSSHPL65-3654924430838-d4c7cca46549ea8e53b9217d8cd4eaaf866972893e3dcf8d4e3547cd0484982e" #basic info -app level token - add scope
SLACK_BOT_TOKEN = 'xoxb-3657324970245-3662649764932-KCBEPXF1GwOrbVxjui3V2gdi'           #oauth bot token
# Initializes your app with your bot token and socket mode handler
app = App(token=SLACK_BOT_TOKEN)

# 1. Listens to incoming messages that contain "hello"

# @app.message("hello")
# def message_hello(message, say):
#     # say() sends a message to the channel where the event was triggered
#     say(f"Hey there  <@{message['user']}>!")


#2 - Sending and responding to actions

@app.message('hello')
def message_hello(message, say):
    # say() sends a message to the channel where the event was triggered
    say(
        blocks=[
            {
                "type": "section",
                "text": {"type": "mrkdwn", "text": f"Hey there <@{message['user']}>!"},
                "accessory": {
                    "type": "button",
                    "text": {"type": "plain_text", "text": "Click Me"},
                    "action_id": "button_click"
                }
            }
        ],
        text=f"Hey there <@{message['user']}>!"
    )


@app.action("button_click")
def action_button_click(body, ack, say):
    # Acknowledge the action
    ack()
    say(f"<@{body['user']['id']}> clicked the button")


@app.message(":wave:")
def say_hello(message, say):
    user = message['user']
    say(f"Hi there, <@{user}>!")

#Schedule a message - calling chat_schedulemssage api
@app.message("wake me up")
def say_hello(client, message):
    # Unix Epoch time for September 30, 2020 11:59:59 PM
    when_september_ends = 1655150400 #use convo_info to print out the timestamp,use timestamp to see live demo
    channel_id = message["channel"]
    client.chat_scheduleMessage(
        channel=channel_id,
        post_at=when_september_ends,
        text="Summer has come and passed"
    )


#adding users to the channel by user id - using conversations_invite
@app.message('invite')
def invite(client,message):
    channel_id = message["channel"]
    client.conversations_invite(
        channel=channel_id,
        users = ['W1234567890','U2345678901','U3456789012']
    )

#conversation_info
@app.message('convo_info')
def conversation_info(client,message):
    channel_id = message['channel']
    info = client.conversations_info ( channel=channel_id)
    # print (info)
    print(client)
    print(message)

    
    
 #find all channels of a user. How do we find user id? - user sends a message and we hold the user id using the message payload.

@app.message('allchannels')
def find_all_channels(client,message):
    user_id = message['user']
    headers ={'Authorization':'Bearer xoxp-3657324970245-3645627919751-3685545535376-f19195d2433c6379ae66cbbdfdf925e2'}
    params = {'user':user_id}
    data = requests.get(url='https://slack.com/api/users.conversations',headers=headers,params=params).json()
    channels = data['channels']
    channel_id = []
    channel_name = []
    for channel in channels :
        channel_id.append(channel['id'])
        channel_name.append(channel['name'])
    print(channel_id)
    print(channel_name)

# Start your app
if __name__ == "__main__":
    SocketModeHandler(app,SLACK_APP_TOKEN).start()
