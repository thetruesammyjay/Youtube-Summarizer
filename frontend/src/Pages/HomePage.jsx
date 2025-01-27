import React, { useState } from 'react';
import VideoInput from '../components/VideoInput';
import SummaryDisplay from '..components/SummaryDisplay';
import PdfExport from '..components/PdfExport';
import { summarizeVideo, downloadPdf } from '..utils/api';

function HomePage() {
    const [videoUrl, setVideoUrl]= useState('');
    const [summary, setSummary] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState('');

    const handleSummarize = async () => {
        setLoading(true);
        setError('');
        try{
            const response = await summarizeVideo(videoUrl);
            if (response.summary) {
                setSummary(response.summary)
            }
            else{
                setError('Failed to generate summary. Please try again. ');
            }
        }
        catch(err){
            setError('An error occurred. Please check your URL and try again. ');
        }
        finally{
            setLoading(false);
        }
    };

    const handleDownloadPdf = async () => {
        if (!summary) return;
        try {
            const response = await downloadPdf(summary);
            if (response.pdf_url) {
                window.open(response.pdf_url, '_blank');
            }
            else {
                setError('An error occured while generating the PDF.');
            }
        }
        catch (err) {
            setError('An error occured while generating the PDF. ');
        }
    };

    return(
        <div className="home-page">
            <h1> YouTube Summarizer</h1>
            <VideoInput
                videoUrl={videoUrl}
                setVideoUrl={setVideoUrl}
                onSummarize={handleSummarize}
                loading={loading}
            />
            {error && <p className="error">{error}</p>}
            <SummaryDisplay summary={summary} />
            {summary && <PdfExport onDownload= {handleDownloadPdf} />}
        </div>
    )
}

export default HomePage;