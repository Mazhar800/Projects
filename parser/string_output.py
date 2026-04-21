from langchain_huggingface import HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="google/flan-t5-base",
    task="text-generation"
)

print(llm.invoke("What is a black hole?"))
