import streamlit as st

# Page settings
st.set_page_config(
    page_title="NOVEXA - Fake News Detector",
    page_icon="🔍"
)

# Website heading
st.title("🔍 NOVEXA")
st.subheader("Fake News Detector Using NLP")

st.write(
    "Check social media posts using "
    "Natural Language Processing."
)

# User input
news = st.text_area(
    "Paste your news or social media post here:"
)

# Analyse button
if st.button("Analyse News"):

    if news.strip():

        st.success("Your text has been received!")

        st.info(
            "Demo version: Machine learning "
            "model will be connected soon."
        )

    else:
        st.warning("Please enter some news first.")

# Footer
st.caption("NOVEXA | Fake News Detection Project")