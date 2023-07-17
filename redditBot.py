import praw
import config
import time
import os
import sys
import requests

global subs
subs = ["DOG", "xqcow", "ask", "rateme", "AskReddit", "NoStupidQuesitons", "Wellthatsucks", "Rainbow6", "ksi", "facepalm", "trackandfield", "Damnthatsinteresting", "PublicFreakout", "DOG"]
global cycles
cycles = 0

def bot_login ():
    print ("Loggin in...")
    reddit = praw.Reddit(username = config.username, 
            passwod = config.password, 
            client_id = config.client_id, 
            client_secret = config.client_secret, 
            user_agent = "danyuL-'s sigh responder")
    print ("Logged in...")

    return reddit
    
def run_bot (r, already_replied_to, cycles):
    print ("Running the first wave.")
    counter = 0
    for subreds in subs:
        print (f"Reading from {subreds}...")
        #loop through the list of subreds and search for comments contain the string 'dog'
        for comments in r.subreddit(subreds).comments(limit=25):
            if "dog" in comments.body and comments.id not in already_replied_to and comments.author != r.user.me():
                #append the id of the comment to the list so that when we check if we already replied it will return true
                already_replied_to.append (comments.id)
                #a parameter means that you're going to append to the file
                with open ("already_replied_to.txt", "a") as file:
                    file.write(comments.id + "\n")

                print (f"String with \"dog\" found!! replied to comment id: {comments.id}")
                #fetch the open source api and get the joke from the json format
                joke = requests.get('https://icanhazdadjoke.com/slack').json()['attachments']
                #comments.reply(f"I see you have [dog](https://imgur.com/gallery/AobmBUw) in your reddit comment. \n\nHeres a nice joke: {joke}")
                counter += 1

        if counter == 0:
            print (f"Nothing found in {subreds}.")
        else:
            print (f"Replied to {counter} comments in {subreds}.")  
        #sleep the program for ten seconds in order to avoid overflow
        time.sleep(2)
        counter = 0
    print (f"new cycle ----------------------------{cycles}")

#making sure that the comments already replied to will never get replied to again even after rerunning the entire program
def get_saved_comments ():
    if not os.path.isfile("already_replied_to.txt"):
        already_replied_to = []
    else:
        #r parameter means you're going to read the file
        with open("already_replied_to.txt", "r") as file:
            already_replied_to = file.read()
            #split reads every new line character and puts it into an array format
            already_replied_to = already_replied_to.split("\n")
            #already_replied_to = filter(None, already_replied_to)
        return already_replied_to

#for sending dms
def get_usernames(filename):
    try:
        with open (filename, "r") as file:
            usernames = file.read()
            usernames = usernames.split("\n")
            #usernames = filter(None, usernames)
    except IOError:
        print (f"Error: File {filename} was not found in the current directory.")
        quit ()
    return usernames

def send_message (reddit, username, subject, message):
    try:
        reddit.redditor(username).message(subject, message)
    except praw.exceptions.APIException as e:
        #first arg in the command line after the exception is thrown
        print (e.args[0])
        if "USER_DOESNT_EXIST" in e.args[0]:
            print (f"Redditor {username} was not found didn't send the message.")
            return
        else:
            print (f"Sent message to {username}!")


if not len(sys.argv) == 4:
    print ("usage: redditBoy.py file \"subject\" \"body\"")

filename = sys.argv [1]
subject = sys.argv [2]
body = sys.argv [3]

#this will run the bot cycle x times
already_replied_to = get_saved_comments ()
reddit = bot_login()
usernames = get_usernames(filename)
# for i in range (5):   
#     run_bot (reddit, already_replied_to, cycles)
#     cycles += 1

for username in usernames:
    send_message(reddit, username, subject, body)