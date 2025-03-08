import os
import json
import tempfile
import numpy as np
import tensorflow as tf
from PIL import Image
from fpdf import FPDF
import streamlit as st
from groq import Groq
import io

def Home():
    # Home Section
    st.title("🌱 Welcome to Tomato System!")
    st.subheader("Your ultimate companion for tomato planting, care, and disease management.")
    st.write("""
        Use the Tomato System to:
        - Detect and diagnose diseases in tomato plants.
        - Get expert advice and treatment options with Planty AI.
        - Shop for high-quality fertilizers, pesticides, and seeds.
    """)

    st.markdown("---")
    st.header("🌟 Special Offer for Tomato Lovers!")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Buy Premium Tomato Seeds Now!")
        st.write("""
            - High yield and disease resistance.
            - Suitable for all climates.
            - Special 20% discount for a limited time!
        """)
        st.write("""
            🌟 Why choose our seeds?
            - Tested and trusted by farmers worldwide.
            - Supports sustainable and organic farming practices.
            - Guaranteed freshness and germination rates.
        """)
        st.write("### 👉 Visit Our Shop")
        # if st.button("👉 Visit Our Shop"):
        #     st.write("Redirecting to shop...")
        #     shop_url = "http://localhost:8501/shop"

    with col2:
        ad_image = "./image/tomato_seeds.png"  # Replace with your ad image path
        st.image(ad_image, caption="Premium Tomato Seeds", use_container_width=True)

    st.markdown("---")

    # Load the pre-trained model
    model = tf.keras.models.load_model('tomato_disease_model.h5')

    # Classes for diseases
    classes = ['Bacterial_spot', 'Early_blight', 'Late_blight', 'Leaf_Mold', 'No_tomato_leaf', 'Septoria_leaf_spot',
               'Spider_mites Two-spotted_spider_mite', 'Target_Spot', 'Tomato_Yellow_Leaf_Curl_Virus',
               'Tomato_mosaic_virus', 'Healthy', 'powdery_mildew']

    # Function to preprocess image
    def preprocess_image(img) :
        img = img.resize ( (128, 128) )  # Assuming the model expects 224x224 images
        img_array = np.array ( img )
        img_array = np.expand_dims ( img_array, axis=0 )  # Add batch dimension
        img_array = img_array / 255.0  # Normalize pixel values
        return img_array

    st.title("Tomato Disease Diagnosis")
    st.write("Use this section to upload images of tomato leaves and get a diagnosis.")

    uploaded_file = st.file_uploader("Upload an image of the tomato leaf", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:

        st.image(uploaded_file, caption='Uploaded Image', width=400)

        image = Image.open ( uploaded_file )
        processed_image = preprocess_image(image)
        prediction = model.predict(processed_image)

        predicted_class_index = np.argmax(prediction, axis=1)[0]
        predicted_class = classes[predicted_class_index]
        confidence = np.max(prediction) * 100

        try:
            # Configure Groq API key
            working_dir = os.path.dirname(os.path.abspath(__file__))
            config_data = json.load(open(f"{working_dir}/config.json"))
            GROQ_API_KEY = config_data["GROQ_API_KEY"]
            os.environ["GROQ_API_KEY"] = GROQ_API_KEY

            client = Groq()

            # Query Groq
            messages = [
                {"role": "system", "content": "You are an expert in tomato diseases and treatment solutions."},
                {"role": "user", "content": f"Provide information, treatment solutions, and pesticide recommendations for {predicted_class} in tomatoes and only Bold the Main Topics."}
            ]
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages
            )
            solution_info = response.choices[0].message.content.strip()

            if predicted_class == "No_tomato_leaf" :
                st.write ( "### ❌ Invalid Image" )
                st.write ( "Please upload a valid image of a tomato leaf for diagnosis." )

            elif confidence < 80 :
                st.write ( "### ⚠️ Low Image Quality" )
                st.write ( "Please upload a clearer image for better diagnosis." )

            else :
                st.write ( "### ✅ Disease Detected: ", predicted_class )
                st.write ( f"Confidence: {confidence:.2f}%" )
                st.write ( "### Information and Solution:" )
                st.write ( "####", solution_info )

            # Generate PDF Report
            def generate_pdf(image, disease_name, solution_info):
                # Initialize PDF
                pdf = FPDF()
                pdf.add_page()

                # Title Section
                pdf.set_font("Arial", style="B", size=16)
                pdf.cell(200, 10, txt="Tomato Disease Diagnosis Report", ln=True, align="C")

                # Add Image
                pdf.ln ( 20 )
                pdf.image ( image, x=60, y=50, w=90 )

                # Disease Name Section
                pdf.ln(110)
                pdf.set_font("Arial", style='B', size=14)
                pdf.cell(200, 10, txt=f"Disease Name: {disease_name}", ln=True)

                # Solution and Treatment Section
                pdf.ln(10)
                pdf.set_font("Arial", size=12)
                pdf.multi_cell( 0, 10, txt=f"Solution and Treatment:\n{solution_info}" )

                # Return the generated PDF
                return pdf

            def save_pdf(image, disease_name, solution_info):
                # Convert the image to a temporary file
                temp_image_buffer = io.BytesIO()
                image.save(temp_image_buffer, format="PNG")
                temp_image_buffer.seek(0)

                # Save image to a temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_image_file:
                    temp_image_file.write(temp_image_buffer.read())
                    temp_image_path = temp_image_file.name

                # Generate the PDF
                pdf = generate_pdf(temp_image_path, disease_name, solution_info)

                # Save the PDF to a temporary file
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as pdf_temp_file:
                    pdf_path = pdf_temp_file.name
                    pdf.output(pdf_path)

                return pdf_path

            # Button to generate and download PDF
            if st.button("Generate PDF Report"):
                try:
                    pdf_path = save_pdf(image, predicted_class, solution_info)

                    # Provide download button for the PDF
                    with open(pdf_path, "rb") as pdf_file:
                        st.download_button(
                            label="📄 Download Diagnosis Report",
                            data=pdf_file,
                            file_name="tomato_diagnosis_report.pdf",
                            mime="application/pdf",
                        )
                except Exception as e:
                    st.error(f"Error generating the PDF report: {e}")

        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.write("Please upload an image for diagnosis.")
