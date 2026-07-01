
import streamlit as st
import requests

#Install all the libraries
#%pip install -qU langchain-groq

#!pip install -q langchain \
#                langchainhub==0.1.20 \
#                langchain-experimental==0.0.62\
#                langchain_huggingface\
#                langchain-groq

#from google.colab import userdata
#from langchain_groq import ChatGroq  # Import Groq LLM

# Get the API key from Colab secrets
#groq_api_key = userdata.get('GROQ_API_KEY') #Complete the code by calling the API key

from langchain_huggingface import HuggingFacePipeline
from transformers import pipeline




#st.title("🤖 Secure Hugging Face Chatbot")

# 1. Safely retrieve the token using st.secrets
# Falls back to os.environ if deployed directly on Hugging Face Spaces
#try:
#    st_hf_token = st.text_input("st_hf_token:")
#    st_hf_token = st.secrets.st_hf_token
#except KeyError:
#    import os
#    st_hf_token = os.getenv("myhfsecret_SumanKomarlaAdinarayana_AITPA9662R100368427028EcoSystemAutomationOfBusinessInfoV1")

st_hf_token = st.secrets.st_hf_token
st.write(st_hf_token)

#if not st_hf_token:
#    st.error("Please configure your st_hf_token secret.")
#    st.stop()

# 2. Initialize the Hugging Face Inference Client
# You can swap this out for other open-source chat models
#MODEL_ID = "meta-llama/Llama-3-8B-Instruct"
#client = InferenceClient(api_key=st_hf_token)




# 2. Setup Streamlit UI components
#user_input = st.text_input("Ask something:")

#if user_input:
#    with st.spinner("Generating..."):
#        # Invoke your model through LangChain
#        response = llm.invoke(user_input)
#        st.write(response)



st.title("Welcome! \"India International Market And Business Information\"")
st.page_link("https://github.com/suman-komarla-adinarayana-groups/SumanKomarlaAdinarayana-AITPA9662R-100368427028-EcoSystemAutomationOfBusinessInfo-V1", label="https://github.com/suman-komarla-adinarayana-groups", icon="🌎")
st.header("Thanks for choosing SUMAN KOMARLA ADINARAYANA Business Analysis And Information Consultancy")
st.subheader("Market SECTOR Business Analysis System")
st.text("Step 0 Of 7")
st.markdown("Step 0 - Raw Dataset Preparation")
st.write("Chatbot Output")

#Start of Chatbot GUI

st.markdown("LangChain + Streamlit App")

# --- SIDEBAR ARRANGEMENT ---
with st.sidebar:
    st.title("🤖 Bot Settings")

    # pip install litellm
    import litellm

    def get_all_provider_models():
        # Returns a dynamic list of all models supported by litellm
        return litellm.model_list

#    st.write(get_all_provider_models())
    get_all_provider_models_list = get_all_provider_models()


    # Secure field for Hugging Face Token (Get it from: hf.co/settings/tokens)
    hf_token_sidebar = st.text_input("Hugging Face API Token", type="password", help="Insert your HF Read Access Token.")

    # Dropdown choice for the Hugging Face model endpoint
    model_choice = st.selectbox(
        "Choose LLM Model",
        get_all_provider_models_list
    )












# Custom system instructions to shape the bot's behavior
system_prompt = st.text_area(
    "System Prompt",
    value="You are a helpful, brief, and friendly AI assistant."
  )

# Reset button to wipe out session memory
if st.button("🧹 Clear Conversation History"):
    st.session_state.messages = []
    st.rerun()





# 1. Initialize a Hugging Face pipeline locally or via API
@st.cache_resource # Caches the model so it doesn't reload on every click
def load_model():
    # Example using a small text generation model
    hf_pipe = pipeline("text-generation", model="gpt2", max_new_tokens=50)
#    hf_pipe = pipeline("text-generation", model="meta-llama/llama-4-scout-17b-16e-instruct", max_new_tokens=50)
    return HuggingFacePipeline(pipeline=hf_pipe)

llm = load_model()


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
    if user_ai_input.strip() == "":
        st.warning("Please enter some text first!")
    else:
        with st.spinner("Processing text with Hugging Face..."):
            # Run model inference
            response = llm.invoke(user_ai_input)
            #print("\n\n\n","[",i+1,"]", "iteration output \n\n\n",response)
            st.write(f"ChatwithAI Output: **{response}**")
            st.success("Success!")

st.write("Chatbot Output")

st.text("Step 1 Of 7")

st.markdown("Step 1 - Dataset Preparation")

# Create the popover container
with st.popover("Open Filter Options"):
    st.markdown("### Filter Settings")
    status = st.selectbox("Select Status", ["NSE", "BSE","International Stock Exchanges List","Forex","World Trade Data", "Others"])
    date_range = st.date_input("Choose Date Range")

    # Action inside popover
    submitted = st.button("Apply Filters")

if submitted:
    st.write(f"Filters applied: {status} for dates {date_range}")





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
