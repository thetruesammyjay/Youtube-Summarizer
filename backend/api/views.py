from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services.youtube_service import fetch_transcript
from .services.deepseek_services import summarize_text
from .utils.pdf_utils import generate_pedf
import json

@csrf_exempt
def summarize_video(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        video_url = data.get('video_url')

        # Fetch transcipt
        transcript = fetch_transcript(video_url)
        if not transcript:
            return JsonResponse({'error': 'Failed to fetch transcript'}, status = 400)
        
        # Summarize using DeepSeek R1
        summary = summarize_text(transcript)
        if not summary:
            return JsonResponse({'error': 'Failed to generate summary'}, status = 400)
        return JsonResponse({'summary': summary})

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@crsf_exempt
def download_pdf(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        summary = data.get('summary')

        # Generate PDF
        pdf_file = generate_pdf(summary)
        if not pdf_file:
            return JsonResponse({'pdf_url': pdf_file})

    return JsonResponse({'error': 'Invalid request method'}, status=405)