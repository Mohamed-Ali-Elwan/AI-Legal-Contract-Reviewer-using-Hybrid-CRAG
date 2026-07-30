import streamlit as st

from service import ReviewService


st.set_page_config(
    page_title="AI Legal Contract Reviewer",
    page_icon="⚖️",
    layout="wide"
)

# ===============================
# Custom Theme
# ===============================

st.markdown("""
<style>

.stApp{
    background-color:#F5F1E8;
}

h1,h2,h3{
    color:#5C4033;
}

.stButton>button{
    background-color:#B8860B;
    color:white;
    border-radius:10px;
    font-size:18px;
    width:100%;
}

.stButton>button:hover{
    background-color:#8B6508;
}

div[data-testid="stFileUploader"]{
    background-color:#FFF8DC;
    border:2px solid #B8860B;
    padding:20px;
    border-radius:10px;
}

.result-box{
    background:#FFF8DC;
    padding:20px;
    border-radius:15px;
    border:2px solid #B8860B;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# Title
# ===============================

st.title("⚖️ AI Legal Contract Reviewer")

st.write(
    "Upload a legal contract and let AI analyse risks according to Egyptian law."
)

# ===============================
# Sidebar
# ===============================

st.sidebar.header("Settings")

kaggle_endpoint_url = st.sidebar.text_input(
    "Kaggle ngrok URL",
    placeholder="https://xxxx.ngrok-free.app",
    help="Run the Kaggle notebook, then paste the ngrok URL printed there."
)

tavily_api_key = st.sidebar.text_input(
    "Tavily API Key",
    type="password",
    help="Used for the web-search fallback when the local legal corpus doesn't cover a clause."
)
kaggle_api_key = st.sidebar.text_input(
    "Kaggle API Key",
    type="password",
    value="secret123",
    help="Must match the API_KEY inside the Kaggle notebook."
)
# ===============================
# Input method
# ===============================

input_method = st.radio(
    "How would you like to provide the contract?",
    ["Upload PDF", "Paste Text"],
    horizontal=True
)

uploaded_file = None
pasted_text = ""

if input_method == "Upload PDF":

    uploaded_file = st.file_uploader(
        "Upload Contract",
        type=["pdf"]
    )

else:

    pasted_text = st.text_area(
        "Paste Contract Text",
        height=300,
        placeholder="Paste the full contract text here..."
    )

# ===============================
# Analyse
# ===============================

if st.button("Analyse Contract"):

    if input_method == "Upload PDF" and uploaded_file is None:

        st.warning("Please upload a PDF.")

    elif input_method == "Paste Text" and not pasted_text.strip():

        st.warning("Please paste the contract text.")

    elif kaggle_endpoint_url == "":

        st.warning("Please enter your Kaggle ngrok URL.")
    elif kaggle_api_key == "":
        st.warning("Please enter the Kaggle API Key.")    

    elif tavily_api_key == "":

        st.warning("Please enter your Tavily API Key.")

    else:

        try:
            service = ReviewService(
                tavily_api_key=tavily_api_key,
                kaggle_endpoint_url=kaggle_endpoint_url,
                kaggle_api_key=kaggle_api_key
                )
        except ConnectionError as e:
            st.error(str(e))
            st.stop()

        with st.spinner("Reviewing Contract..."):

            if input_method == "Upload PDF":
                result = service.review_pdf(uploaded_file)
            else:
                result = service.review(pasted_text)

        st.success("Analysis Complete")

        st.markdown(
            f"""
            <div class="result-box">

            <h3>Overall Risk</h3>

            {result.overall_risk}

            </div>
            """,
            unsafe_allow_html=True
        )

        st.markdown("## Contract Summary")

        st.write(result.summary)

        st.markdown("## Detected Issues")

        for issue in result.issues:

            st.expander(issue.clause).write(
                f"""
Risk Level:

{issue.risk_level}

Explanation:

{issue.explanation}

Recommendation:

{issue.recommendation}
"""
            )