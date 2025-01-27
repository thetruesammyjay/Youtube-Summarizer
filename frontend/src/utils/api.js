export const summarizeVideo = async (videoUrl) => {
    const response =  await fetch('/summarize/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json'},
        body: JSON.stringify({ video_url: videoUrl}), 
    });
    return response.json();
};

export const downloadPdf = async (summary) => {
    const response = await fetch('/api/download-pdf', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ summary}),
    });
    return response,json();
};