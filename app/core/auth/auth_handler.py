import time

import jwt

from core.config import settings


def decode_jwt(token: str):
    """
    :param token: jwt token
    :return:
    :rtype: None | dict
    """
    try:
        decoded_token = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
    except:
        return None
    return decoded_token if decoded_token["expires"] >= time.time() else None