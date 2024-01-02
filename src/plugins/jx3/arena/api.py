from src.tools.dep import *


@Jx3Arg.requireToken
@Jx3Arg.requireTicket
async def arena_records(server: str = None, name: str = None, mode: str = "33"):
    final_url = f"{Config.jx3api_link}/view/match/recent?token={token}&name={name}&server={server}&robot={bot}&ticket={ticket}&mode={mode}&scale=1"
    data = await get_api(final_url)
    if data["code"] == 400:
        return [PROMPT_ServerInvalid]
    if data["code"] == 404:
        return ["唔……未找到该玩家的记录，请检查玩家名或服务器名。"]
    return data["data"]["url"]


@Jx3Arg.requireToken
@Jx3Arg.requireTicket
async def arena_rank(mode: str = "33"):
    final_url = f"{Config.jx3api_link}/view/match/awesome?token={token}&robot={bot}&ticket={ticket}&mode={mode}&scale=1"
    data = await get_api(final_url)
    if data["code"] == 400:
        return ["唔……名剑模式输入错误。"]
    return data["data"]["url"]


@Jx3Arg.requireToken
@Jx3Arg.requireTicket
async def arena_statistics(mode: str = "33"):
    final_url = f"{Config.jx3api_link}/view/match/schools?token={token}&robot={bot}&ticket={ticket}&mode={mode}&scale=1"
    data = await get_api(final_url)
    if data["code"] == 400:
        return ["唔……名剑模式输入错误。"]
    return data["data"]["url"]
