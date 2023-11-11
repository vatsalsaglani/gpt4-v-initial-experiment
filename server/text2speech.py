import httpx
import uuid


async def text2Speech(text: str, voice: str, api_key: str):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {"model": "tts-1", "input": text, "voice": voice}
    async with httpx.AsyncClient(timeout=600) as request:
        response = await request.post("https://api.openai.com/v1/audio/speech",
                                      headers=headers,
                                      json=payload)
        # print(response.text)
        response.raise_for_status()
        # fn = f"{str(uuid.uuid4())}.mp3"
        return response.content
