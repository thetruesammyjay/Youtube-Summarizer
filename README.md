
# YouTube Summarizer

The YouTube Summarizer is a web application that allows users to input a YouTube video URL and receive a concise summary of the video's content. The app also provides the option to download the summary as a PDF.

---

## Features

- **Summarize YouTube Videos**: Input a YouTube video URL and get a summary of the video's transcript.
- **Download as PDF**: Download the summarized content as a PDF for offline use.
- **User-Friendly Interface**: Clean and intuitive frontend built with React.
- **Backend Powered by Django**: Robust backend for handling video processing and summarization.

---

## Technologies Used

### Frontend
- React: A JavaScript library for building user interfaces.
- CSS: For styling the application.

### Backend
- Django: A Python web framework for building the backend.
- YouTube Transcript API: For fetching video transcripts.
- DeepSeek API: For summarizing the transcript (optional, if you integrate it).
- FPDF2: For generating PDFs.

### Deployment
- GitHub: For version control and hosting the repository.
- Heroku/Netlify: For deploying the backend and frontend (optional).

---

## Installation

### Prerequisites
- Node.js: For running the React frontend.
- Python 3.8+: For running the Django backend.
- Git: For version control.

### Steps

1. Clone the Repository:
   ```bash
   git clone https://github.com/thetruesammyjay/Youtube-Summarizer.git
   cd Youtube-Summarizer
   ```

2. Set Up the Backend:
   - Navigate to the `backend` directory:
     ```bash
     cd backend
     ```
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Run the Django development server:
     ```bash
     python manage.py runserver
     ```

3. Set Up the Frontend:
   - Navigate to the `frontend` directory:
     ```bash
     cd frontend
     ```
   - Install Node.js dependencies:
     ```bash
     npm install
     ```
   - Start the React development server:
     ```bash
     npm start
     ```

4. Access the Application:
   - Open your browser and go to `http://localhost:3000`.

---

## Usage

1. Enter YouTube Video URL:
   - On the homepage, paste the URL of the YouTube video you want to summarize.

2. Get Summary:
   - Click the "Summarize" button to generate a summary of the video's transcript.

3. Download as PDF:
   - After the summary is generated, click the "Download as PDF" button to save the summary as a PDF.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License

This project is licensed under the MIT License. 

---

## Acknowledgments

- YouTube Transcript API: For fetching video transcripts.
- DeepSeek: For providing the summarization API.
- React and Django Communities: For their amazing documentation and support.

---

## Contact

If you have any questions or feedback, feel free to reach out:

- Name: Ifiezibe Justin Samuel 
- Email: thetruesammyjay@gmail.com
- GitHub: [thetruesammyjay](https://github.com/thetruesammyjay)
