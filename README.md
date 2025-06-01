# 🎓 DSEU College Helpdesk AI Chatbot

This is an AI-powered chatbot built using Streamlit and the Google Gemini API to assist users with queries related to Delhi Skill and Entrepreneurship University (DSEU). The chatbot answers questions specifically about DSEU, including admissions, courses, faculty, fees, campuses, events, contact information, results, placements, and more.

---

## Features

- Conversational AI interface powered by Google Gemini API (`gemini-2.0-flash`)
- Focused responses related only to DSEU
- Example questions sidebar to guide users
- Real-time chat display with user and assistant messages
- Simulated admin dashboard for viewing recent chat logs
- Option to download chat logs as a `.txt` file for record-keeping

---

## Getting Started

### Prerequisites

- Python 3.8+
- Streamlit
- Google Generative AI Python SDK (`google-generativeai`)
- A valid Google Gemini API key

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yadavhitesh380/college-chatbot.git
   cd college-chatbot
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set your Gemini API key in `.streamlit/secrets.toml`:

   ```toml
   [default]
   gemini_api_key = "YOUR_GOOGLE_GEMINI_API_KEY"
   ```

### Running the App

```bash
streamlit run main.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`) to interact with the chatbot.

---

## Usage

- Type your questions related to DSEU in the chat input.
- Use the example questions in the sidebar as inspiration.
- Admins can view and download chat logs from the simulated dashboard section.

---

## Project Structure

```
├── main.py               # Main Streamlit app
├── requirements.txt      # Python dependencies
├── .streamlit/
│   └── secrets.toml      # Store Gemini API key securely
└── README.md             # Project documentation
```

---

## Notes

- The chatbot is explicitly instructed to respond only about DSEU and ignore queries about other colleges or universities.
- Chat logs are saved in the session and can be downloaded as a text file.
- Make sure to keep your Gemini API key secure and do not expose it publicly.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- Built with [Streamlit](https://streamlit.io/)
- Powered by [Google Gemini API](https://developers.generativeai.google/)
