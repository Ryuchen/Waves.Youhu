
import json
import aiohttp

from typing import Annotated
from fastapi import FastAPI, Form

from src.models import Weapon
from src.models import Phantom
from src.models import WavesRole
from src.settings import WavesUrls
from src.settings import REQUEST_HEADERS_BASE

app = FastAPI()

# {
#     "code": 200,
#     "data": {
#         "enableChildMode": false,
#         "gender": 1,
#         "signature": "哈哈哈哈",
#         "headUrl": "https://prod-alicdn-community.kurobbs.com/headCode/Nuoan2.png",
#         "headCode": "80",
#         "userName": "JokingLife",
#         "userId": "12295995",
#         "isRegister": 0,
#         "isOfficial": 0,
#         "status": 0,
#         "unRegistering": false,
#         "token": "eyJhbGciOiJIUzI1NiJ9.
#           eyJjcmVhdGVkIjoxNzIzNDYyOTM4NDIwLCJ1c2VySWQiOjEyMjk1OTk1fQ.
#           EoH852-cEOMp_HdkSpxX7S8XAy4ie_66bf8xVbF342s"
#     },
#     "msg": "请求成功",
#     "success": true
# }

UserId: str = "12295995"
UserName: str = "JokingLife"
UserToken: str = "eyJhbGciOiJIUzI1NiJ9.eyJjcmVhdGVkIjoxNzIzNjE3OTM4MTA3LCJ1c2VySWQiOjEyMjk1OTk1fQ.7UwfHmJn-Z4rwPqwIBwJRQtX_vX7dKamGAgCIMF1U-I"

RoleList: dict = {}

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/user/sdkLogin")
async def getToken(mobile: Annotated[str, Form()], code: Annotated[str, Form()]):
    """
    Try to get Kuro App token
    :param mobile:
    :param code:
    :return:
    """
    devCode: str = "3sHgsQduVSDWiMn7NwCTL42ENcArCNDT"

    data = aiohttp.FormData()
    data.add_field("code", code)
    data.add_field("mobile", mobile)
    data.add_field("device", devCode)

    async with aiohttp.ClientSession() as session:
        async with session.post(WavesUrls["LOGIN_URL"], headers=REQUEST_HEADERS_BASE, data=data) as resp:
            context = await resp.json()
            if resp.status == 200:
                if context["code"] == 200:
                    UserId = context["data"]["userId"]
                    UserName = context["data"]["userName"]
                    UserToken = context["data"]["token"]
                else:
                    return {"message": context}
                return {"message": context}
            else:
                return {"message": context}


@app.post("/user/roleBox")
async def getRoleBox(uid: Annotated[str, Form()]):
    """
    Fetch user's role box by uid
    :param uid: Wuthering Waves game uid
    """

    serverId: str = "76402e5b20be2c39f095a152090afddc"

    data = aiohttp.FormData()
    data.add_field("gameId", 3)
    data.add_field("roleId", uid)
    data.add_field("serverId", serverId)

    REQUEST_HEADERS_BASE.update(
        {"token": UserToken}
    )

    async with aiohttp.ClientSession() as session:
        async with session.post(WavesUrls.get("ROLE_DATA_URL"), headers=REQUEST_HEADERS_BASE, data=data) as resp:
            context = await resp.json()
            if resp.status == 200:
                if context["code"] == 200:
                    # check whether to showToGuest
                    if context["data"]["showToGuest"]:
                        for item in context["data"]["roleList"]:
                            print(item)
                            RoleList.update({
                                str(item.get("roleId")): WavesRole(item)
                            })
                    else:
                        return {"message": "No allow guest to check your roleBox"}

                    #Test Code
                    for item in RoleList:
                        print(item, RoleList[item])
                else:
                    return {"message": context}
                return {"message": context}
            else:
                return {"message": context}


@app.post("/user/roleDetail")
async def getRoleDetail(uid: Annotated[str, Form()], rid: Annotated[str, Form()]):
    """
    Fetch user's role box by uid
    :param uid: Wuthering Waves game uid
    :param rid: Wuthering Waves role id
    """

    # Test Code
    for item in RoleList:
        print(item, RoleList[item])

    serverId: str = "76402e5b20be2c39f095a152090afddc"

    data = aiohttp.FormData()
    data.add_field("gameId", 3)
    data.add_field("roleId", uid)
    data.add_field("serverId", serverId)
    data.add_field("id", rid)

    REQUEST_HEADERS_BASE.update(
        {"token": UserToken}
    )

    print(RoleList.get(rid))

    async with aiohttp.ClientSession() as session:
        async with session.post(WavesUrls.get("ROLE_DETAIL_URL"), headers=REQUEST_HEADERS_BASE, data=data) as resp:
            context = await resp.json()
            if resp.status == 200:
                if context["code"] == 200:
                    wavesRole = RoleList.get(rid)
                    wavesRole.level = context["data"]["level"]
                    wavesRole.setChainList(context["data"]["chainList"])
                    wavesRole.setSkillList(context["data"]["skillList"])
                    wavesRole.equipWeapon(context["data"]["weaponData"])
                    wavesRole.equipPhantom(context["data"]["phantomData"])
                    wavesRole.detail()
                else:
                    return {"message": context}
                return {"message": context}
            else:
                return {"message": context}