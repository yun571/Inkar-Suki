from .sl import *

async def item_(name: str = None):  # 物价 <物品>
    if token is None:
        return [PROMPT_NoToken]
    final_url = f"https://www.jx3api.com/view/trade/record?robot={bot}&name={name}&scale=1"
    data = await get_api(final_url)
    if data["code"] == 400:
        return ["唔……尚未收录该物品。"]
    return data["data"]["url"]