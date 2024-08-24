from transformers import pipeline

from langchain_huggingface import HuggingFaceEndpoint
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

HUGGINGFACEHUB_API_TOKEN = os.getenv('HUGGINGFACEHUB_API_TOKEN')
# Hugging Face API Token
# HUGGINGFACEHUB_API_TOKEN = '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'

# LLM Configuration
repo_id = "meta-llama/Meta-Llama-3-8B-Instruct"
llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.7, token=HUGGINGFACEHUB_API_TOKEN)


def generate_response_llama(query):
    ans = llm.invoke(query)
    return ans

# # # Get the LLM Response
# # ans = llm.invoke(query)
# print("LLM Output:", ans)
# Create Document to Insert in MongoDB





