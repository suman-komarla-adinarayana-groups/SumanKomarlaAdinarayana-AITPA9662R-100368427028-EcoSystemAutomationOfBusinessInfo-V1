
import streamlit as st
import requests

st.title("Welcome! \"India International Market And Business Information\"")
st.header("Thanks for choosing SUMAN KOMARLA ADINARAYANA Business Analysis And Information Consultancy")
st.subheader("Market SECTOR Business Analysis System")
st.text("Step 0 Of 7")
st.markdown("Step 0 - Raw Dataset Preparation")
st.write("Chatbot Output")

# 3. Handle Text Input
user_input = st.text_area("Your Input Text", placeholder="Type or paste your text here...")

if st.button("Generate Raw Data - ALGO by Suman Komarla Adinarayana"):
    if user_input.strip() == "":
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Processing text with Hugging Face..."):
            # Run model inference
            st.write(user_input)

# 3. Handle Text Input
user_ai_input = st.text_area("Your chat Text", placeholder="Type or paste your chat text here...")

if st.button("CHATwithAI built by SUMAN KOMARLA ADINARAYANA"):
    if user_input.strip() == "":
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Processing text with Hugging Face..."):
            # Run model inference
            st.write(f"ChatwithAI Output: **{user_ai_input}**")
            st.success("Success!")

st.text("Step 1 Of 7")
st.markdown("Step 1 - Dataset Preparation")
st.write("Chatbot Output")

# Input fields for product and store data
Sl_No = st.number_input("Sl_No", min_value=0.0, value=1000000.00)
LocationID	= st.selectbox("LocationID", ["Bangalore","Karnataka", "India", "International"])
#ProdTaken	= st.number_input("ProdTaken", min_value=0.0, value=1000000.00)
SectorID	= st.selectbox("SectorID", ["Auto","Bank","Cement","Chemicals","Financial Services","Financial Services 25/50","Financial Services Ex-Bank","FMCG","Healthcare","IT","Media","Metal","Pharma","Private","Bank","PSU","Bank","Realty","REITs & Realty","Consumer Durables","Oil and Gas","Healthcare","MidSmall Financial Services","MidSmall Healthcare","MidSmall IT & Telecom"])
OrganizationID	= st.number_input("OrganizationID", min_value=0.0, value=1000000.00)
MarketCapitalisation_INR_CR	= st.number_input("MarketCapitalisation_INR_CR", min_value=0.0, value=1000000.00)
FounderID = st.number_input("FounderID", min_value=0.0, value=1000000.00)
OrganizationLocationsID	= st.number_input("OrganizationLocationsID", min_value=0.0, value=1000000.00)
OrganizationWebsiteID	= st.number_input("OrganizationWebsiteID", min_value=0.0, value=1000000.00)
OriginCountry_ID	= st.number_input("OriginCountry_ID", min_value=0.0, value=1000000.00)
OrganizationWebsite_UNVERIFIED_ID = st.text_input("OrganizationWebsite_UNVERIFIED_ID", value="", max_chars=None)
OrganizationHeadQuartersPostalAddress_ID = st.text_input("OrganizationHeadQuartersPostalAddress_ID", value="", max_chars=None)
OrganizationContact_ID = st.text_input("OrganizationContact_ID", value="", max_chars=None)



product_data = {
    "Sl_No": Sl_No,
    "LocationID" : LocationID,
    "SectorID" : SectorID,
    "OrganizationID" : OrganizationID,
    "MarketCapitalisation_INR_CR" : MarketCapitalisation_INR_CR,
    "FounderID" : FounderID,
    "OrganizationLocationsID" : OrganizationLocationsID,
    "OrganizationWebsiteID" : OrganizationWebsiteID,
    "OriginCountry_ID" : OriginCountry_ID,
    "OrganizationWebsite_UNVERIFIED_ID" : OrganizationWebsite_UNVERIFIED_ID,
    "OrganizationHeadQuartersPostalAddress_ID" : OrganizationHeadQuartersPostalAddress_ID,
    "OrganizationContact_ID" : OrganizationContact_ID,

}



if st.button("Predict", type='primary'):
    response = requests.post("https://huggingface.co/spaces/suman-komarla-adinarayana-groups/SumanKAGreatLearningInfo-EducationStudyAssignment10-TourismPackagePredictionAPI/v1/predict", json=product_data)  # Replace <user_name> and <space_name>
    if response.status_code == 200:
        result = response.json()
        predicted_sales = result["Sales"]
        st.write(f"Predicted Tourism Package Total: ₹{predicted_sales:.2f}")
    else:
        st.error("Error in API request")
