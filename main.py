import streamlit as st
import google.generativeai as genai
import datetime

# --- Streamlit Page Settings ---
st.set_page_config(page_title="DSEU Helpdesk Chatbot", layout="centered")

# --- Configure Gemini ---
try:
    genai.configure(api_key=st.secrets['gemini_api_key'])
except KeyError:
    st.error("Gemini API key not found. Set it in .streamlit/secrets.toml as 'gemini_api_key'.")
    st.stop()

st.title("🎓 DSEU College Helpdesk AI Chatbot")

# --- Session State Initialization ---
if 'messages' not in st.session_state:
    st.session_state.messages = [
        {
            "role": "user",
            "content": "You are a helpful assistant for DSEU (Delhi Skill and Entrepreneurship University). "
                       "Answer queries only about DSEU including admissions, courses, faculty, fees, campuses, "
                       "events, contact info, results, and placement details. Do not talk about any other university."
        }
    ]

if 'chat_logs' not in st.session_state:
    st.session_state.chat_logs = []

# --- Sidebar ---
with st.sidebar:
    st.markdown("### 💡 Example Questions")
    st.markdown("- What is the BCA course fee at DSEU?")
    st.markdown("- Where is the Dwarka campus located?")
    st.markdown("- How can I apply for DSEU admission?")
    st.markdown("- What are the skill-based programs at DSEU?")
    st.markdown("- Who is the VC of DSEU?")
    if st.button("🧹 Clear Chat"):
        st.session_state.messages = [st.session_state.messages[0]]
        st.session_state.chat_logs = []
        st.rerun()

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
            try:
                # Rebuild API history correctly
                api_history = [{"role": "user", "parts": [{"text": st.session_state.messages[0]['content']}]}]
                for msg in st.session_state.messages[1:]:
                    role = 'user' if msg['role'] == 'user' else 'model'
                    api_history.append({"role": role, "parts": [{"text": msg['content']}]})

                # Call Gemini
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

        # Download button
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
