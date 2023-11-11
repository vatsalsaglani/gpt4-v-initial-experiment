import base64
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api_schemas import QARequest
from text2speech import text2Speech
from completions import chatCompletion
from configs import OPENAI_API_KEY

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def index():
    return {"ok": True}


@app.post("/api/chat")
async def apiVoiceChat(payload: QARequest):
    messages = [{
        "role":
        "system",
        "content":
        f"Provide the answer in {payload.language.title()} language"
    }] + payload.messages
    text_result = await chatCompletion(messages,
                                       "gpt-4-vision-preview",
                                       OPENAI_API_KEY,
                                       temperature=0.2,
                                       max_tokens=2048)
    text_result = text_result.get("choices")[0].get("message").get("content")
    voice_result = await text2Speech(text_result, payload.voice,
                                     OPENAI_API_KEY)
    voice_result_b64 = base64.b64encode(voice_result).decode("utf-8")
    return {"voice_result": voice_result_b64, "text_result": text_result}


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=5010)
