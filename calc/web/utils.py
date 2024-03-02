"""Module providing a pymongo action methods."""

from flask import jsonify
from pymongo import MongoClient

client = MongoClient("mongodb://db:27017")
db = client["CalcDb"]
user_visit = db["user_visit"]
user_visit.insert_one(
    {
        "users_visited_count": 0,
        "users_visited_add_count": 0,
        "users_visited_sub_count": 0,
        "users_visited_mul_count": 0,
        "users_visited_div_count": 0,
        "users_visited_mod_count": 0,
    }
)


def check_payload_data(payload, method_name):
    """
    Function will check the received payload is valid
    """
    if "x" not in payload:
        return parameter_missing_error_response("x")
    if "y" not in payload:
        return parameter_missing_error_response("y")
    if not isinstance(payload["x"], int) and not payload["x"].isdigit():
        return parameter_not_integer_error_response("x")
    if not isinstance(payload["y"], int) and not payload["y"].isdigit():
        return parameter_not_integer_error_response("y")
    if method_name in ("mod", "div") and int(payload["y"]) == 0:
        return parameter_zero_error_response("y")
    return success_response()


def parameter_missing_error_response(param):
    """This method will help to send error response json for missing parameter

    Args:
        param (dict): Payload from request will be send as param

    Returns:
        dict: Return dict of error message and status code
    """
    return_json = {
        "message": f"{param} parameter is missing in Payload. Please check the payload",
        "status code": 400,
    }
    return return_json


def parameter_not_integer_error_response(param):
    """This method will help to send error response json for parameter is not an integer

    Args:
        param (dict): Payload from request will be send as param

    Returns:
        dict: Return dict of error message and status code
    """
    return_json = {
        "message": f"{param} parameter is not a Integer in Payload. Please check the payload",
        "status code": 400,
    }
    return return_json


def parameter_zero_error_response(param):
    """This method will help to send error response json for parameter has value of zero

    Args:
        param (dict): Payload from request will be send as param

    Returns:
        dict: Return dict of error message and status code
    """
    return_json = {
        "message": f"{param} parameter should not be zero. Please check the payload",
        "status code": 400,
    }
    return return_json


def success_response():
    """This method will help to send success response json for valid parameter

    Args:
        param (dict): Payload from request will be send as param

    Returns:
        dict: Return dict of success message and status code
    """
    return_json = {"message": "Payload Verified no issues found", "status code": 200}
    return return_json


def get_users_visited_count():
    """Get the count of the visit api

    Returns:
        int: Return count of the visit api
    """
    prev_user_visited_count = user_visit.find_one({})["users_visited_count"]
    new_user_visited_count = prev_user_visited_count + 1
    user_visit.update_one({}, {"$set": {"users_visited_count": new_user_visited_count}})
    return user_visit.find_one({})["users_visited_count"]


def get_users_visited_add_count():
    """Get the count of the visit add api

    Returns:
        int: Return count of the visit add api
    """
    prev_doc = user_visit.find_one({})
    prev_user_visited_count = prev_doc["users_visited_add_count"]
    new_user_visited_count = prev_user_visited_count + 1
    user_visit.update_one(
        {"_id": prev_doc["_id"]},
        {"$set": {"users_visited_add_count": new_user_visited_count}},
    )
    return user_visit.find_one({})["users_visited_add_count"]


def get_users_visited_sub_count():
    """Get the count of the visit sub api

    Returns:
        int: Return count of the visit sub api
    """
    prev_doc = user_visit.find_one({})
    prev_user_visited_count = prev_doc["users_visited_sub_count"]
    new_user_visited_count = prev_user_visited_count + 1
    user_visit.update_one(
        {"_id": prev_doc["_id"]},
        {"$set": {"users_visited_sub_count": new_user_visited_count}},
    )
    return user_visit.find_one({})["users_visited_sub_count"]


def get_users_visited_mul_count():
    """Get the count of the visit mul api

    Returns:
        int: Return count of the visit mul api
    """
    prev_doc = user_visit.find_one({})
    prev_user_visited_count = prev_doc["users_visited_mul_count"]
    new_user_visited_count = prev_user_visited_count + 1
    user_visit.update_one(
        {"_id": prev_doc["_id"]},
        {"$set": {"users_visited_mul_count": new_user_visited_count}},
    )
    return new_user_visited_count


def get_users_visited_div_count():
    """Get the count of the visit div api

    Returns:
        int: Return count of the visit div api
    """
    prev_doc = user_visit.find_one({})
    prev_user_visited_count = prev_doc["users_visited_div_count"]
    new_user_visited_count = prev_user_visited_count + 1
    user_visit.update_one(
        {"_id": prev_doc["_id"]},
        {"$set": {"users_visited_div_count": new_user_visited_count}},
    )
    return new_user_visited_count


def get_users_visited_mod_count():
    """Get the count of the visit mod api

    Returns:
        int: Return count of the visit mod api
    """
    prev_doc = user_visit.find_one({})
    prev_user_visited_count = prev_doc["users_visited_mod_count"]
    new_user_visited_count = prev_user_visited_count + 1
    user_visit.update_one(
        {"_id": prev_doc["_id"]},
        {"$set": {"users_visited_mod_count": new_user_visited_count}},
    )
    return new_user_visited_count


def reset_all_visited_count():
    """This method will reset all visited count in all the modules"""
    prev_doc = user_visit.find_one({})
    user_visit.update_one(
        {"_id": prev_doc["_id"]},
        {
            "$set": {
                "users_visited_count": 0,
                "users_visited_add_count": 0,
                "users_visited_sub_count": 0,
                "users_visited_mul_count": 0,
                "users_visited_div_count": 0,
                "users_visited_mod_count": 0,
            }
        },
    )
    return_json = {"message": "All the counts were reset to 0", "status code": 200}
    return jsonify(return_json)
