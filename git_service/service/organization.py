from flask import jsonify
from flask_api import status
import requests
import time
import json
from ..common import log, constants, util
from ..common.error_response import error_response_preparation
from ..model.access_history import AccessHistory
from .. import db


def get_org_list(page_number, page_size):
    try:
        log.info(f"Entry into get_org_list")
        page_number, page_size = util.get_page_num_size(page_number, page_size)
        log.info(f"page_number: {page_number} | page_size: {page_size}")

        parameter = {"page_number": page_number, "page_size": page_size}
        access_history_obj = AccessHistory(
            created_date_time=util.get_time_in_ms(time.time()),
            parameter=json.dumps(parameter)
        )
        db.session.add(access_history_obj)
        db.session.commit()
        log.info("Request param saved in db")

        url = constants.GIT_ORG_LIST_URL
        url += f'?per_page={page_size}'
        url += f'&since={page_number}'
        log.info(f"request url: {url}")
        response = requests.get(url=url, timeout=30)
        log.info(f"response status_code: {response.status_code}")
        if response.status_code == 200:
            return response.json()
        else:
            response = error_response_preparation(
                response.status_code, constants.RESPONSE_ERROR, response.json())
        return jsonify(response)
    except Exception as err:
        log.error("Error in get_org_list" + str(err))
        response = error_response_preparation(
            status.HTTP_500_INTERNAL_SERVER_ERROR, constants.RESPONSE_ERROR, constants.ERROR)
        return response, status.HTTP_500_INTERNAL_SERVER_ERROR
