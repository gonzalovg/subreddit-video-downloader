import os

import praw
from dotenv import load_dotenv

from utils import *

load_dotenv()

# Folder where you will save your videos
VIDEOS_FOLDER = os.getenv('VIDEOS_FOLDER')

# Get your reddit application credentials
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

# Subreddits with the videos you want
subreddits = os.getenv('SUBREDDITS').split(',')


def main():
    # Build your reddit client
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent='Video downloader by /u/Positive-Strategy-86'
    )
    # Iterate over your selected subreddit
    for subreddit in subreddits:
        # Get hottest 50 posts of each subreddit
        # If it is a video, it will download it to your selected folder
        for submission in reddit.subreddit(subreddit).hot(limit=50):

            if submission.is_video:

                multimedia_info = submission.media
                video_id = get_track_id(subreddit, submission)
                video_url = str(
                    multimedia_info['reddit_video']['fallback_url'])
                audio_url = get_audio_url(video_url)

                video_path = VIDEOS_FOLDER + video_id + '.mp4'

                # Combine video and audio tracks to create your video
                combine_audio(vidname=video_url,
                              audname=audio_url, path=video_path)


if __name__ == '__main__':
    main()
