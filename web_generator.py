from langchain_core.output_parsers import StrOutputParser
from prompts import web_dev_template
from llm import llm

web_chain = web_dev_template | llm | StrOutputParser()