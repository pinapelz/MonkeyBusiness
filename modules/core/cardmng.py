from fastapi import APIRouter, Request, Response
from tinydb import Query, where

from core_common import core_process_request, core_prepare_response, E
from core_database import get_db

router = APIRouter(prefix="/core", tags=["cardmng"])


def to_refid(cid):
    # Generate a deterministic 16-digit numeric ID from the hex card ID
    return str(int(cid, 16)).zfill(16)[-16:]


def get_target_table(game_id):
    target_table = {
        "LDJ": "iidx_profile",
        "MDX": "ddr_profile",
        "KFC": "sdvx_profile",
        "M32": "gitadora_profile",
        "PAN": "nostalgia_profile",
        "REC": "dancerush_profile",
        "JDZ": "iidx_profile",
        "KDZ": "iidx_profile",
        "LAV": "polaris_profile",
        "XIF": "polaris_profile",
    }

    return target_table[game_id]


def get_profile(game_id, cid):
    target_table = get_target_table(game_id)
    profile = get_db().table(target_table).get(where("card") == cid)

    if profile is None:
        profile = {
            "card": cid,
            "version": {},
        }

    return profile


def get_profile_by_refid(game_id, refid):
    target_table = get_target_table(game_id)
    return get_db().table(target_table).get(where("refid") == refid)


def get_game_profile(game_id, game_version, cid):
    profile = get_profile(game_id, cid)

    if str(game_version) not in profile["version"]:
        profile["version"][str(game_version)] = {}

    return profile["version"][str(game_version)]


def create_profile(game_id, game_version, cid, pin, refid=None):
    target_table = get_target_table(game_id)
    profile = get_profile(game_id, cid)

    profile["pin"] = pin
    if refid:
        profile["refid"] = refid

    get_db().table(target_table).upsert(profile, where("card") == cid)


@router.post("/{gameinfo}/cardmng/authpass")
async def cardmng_authpass(request: Request):
    request_info = await core_process_request(request)

    refid = request_info["root"][0].attrib["refid"]
    passwd = request_info["root"][0].attrib["pass"]

    profile = get_profile_by_refid(request_info["model"], refid)
    if profile is None or passwd != profile.get("pin", None):
        status = 116
    else:
        status = 0

    response = E.response(E.cardmng(status=status))

    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)


@router.post("/{gameinfo}/cardmng/bindmodel")
async def cardmng_bindmodel(request: Request):
    request_info = await core_process_request(request)

    response = E.response(E.cardmng(dataid=1))

    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)


@router.post("/{gameinfo}/cardmng/getrefid")
async def cardmng_getrefid(request: Request):
    request_info = await core_process_request(request)

    cid = request_info["root"][0].attrib["cardid"]
    passwd = request_info["root"][0].attrib["passwd"]
    refid = to_refid(cid)

    create_profile(request_info["model"], request_info["game_version"], cid, passwd, refid=refid)

    response = E.response(
        E.cardmng(
            dataid=cid,
            refid=refid,
            pcode=refid,
        )
    )

    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)


@router.post("/{gameinfo}/cardmng/inquire")
async def cardmng_inquire(request: Request):
    request_info = await core_process_request(request)

    cid = request_info["root"][0].attrib["cardid"].strip() # Validate/Strip

    profile = get_profile(request_info["model"], cid)
    
    # Check if this is a registered card (has pin or dataid) AND has user profile (name or usr_id)
    # This prevents 'Card Registered but User Unregistered' state which confuses some games (like Polaris)
    is_registered = ("pin" in profile or "dataid" in profile) and ("name" in profile or "usr_id" in profile)

    if is_registered:
        binded = 1
        newflag = 0
        status = 0
    else:
        binded = 0
        newflag = 1
        status = 112
    
    refid = to_refid(cid)
    print(f"cardmng_inquire: cid={cid}, refid={refid}, status={status}")

    response = E.response(
        E.cardmng(
            dataid=cid,
            ecflag=1,
            expired=0,
            binded=binded,
            newflag=newflag,
            refid=refid,
            pcode=refid,
            status=status,
        )
    )

    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)
