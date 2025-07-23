from dotenv import load_dotenv
import os
from smolagents import OpenAIServerModel

load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

def get_model(model_id="meta-llama-3.1-8b-instruct"):
    return OpenAIServerModel(
        model_id=model_id,
        api_base="http://127.0.0.1:1234/v1",
        api_key="lm-studio",
    )
