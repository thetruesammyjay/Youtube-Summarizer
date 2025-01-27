import React from 'react';

function VideoInput({ videoUrl, setVideoUrl, onSummarize, loading}) {
    return(
        <div className="video-input">
            <input
                type="text"
                placeholder="Enter YouTube Video URL "
                value={videoUrl}
                onChange={(e) => setVideoUrl(e.target.value)}
            />
            <button onClick={onSummarize} disabled={loading}>
                {loading ? 'Summarizing...' : 'Summarize'}
            </button>
        </div>
    );
}

export default VideoInput;