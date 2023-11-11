import httpx


async def chatCompletion(messages, model, api_key, **kwargs):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    # print(headers)
    payload = {"messages": messages, "model": model, **kwargs}
    async with httpx.AsyncClient(timeout=120) as request:
        response = await request.post(
            "https://api.openai.com/v1/chat/completions",
            headers=headers,
            json=payload)
        # print(response.text)
        response.raise_for_status()
        return response.json()
