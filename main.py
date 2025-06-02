import streamlit as st
import google.generativeai as genai
import json
import datetime

# --- Streamlit Page Settings ---
st.set_page_config(page_title="GGSIPU Helpdesk Chatbot", layout="centered")

# --- Configure Gemini ---
try:
    genai.configure(api_key=st.secrets['gemini_api_key'])
except KeyError:
    st.error("Gemini API key not found. Set it in .streamlit/secrets.toml as 'gemini_api_key'.")
    st.stop()

st.title("🎓 GGSIPU College Helpdesk AI Chatbot")

# --- Session State Initialization ---
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant for GGSIPU (Guru Gobind Singh Indraprastha University). Answer queries only about GGSIPU including admissions, courses, faculty, fees, events, contact info, etc. Do not talk about any other university."}
    ]

if 'chat_logs' not in st.session_state:
    st.session_state.chat_logs = []

# --- Sidebar ---
with st.sidebar:
    st.markdown("### 💡 Example Questions")
    st.markdown("- What is the B.Tech CSE fee structure?")
    st.markdown("- Who is the head of ECE department?")
    st.markdown("- What are the hostel facilities?")
    st.markdown("- How do I get my semester results?")
    st.markdown("- What is the CET code for BCA?")

# --- Display Chat Messages ---
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg['role']):
        st.markdown(msg['content'])

# --- Handle User Query ---
if user_query := st.chat_input("Ask your question here..."):
    st.chat_message("user").markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            answer = ""
            try:
                # Build Gemini conversation history
                api_history = [{"role": "user", "parts": [{"text": st.session_state.messages[0]['content']}]}]
                for msg in st.session_state.messages[1:]:
                    if not msg['content']: continue
                    role = 'user' if msg['role'] == 'user' else 'model'
                    if api_history and api_history[-1]['role'] == role:
                        api_history[-1]['parts'].append({"text": msg['content']})
                    else:
                        api_history.append({"role": role, "parts": [{"text": msg['content']}]} )
                
                model = genai.GenerativeModel("gemini-2.0-flash")
                response = model.generate_content(api_history)
                answer = response.text
            except Exception as e:
                answer = f"⚠️ Error: {e}"

            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})
    st.session_state.chat_logs.append({
        "user_query": user_query,
        "assistant_response": answer,
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

# --- Admin Dashboard ---
st.markdown("---")
with st.expander("📊 Admin View (Simulated Dashboard)"):
    st.markdown("This section shows recent chat activity.")
    
    st.subheader("Recent Chat Logs")
    if st.session_state.chat_logs:
        for i, log in enumerate(reversed(st.session_state.chat_logs)):
            st.markdown(f"**Query {len(st.session_state.chat_logs) - i}** (_{log['timestamp']}_):")
            st.markdown(f"**User**: {log['user_query']}")
            st.markdown(f"**Assistant**: {log['assistant_response']}")
            st.markdown("---")

        # Prepare chat logs as a TXT string
        chat_text = ""
        for i, log in enumerate(st.session_state.chat_logs, 1):
            chat_text += f"Query {i} ({log['timestamp']}):\nUser: {log['user_query']}\nAssistant: {log['assistant_response']}\n\n"

        st.download_button(
            label="⬇️ Download Logs as TXT",
            data=chat_text,
            file_name="chat_logs.txt",
            mime="text/plain"
        )
    else:
        st.info("No chat logs yet. Start a conversation to see logs.")
