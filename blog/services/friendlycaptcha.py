import logging
from json import JSONDecodeError

import requests

from blog.services.errors import FriendlyCaptchaException
from mysite.settings import FRIENDLY_CAPTCHA_API_KEY, FRIENDLY_CAPTCHA_SITE_KEY


def verify_captcha_solution(solution: str) -> bool:
    json_body = {'solution': solution,
                 'secret': FRIENDLY_CAPTCHA_API_KEY,
                 'sitekey': FRIENDLY_CAPTCHA_SITE_KEY}

    try:
        r = requests.post(url='https://friendlycaptcha.com/api/v1/siteverify', json=json_body)
        r.raise_for_status()
        response = r.json()
        if response['success']:
            return True
        else:
            error = ', '.join(response['errorCodes'])
            raise FriendlyCaptchaException(error)
    except (requests.RequestException, JSONDecodeError, FriendlyCaptchaException) as e:
        logging.error(str(e))
        return False
