"""Module providing dataclasses, flask modules, utils methods"""

import dataclasses
from flask import jsonify, request
from utils import check_payload_data, get_users_visited_sub_count


@dataclasses.dataclass
class Sub:
    """This class has calculation method for sub"""

    def post(self):
        """This method will perform calculation of sub

        Returns:
            Response: This will send response as dict of message and status code
        """
        payload = request.get_json()
        result = check_payload_data(payload, "sub")
        if result["status code"] != 200:
            return jsonify(result)

        x = int(payload["x"])
        y = int(payload["y"])
        return_json = {
            "message": x - y,
            "status code": result["status code"],
            "visits": get_users_visited_sub_count(),
        }
        return jsonify(return_json)
