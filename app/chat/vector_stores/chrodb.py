import os
from langchain.vectorstores import Chroma
from app.chat.embeddings.openai import embeddings
from dotenv import load_dotenv

load_dotenv()

# Initialize Chroma vector store
vector_store = Chroma(
    collection_name="collection",  # Name of the collection
    embedding_function=embeddings,    # Embedding function (e.g., OpenAI embeddings)
    persist_directory=os.getenv("CHROMA_PERSIST_DIR")  # Directory to persist data
)


def build_retriever(chat_args, k):
    search_kwargs = {
        "filter": {"pdf_id": chat_args.pdf_id},
        "k" : k
    }
    return vector_store.as_retriever(
        search_kwargs=search_kwargs
    )
