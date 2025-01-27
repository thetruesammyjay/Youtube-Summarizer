from youtube_transcript_api import YouTubeTransciptApi

def fetch_transcript(video_url):
    try:
        video_id = video_url.split('v=')[1]
        transcript = YouTubeTranscript.get_transcript(video_id)
        return ' '.join([entry['test'] for entry in transcript])
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None 