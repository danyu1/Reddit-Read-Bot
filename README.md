# Reddit-Read-Bot
This bot will monitor a particular subreddit for new posts, and when someone posts "[text]”, it will reply “[text]”.

Using praw to access the reddit api the bot will read through subreddits automatically and response when needed.

# Info on praw package: 

![download](https://github.com/danyu1/Reddit-Read-Bot/assets/115963400/60cbcf47-f2d2-4e37-9cf0-18a02ddb8b3e)

[praw package](https://praw.readthedocs.io/en/stable/code_overview/reddit_instance.html)

->created reddit class instance

->don't mess with praw.ini file

->used funcs: message, reply

## jSON usages
json api used to reply with random [jokes](https://icanhazdadjoke.com/api)

Useful tool to read json files and extract / fetch what you need effeciently:

### Important Notes
Imported os and sys operating systems in order to read file paths and read terminal inputs


Os was used to read text files that contained comment id's

sys was used to read the terminal to determine .txt file path and body/subject of the message that you would want to send through the bot

This has not yet been packaged so you cannout use it outside of the redditBot.py class. Feel free to create your own

