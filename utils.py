def get_audio_url(video_url):

    audio_url_part = 'DASH_audio.mp4?source=fallback'
    video_split = video_url.split('/')

    audio_split = video_split[:-1]
    audio_split.append(audio_url_part)

    audio_url = '/'.join(audio_split)

    return audio_url


def get_track_id(subreddit, submission):

    track_id = '{subreddit}{author}{name}'.format(
        subreddit=subreddit, name=str(submission.name),  author=str(submission.author))

    track_id = track_id.replace('_', '').replace('-', '')

    return track_id


def combine_audio(vidname, audname, path, fps=60):

    import moviepy.editor as mpe

    my_clip = mpe.VideoFileClip(vidname)

    audio_background = mpe.AudioFileClip(audname)

    final_clip = my_clip.set_audio(audio_background)

    final_clip.write_videofile(path, fps=fps)
