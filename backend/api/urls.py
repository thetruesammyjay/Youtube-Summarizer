from django.urls import path
from .views import summarize_video, download_pdf

urlpatterns = [
    path('summarize/', summarize_video, name='summarize_video'),
    path('download-pdf/', download_pdf, name='download_pdf')
]