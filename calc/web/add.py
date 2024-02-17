"""Module providing dataclasses, flask modules, utils methods"""

import dataclasses
from flask import jsonify, request
from utils import check_payload_data, get_users_visited_add_count


@dataclasses.dataclass
class Add:
    """This class has calculation method for add"""

    def post(self):
        """This method will perform calculation of add

        Returns:
            Response: This will send response as dict of message and status code
        """
        payload = request.get_json()
        result = check_payload_data(payload, "add")
        if result["status code"] != 200:
            return jsonify(result)

        x = int(payload["x"])
        y = int(payload["y"])
        return_json = {
            "message": x + y,
            "status code": result["status code"],
            "visits": get_users_visited_add_count(),
        }

        return jsonify(return_json)
