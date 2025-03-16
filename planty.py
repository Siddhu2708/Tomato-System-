import json
import os
import streamlit as st
from groq import Groq

def Planty(lang_code):
    # Define translations
    translations = {
        "en" : {
            "title" : "🪴 Planty AI",
            "clear_chat" : "🗑️ Clear Chat",
            "select_option":"🗑️️ Select an option",
            "ask_prompt" : "Ask Planty...",
            "assistant_system_message" : "You are a helpful assistant.",
            "error_message" : "Please check your internet connection.",
            "chat_cleared" : "✅ Chat history cleared!"
        },
        "hi" : {
            "title" : "🪴 प्लांटी एआई",
            "clear_chat" : "🗑️ चैट साफ़ करें",
            "select_option" : "🗑️ एक विकल्प चुनें",
            "ask_prompt" : "प्लांटी से पूछें...",
            "assistant_system_message" : "आप एक सहायक सहायक हैं।",
            "error_message" : "कृपया अपना इंटरनेट कनेक्शन जांचें।",
            "chat_cleared" : "✅ चैट इतिहास साफ किया गया!"

        },
        "mr" : {
            "title" : "🪴 प्लांटी एआय",
            "clear_chat" : "🗑️ चॅट साफ करा",
            "select_option" : "🗑️ एक पर्याय निवडा",
            "ask_prompt" : "प्लांटीला विचारा...",
            "assistant_system_message" : "तुम्ही एक मदतनीस सहाय्यक आहात.",
            "error_message" : "कृपया तुमचे इंटरनेट कनेक्शन तपासा.",
            "chat_cleared" : "✅ चॅट इतिहास साफ करण्यात आला!"

        }
    }

    t = translations[lang_code]

    try:
        # Load API Key
        working_dir = os.path.dirname(os.path.abspath(__file__))
        config_data = json.load(open(f"{working_dir}/config.json"))
        GROQ_API_KEY = config_data["GROQ_API_KEY"]
        os.environ["GROQ_API_KEY"] = GROQ_API_KEY

        client = Groq()

        # Initialize chat history
        if "chat_history" not in st.session_state:
            st.session_state.chat_history = []

        # Set the Streamlit page title
        st.title(t["title"])

        if st.button ( t["clear_chat"] ) :
            st.session_state.chat_history = []

        # Display chat history
        for message in st.session_state.chat_history:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

        # Input field for user's message:
        user_prompt = st.chat_input(t["ask_prompt"])

        if user_prompt:
            st.chat_message("user").markdown(user_prompt)
            st.session_state.chat_history.append({"role": "user", "content": user_prompt})

            # Send user's message to the LLM and get a response
            messages = [
                {"role": "system", "content": "You are an expert in tomato diseases and treatment solutions"},
                *st.session_state.chat_history
            ]

            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages
            )

            assistant_response = response.choices[0].message.content
            st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

            # Display the Planty response
            with st.chat_message("assistant"):
                st.markdown(assistant_response)

    except Exception as e:
        st.error(f"{translations['en']['error_message']}: {e}")


