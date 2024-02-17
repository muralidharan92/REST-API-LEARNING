"""Module providing dataclasses, flask modules, utils methods"""

import dataclasses
from flask import jsonify, request
from utils import check_payload_data, get_users_visited_mod_count


@dataclasses.dataclass
class Mod:
    """This class has calculation method for mod"""

    def post(self):
        """This method will perform calculation of mod

        Returns:
            Response: This will send response as dict of message and status code
        """
        # Step1: Get the payload from the request
        payload = request.get_json()
        # Step1.1: Verify validity of payload
        result = check_payload_data(payload, "mod")
        if result["status code"] != 200:
            return jsonify(result)

        x = int(payload["x"])
        y = int(payload["y"])
        return_json = {
            "message": x % y,
            "status code": result["status code"],
            "visits": get_users_visited_mod_count(),
        }
        return jsonify(return_json)
