from langchain_community.document_loaders import YoutubeLoader

def extract_transcript(link: str) -> str:
    loader = YoutubeLoader.from_youtube_url(link)
    docs = loader.load()
    return docs[0].page_content