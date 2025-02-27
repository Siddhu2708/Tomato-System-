import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st

def send_email(form_data):
    # Your Gmail account and App Password
    sender_email = form_data["email"]
    app_password = "vgrg ngxt txnr qxni"

    # Receiver email
    receiver_email = "siddharthgaykhe08@gmail.com"

    # Set up the MIME message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = f"Contact Form Message from {form_data['name']}"

    # Email body content
    body = f"""
    You have received a new message from your contact form:

    Name: {form_data['name']}
    Email: {form_data['email']}
    Address: {form_data['address']}
    Phone: {form_data['phone']}

    Message:
    {form_data['message']}
    """

    message.attach(MIMEText(body, "plain"))

    # Connect to Gmail's SMTP server and send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Start TLS encryption
            server.login(sender_email, app_password)  # Login with App Password
            server.sendmail(sender_email, receiver_email, message.as_string())
            st.success("Your message has been sent successfully!")
    except Exception as e:
        st.error(f"Error sending email: {e}")

def Contact():
    # Title for the Contact Us page
    st.title("📞 Contact Us")
    st.write("For any inquiries, reach out to us through the following contact details.")


    # Initialize session state for the form fields
    if "form_data" not in st.session_state:
        st.session_state.form_data = {
            "name": "",
            "email": "",
            "address": "",
            "phone": "",
            "message": ""
        }

    # Contact Form Inputs
    col1, col2, col3 = st.columns(3)

    with col1:
        st.session_state.form_data["name"] = st.text_input(
            "**Your Name**",
            placeholder="Enter your name",
            value=st.session_state.form_data["name"]
        )
        st.session_state.form_data["email"] = st.text_input(
            "**Your Email**",
            placeholder="Enter your email",
            value=st.session_state.form_data["email"]
        )

    with col2:
        st.session_state.form_data["address"] = st.text_input(
            "**Your Address**",
            placeholder="Enter your address",
            value=st.session_state.form_data["address"]
        )
        st.session_state.form_data["phone"] = st.text_input(
            "**Your Phone**",
            placeholder="Enter your phone number",
            value=st.session_state.form_data["phone"]
        )

    with col3:
        st.session_state.form_data["message"] = st.text_area(
            "**Your Message**",
            placeholder="Type your message here",
            value=st.session_state.form_data["message"]
        )

    # Submit Button
    if st.button("SEND MESSAGE"):
        # Validation for mandatory fields
        if not st.session_state.form_data["name"] or not st.session_state.form_data["email"] or not \
        st.session_state.form_data["message"]:
            st.error("Please fill out all required fields (Name, Email, and Message).")
        else:
            # Send the email
            send_email(st.session_state.form_data)

            # Reset all fields
            st.session_state.form_data = {
                "name": "",
                "email": "",
                "address": "",
                "phone": "",
                "message": ""
            }

# Additional Information Section
    st.markdown("---")
    st.write("For urgent inquiries, you can reach us through the following channels:")
    st.write("📞 **Phone:** +1 (800) 123-4567")
    st.write("📧 **Email:** support@tomatosystem.com")
    st.write("🌐 **Website:** [www.tomatosystem.com](http://www.tomatosystem.com)")
    st.write("📱 **Instagram:** [@tomatosystem](https://www.instagram.com/tomatosystem)")
    st.write("🐦 **Twitter:** [@tomatosystem](https://www.twitter.com/tomatosystem)")
    st.markdown("---")

# Run the contact function when the script is executed
if __name__ == "__main__":
    Contact()
