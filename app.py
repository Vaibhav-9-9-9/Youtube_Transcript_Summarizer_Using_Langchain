import streamlit as st

from summarizers import smart_summarizer
from web_generator import web_chain
from utils import is_valid_youtube_url
from file_handler import extract_code,save_files,create_zip

st.set_page_config(page_title="YouTube → Article Generator", layout="wide")

st.title("🎥 YouTube to Article & Website Generator")

user_input = st.text_input("Enter YouTube URL")

if st.button("🚀 Generate Article & Website"):

    if not user_input:
        st.warning("⚠️ Please enter a YouTube URL")

    elif not is_valid_youtube_url(user_input):
        st.error("❌ Invalid YouTube URL")

    else:
        with st.spinner("⏳ Processing video..."):

            try:
                article = smart_summarizer.invoke(user_input)

                website = web_chain.invoke({
                    "article_content": article
                })

                html, css, js = extract_code(website)

                save_files(html, css, js)
                create_zip()

                st.success("✅ Website Generated Successfully!")

                st.download_button(
                    label="📥 Download Website ZIP",
                    data=open("website.zip", "rb"),
                    file_name="website.zip",
                    mime="application/zip"
                )

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")