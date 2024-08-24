from transformers import pipeline

from langchain_huggingface import HuggingFaceEndpoint
import os
# Hugging Face API Token
HUGGINGFACEHUB_API_TOKEN = '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'

# LLM Configuration
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, max_length=128, temperature=0.7, token=HUGGINGFACEHUB_API_TOKEN)


def generate_response_mistral(query):
    ans = llm.invoke(query)
    return ans

# # # Get the LLM Response
# # ans = llm.invoke(query)
# print("LLM Output:", ans)
# Create Document to Insert in MongoDB





