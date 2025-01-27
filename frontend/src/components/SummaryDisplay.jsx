import React from 'react';

function SummaryDisplay({ summary}) {
    return(
        <div className="summary-display">
            <h2>Summary</h2>
            <p>{summary}</p>
        </div>
    );
}

export default SummaryDisplay;