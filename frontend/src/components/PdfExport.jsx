import React from 'react';

function PdfExport({ onDownload}){
    return(
        <div className="pdf-export">
            <button onClick={onDownload}>Download as PDF</button>
        </div>
    );
}

export default PdfExport;