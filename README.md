
<h1 align="center">🎓 GGSIPU College Helpdesk AI Chatbot</h1>

<p align="center">
  An interactive <strong>AI-powered chatbot</strong> built using <strong>Streamlit</strong> and <strong>Google Gemini API</strong> to assist users with queries related to Guru Gobind Singh Indraprastha University (GGSIPU).<br>
  Designed to answer queries about admissions, courses, faculty, fees, events, and more — all specific to GGSIPU.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Built%20With-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white"/>
  <img src="https://img.shields.io/badge/Powered%20By-Gemini%20AI-blue?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Made%20by-Hitesh%20Yadav-blueviolet?style=for-the-badge"/>
</p>

---

## ✨ Features

- 💬 Conversational AI trained to answer only GGSIPU-related questions
- 🔍 Predefined example queries in the sidebar for quick help
- 📄 Document upload support for relevant materials (e.g. brochures)
- 🧑‍💼 Admin dashboard to view and manage chat logs
- 💾 Download complete chat history as `.txt` files
- 📚 Session-based memory for better multi-turn conversations

---

## 🚀 Live Demo

> 🔗 **[Click here to try it online](https://college-chatbox-vfpnvcksnwok43ka6qcvhh.streamlit.app/)**  
> *(No setup needed — runs directly in your browser)*

---

## 💡 Example Questions

- “What are the admission criteria for B.Tech at GGSIPU?”
- “How can I contact the IPU admission office?”
- “When will the counselling process start?”
- “What is the fee structure for MBA in GGSIPU?”
- “Where can I find the academic calendar?”

---

## 🧑‍💻 Run Locally

### 🔧 Installation

```bash
git clone https://github.com/yadavhitesh380/college-chatbot.git
cd college-chatbot
pip install -r requirements.txt
```

### 🔐 Set Gemini API Key

Create a `.streamlit/secrets.toml` file and add:

```toml
[default]
gemini_api_key = "YOUR_GOOGLE_GEMINI_API_KEY"
```

---

### ▶ Launch App

```bash
streamlit run main.py
```

Then open: [http://localhost:8501](http://localhost:8501)

---

## 🛠 Built With

* [Streamlit](https://streamlit.io)
* [Google Gemini API](https://developers.generativeai.google/)
* [Python](https://www.python.org/)
---

## 📁 Folder Structure

```
📦 college-chatbot/
├── main.py                      # Main Streamlit chatbot application
├── requirements.txt             # Python dependencies
├── .streamlit/
│   └── secrets.toml             # Secure API key storage
├── chat_logs/                   # (Optional) Directory for saving chat sessions
└── README.md                    # Project documentation
```

---

## 🔐 Notes

- The chatbot is restricted to only answer questions about GGSIPU.
- Chat logs are session-based and downloadable as text files.
- Your Gemini API key is sensitive — never share it publicly.

---

## 📜 License

This project is licensed under the MIT License.  
See the [LICENSE](LICENSE) file for full terms.

---

## 👨‍💻 Author

Made with ❤️ by **Hitesh Yadav**  
🌐 [GitHub](https://github.com/yadavhitesh380)

---

> If you found this helpful, ⭐ star the repo and share it!
