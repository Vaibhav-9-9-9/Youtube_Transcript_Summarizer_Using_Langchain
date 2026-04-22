from langchain_core.runnables import RunnablePassthrough, RunnableLambda, RunnableBranch
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent
from langchain.agents.middleware import SummarizationMiddleware

from transcript import extract_transcript
from prompts import summarizer_prompt,web_dev_template
from llm import llm


# Base summarizer
base_summarizer = (
    RunnablePassthrough()
    | RunnableLambda(extract_transcript)
    | summarizer_prompt
    | llm
    | StrOutputParser()
)

# Agent (kept exactly same)
agent = create_agent(
    model=llm,
    tools=[],
    system_prompt='You are an Professional Article Writer specializing in writing articles for Medium, LinkedIn, and tech blogs.',
    middleware=[
        SummarizationMiddleware(
            model=llm,
            trigger=("tokens", 1000),
            keep=("tokens", 200),
        ),
    ],
)

def clean_output(output):
    return output.content

# Long summarizer
long_summarizer = (
    RunnablePassthrough()
    | RunnableLambda(extract_transcript)
    | summarizer_prompt
    | llm
    | RunnableLambda(clean_output)
)

# Condition
def estimate_transcript_length(link: str) -> bool:
    transcript = extract_transcript(link)
    return len(transcript) >= 1000

# Smart router
smart_summarizer = RunnableBranch(
    (RunnableLambda(estimate_transcript_length), long_summarizer),
    base_summarizer)