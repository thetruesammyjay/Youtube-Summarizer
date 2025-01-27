from youtube_transcript_api import YouTubeTranscriptApi

def fetch_transcript(video_url):
    try:
        # Extract the video ID from the URL
        video_id = video_url.split('v=')[1]
        
        # Fetch the transcript
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Combine all transcript entries into a single string
        transcript_text = ' '.join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None