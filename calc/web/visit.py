"""Module providing dataclasses, flask modules, utils methods"""

import dataclasses
from utils import get_users_visited_count


@dataclasses.dataclass
class Visit:
    """This class has count action for api hit"""

    def get(self):
        """This method will perform count action on api hit

        Returns:
            Response: This will send response as dict of message and status code
        """
        return get_users_visited_count()
