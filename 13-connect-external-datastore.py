import sys
import os
from pydantic import BaseModel
import asyncio
from google import genai
from google.genai.types import (
    FunctionDeclaration,
    GenerateContentConfig,
    GoogleSearch,
    HarmBlockThreshold,
    HarmCategory,
    MediaResolution,
    Part,
    Retrieval,
    SafetySetting,
    Tool,
    ToolCodeExecution,
    VertexAISearch,
)

#UPDATE THIS
data_store_location = "global"
data_store_id = "[your-data-store-id]"

credential_path = os.getenv("CRED_PATH")
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

PROJECT_ID = os.getenv("PROJECT_ID")
if not PROJECT_ID or PROJECT_ID == "[your-project-id]":
    PROJECT_ID = str(os.environ.get("GOOGLE_CLOUD_PROJECT"))

LOCATION = os.environ.get("GOOGLE_CLOUD_REGION", "us-central1")

client = genai.Client(vertexai=True, project=PROJECT_ID, location=LOCATION)

if not client.vertexai:
    print(f"Using Gemini Developer API.")
elif client._api_client.project:
    print(
        f"Using Vertex AI with project: {client._api_client.project} in location: {client._api_client.location}"
    )
elif client._api_client.api_key:
    print(
        f"Using Vertex AI in express mode with API key: {client._api_client.api_key[:5]}...{client._api_client.api_key[-5:]}"
    )

MODEL_ID = "gemini-2.0-flash"

chat = client.chats.create(model=MODEL_ID)

vertex_ai_search_tool = Tool(
    retrieval=Retrieval(
        vertex_ai_search=VertexAISearch(
            datastore=f"projects/{PROJECT_ID}/locations/{data_store_location}/collections/default_collection/dataStores/{data_store_id}"
        )
    )
)

response = client.models.generate_content(
    model=MODEL_ID,
    contents="What is the company culture like?",
    config=GenerateContentConfig(tools=[vertex_ai_search_tool]),
)

print((response.text))

print(response.candidates[0].grounding_metadata)