from fastapi import Request, Response
from core_common import core_process_request, core_prepare_response, E
import time

async def polaris_pcb_save(request: Request):
    request_info = await core_process_request(request)
    response = E.response(
        E.pcb(
            E.now_date(time.strftime("%Y-%m-%d %H:%M:%S"), __type="str")
        )
    )
    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)

async def polaris_pcb_save_error_log(request: Request):
    request_info = await core_process_request(request)
    response = E.response(
        E.pcb(
            E.now_date(time.strftime("%Y-%m-%d %H:%M:%S"), __type="str")
        )
    )
    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)

async def polaris_pcb_sync_matching_room(request: Request):
    request_info = await core_process_request(request)
    response = E.response(
        E.pcb(
            E.matching_room(
                E.match_id(0, __type="s32"),
                E.location("", __type="str"),
                E.timeup(0, __type="bool"),
                E.decided(0, __type="bool"),
                E.created_at("", __type="str"),
                E.now_date(time.strftime("%Y-%m-%d %H:%M:%S"), __type="str"),
                E.usr_id_1(0, __type="s32"),
                E.usr_id_2(0, __type="s32"),
                E.usr_id_3(0, __type="s32"),
                E.usr_id_4(0, __type="s32"),
            )
        )
    )
    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)

async def polaris_pcb_sync_matching_music(request: Request):
    request_info = await core_process_request(request)
    response = E.response(E.pcb())
    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)

async def polaris_pcb_sync_matching_progress(request: Request):
    request_info = await core_process_request(request)
    response = E.response(E.pcb())
    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)

async def polaris_pcb_sync_matching_game_result(request: Request):
    request_info = await core_process_request(request)
    response = E.response(E.pcb())
    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)

async def polaris_pcb_finish_matching_room(request: Request):
    request_info = await core_process_request(request)
    response = E.response(E.pcb())
    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)
