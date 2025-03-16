import streamlit as st
from twilio.rest import Client
import re

# Twilio API Credentials (Replace with your own)
TWILIO_ACCOUNT_SID = "ACa0ccde15bfd28a78bc4828929f55db51"
TWILIO_AUTH_TOKEN = "4739376322e3871f9439a8b26fefc37f"
TWILIO_PHONE_NUMBER = "+12524270686"
YOUR_PHONE_NUMBER = "+919421293631"

def send_sms(name, email, phone, message) :
    try :
        client = Client ( TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN )

        sms_body = (
            f"🚜 New Message from Farmer:\n"
            f"👤 Name: {name}\n"
            f"📧 Email: {email}\n"
            f"📞 Phone: {phone}\n"
            f"🌾 Message: {message}"
        )

        client.messages.create (
            body=sms_body,
            from_=TWILIO_PHONE_NUMBER,
            to=YOUR_PHONE_NUMBER
        )
        st.success ( "Message sent successfully!" )
    except Exception as e :
        st.error ( f"Error sending SMS: {e}" )

def Contact(lang_code):
    # Language translations
    translations = {
        "en" : {
            "title" : "📞 Contact Us",
            "description" : "For any inquiries, reach out to us through the following contact details.",
            "name" : "Your Name",
            "email" : "Your Email",
            "address" : "Your Address",
            "phone" : "Your Phone",
            "message" : "Your Message",
            "send" : "SEND MESSAGE",
            "error" : "Please fill out all required fields (Name, Email, and Message).",
            "success" : "Your message has been sent successfully!",
            "experts" : "🌟 Meet Our Experts",
            "expert_info" : "Our team of experts specializes in tomato leaf disease detection. Feel free to reach out to them directly.",
            "urgent" : "For urgent inquiries, contact us through the following channels:",
            "phone_label" : "Phone",
            "email_label" : "Email",
            "website_label" : "Website",
            "instagram_label" : "Instagram",
            "twitter_label" : "Twitter",
            "select_language" : "Select Language"
        },
        "hi" : {
            "title" : "📞 हमसे संपर्क करें",
            "description" : "किसी भी पूछताछ के लिए, कृपया निम्नलिखित संपर्क विवरणों के माध्यम से हमसे संपर्क करें।",
            "name" : "आपका नाम",
            "email" : "आपका ईमेल",
            "address" : "आपका पता",
            "phone" : "आपका फ़ोन",
            "message" : "आपका संदेश",
            "send" : "संदेश भेजें",
            "error" : "कृपया सभी आवश्यक फ़ील्ड भरें (नाम, ईमेल और संदेश)।",
            "success" : "आपका संदेश सफलतापूर्वक भेज दिया गया है!",
            "experts" : "🌟 हमारे विशेषज्ञ",
            "expert_info" : "हमारी टीम टमाटर पत्ती रोग पहचान में विशेषज्ञ है। आप सीधे उनसे संपर्क कर सकते हैं।",
            "urgent" : "त्वरित पूछताछ के लिए, निम्नलिखित चैनलों के माध्यम से हमसे संपर्क करें:",
            "phone_label" : "फ़ोन",
            "email_label" : "ईमेल",
            "website_label" : "वेबसाइट",
            "instagram_label" : "इंस्टाग्राम",
            "twitter_label" : "ट्विटर",
            "select_language" : "भाषा चुनें"
        },
        "mr" : {
            "title" : "📞 आमच्याशी संपर्क साधा",
            "description" : "कोणत्याही चौकशीसाठी, खालील संपर्क तपशीलांद्वारे आमच्याशी संपर्क साधा.",
            "name" : "तुमचे नाव",
            "email" : "तुमचा ईमेल",
            "address" : "तुमचा पत्ता",
            "phone" : "तुमचा फोन",
            "message" : "तुमचा संदेश",
            "send" : "संदेश पाठवा",
            "error" : "कृपया सर्व आवश्यक फील्ड भरा (नाव, ईमेल आणि संदेश).",
            "success" : "तुमचा संदेश यशस्वीरीत्या पाठवला गेला आहे!",
            "experts" : "🌟 आमचे तज्ञ",
            "expert_info" : "आमची टीम टोमॅटो पानांच्या रोगांचे निदान करण्यात तज्ज्ञ आहे. तुम्ही त्यांच्याशी थेट संपर्क साधू शकता.",
            "urgent" : "तातडीच्या चौकशीसाठी, खालील चॅनेलद्वारे आमच्याशी संपर्क साधा:",
            "phone_label" : "फोन",
            "email_label" : "ईमेल",
            "website_label" : "वेबसाइट",
            "instagram_label" : "इंस्टाग्राम",
            "twitter_label" : "ट्विटर",
            "select_language" : "भाषा निवडा"
        }
    }

    lang = translations[lang_code]

    st.title(lang["title"])
    st.write(lang["description"])

    # Initialize session state for the form fields
    if "form_data" not in st.session_state :
        st.session_state.form_data = {
            "name" : "",
            "email" : "",
            "address" : "",
            "phone" : "",
            "message" : ""
        }

    # Contact Form Inputs
    col1, col2, col3 = st.columns ( 3 )

    with col1 :
        st.session_state.form_data["name"] = st.text_input (
            "**Your Name**",
            placeholder="Enter your name",
            value=st.session_state.form_data["name"]
        )
        st.session_state.form_data["email"] = st.text_input (
            "**Your Email**",
            placeholder="Enter your email",
            value=st.session_state.form_data["email"]
        )

    with col2 :
        st.session_state.form_data["address"] = st.text_input (
            "**Your Address**",
            placeholder="Enter your address",
            value=st.session_state.form_data["address"]
        )
        st.session_state.form_data["phone"] = st.text_input (
            "**Your Phone**",
            placeholder="Enter your phone number",
            value=st.session_state.form_data["phone"]
        )

    with col3 :
        st.session_state.form_data["message"] = st.text_area (
            "**Your Message**",
            placeholder="Type your message here",
            value=st.session_state.form_data["message"]
        )

        # Submit Button
    if st.button ( "SEND MESSAGE" ) :
            # Validation for mandatory fields
        if not st.session_state.form_data["name"] or not st.session_state.form_data["phone"] or not st.session_state.form_data["message"] :
                st.error ( "Please fill out all required fields (Name, Phone, and Message)." )
        else :
            send_sms ( st.session_state.form_data["name"], st.session_state.form_data["email"],st.session_state.form_data["phone"], st.session_state.form_data["message"] )

            st.session_state.form_data = {
                "name" : "",
                "email" : "",
                "address" : "",
                "phone" : "",
                "message" : ""
            }


    # Expertise Team Section
    st.markdown("---")
    st.subheader(lang["experts"])
    st.write(lang["expert_info"])

    experts = [
        {"name": "Dr. Amit Kumar", "image": "image/team-1.jpg", "phone": "+91 98765 43210"},
        {"name": "Dr. Neha Sharma", "image": "image/team-5.jpg", "phone": "+91 98234 56789"},
        {"name": "Dr. Rajesh Verma", "image": "image/team-4.jpg", "phone": "+91 98712 34567"}
    ]

    col1, col2, col3 = st.columns(3)
    for idx, expert in enumerate(experts):
        with [col1, col2, col3][idx]:
            st.image(expert["image"], width=200)
            st.write(f"**{expert['name']}**")
            st.write(f"📞 {expert['phone']}")

    # Additional Information Section
    st.markdown("---")
    st.write(lang["urgent"])
    st.write(f"📞 **{lang['phone_label']}:** +1 (800) 123-4567")
    st.write(f"📧 **{lang['email_label']}:** support@tomatosystem.com")
    st.write(f"🌐 **{lang['website_label']}:** [www.tomatosystem.com](http://www.tomatosystem.com)")
    st.write(f"📱 **{lang['instagram_label']}:** [@tomatosystem](https://www.instagram.com/tomatosystem)")
    st.write(f"🐦 **{lang['twitter_label']}:** [@tomatosystem](https://www.twitter.com/tomatosystem)")
    st.markdown("---")

