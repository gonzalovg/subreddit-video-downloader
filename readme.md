# SUBREDDIT-VIDEO-DOWNLOADER

Simple python script that gets a series of subreddits and donwloads the videos from "Top" window.


## SET-UP 🤖


### 1. Getting script dependencies
```
pip install -r requirements.txt
```


### 2. Configuring your .env file

First of all you need to copy .env.example file and save it as .env with your data.

```
CLIENT_ID = 0zNKhupgPUopBH7JhbtiyAQMn
CLIENT_SECRET = zAJZ8UY0UyX0bCfwQm2QJl-z8cP3uYJl

#Folder to store the videos
VIDEOS_FOLDER= ./videos/

#Subreddits you want to scrape, separated by comma (without spaces between them)
SUBREDDITS = Subreddit_1,Subreddit_2
```

### 3. Execute

```
python main.py
```


#### Hope it helps ❤️‍🔥