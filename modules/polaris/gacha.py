from fastapi import APIRouter, Request, Response
from core_common import core_process_request, core_prepare_response, E
import time
import uuid

router = APIRouter(prefix="/polaris/gacha", tags=["gacha"])
router.model_whitelist = ["LAV", "XIF"]

@router.post("")
@router.post("/")
@router.post("/{path:path}")
async def polaris_gacha_dispatch(request: Request):
    try:
        request_info = await core_process_request(request)
        method = request_info["method"]
        if method == "get": method = "get_gacha_info" # Mapping for gacha.get -> get_gacha_info (if applicable)

        func_name = f"polaris_gacha_{method}"
        if func_name in globals():
            return await globals()[func_name](request)
        else:
            print(f"GACHA Dispatch: Function {func_name} not found")
            return Response(status_code=404)
    except Exception as e:
        import traceback
        print(traceback.format_exc())
        with open("debug_log.txt", "a") as f:
            f.write(f"\n[GACHA] {traceback.format_exc()}")
        return Response(status_code=500)

async def polaris_gacha_get_gacha_info(request: Request):
    request_info = await core_process_request(request)
    response = E.response(
        E.gacha(
            E.gacha_list(
                E.gacha(
                    E.gacha_id(1, __type="s32"),
                    E.name("Standard Gacha", __type="str"),
                    E.payment_type(0, __type="s32"),
                    E.prob_weight_r(80, __type="s32"),
                    E.prob_weight_sr(15, __type="s32"),
                    E.prob_weight_ssr(5, __type="s32"),
                    E.prob_weight_pickup(0, __type="s32"),
                    E.guarantee_serial_limit(0, __type="s32"),
                    E.gacha_consume_item_id("money.mira", __type="str"),
                    E.gacha_consume_item_count(1000, __type="s32"),
                    E.open_at("2024-01-01 00:00:00", __type="str"),
                    E.close_at("2099-12-31 23:59:59", __type="str"),
                    E.start_softcode("0000000000", __type="str"),
                    E.end_softcode("9999999999", __type="str"),
                    E.drawable_item_type(0, __type="s32"),
                    E.items(),
                )
            )
        )
    )
    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)

async def polaris_gacha_begin_gacha(request: Request):
    request_info = await core_process_request(request)
    response = E.response(
        E.gacha(
            E.now_date(time.strftime("%Y-%m-%d %H:%M:%S"), __type="str"),
            E.transaction_id(str(uuid.uuid4()), __type="str"),
            E.error(
                E.code(0, __type="s32"),
                E.message("", __type="str")
            )
        )
    ) 
    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)

async def polaris_gacha_draw_gacha(request: Request):
    request_info = await core_process_request(request)
    response = E.response(
        E.gacha(
            E.now_date(time.strftime("%Y-%m-%d %H:%M:%S"), __type="str"),
            E.transaction_id(str(uuid.uuid4()), __type="str"),
            E.items(),
            E.error(
                E.code(0, __type="s32"),
                E.message("", __type="str")
            )
        )
    )
    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)

async def polaris_gacha_end_gacha(request: Request):
    request_info = await core_process_request(request)
    response = E.response(
        E.gacha(
            E.now_date(time.strftime("%Y-%m-%d %H:%M:%S"), __type="str"),
            E.transaction_id(str(uuid.uuid4()), __type="str"),
            E.error(
                E.code(0, __type="s32"),
                E.message("", __type="str")
            )
        )
    )
    response_body, response_headers = await core_prepare_response(request, response)
    return Response(content=response_body, headers=response_headers)
