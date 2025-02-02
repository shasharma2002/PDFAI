import os
from langfuse.client import Langfuse
from dotenv import load_dotenv

load_dotenv()

langfuse=Langfuse(
    os.environ["LANGFUSE_PUBLIC_KEY"],
    os.environ["LANGFUSE_SECRET_KEY"]
)