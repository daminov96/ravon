import os
import random
import string

import requests
from django.conf import settings
from django.utils import timezone
from rest_framework import pagination
from rest_framework.response import Response
from twilio.rest import Client

from project.celery import app


class PageNumberPaginationWithTotalPages(pagination.PageNumberPagination):
    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )


def confirmation_code_generator(size=6, chars=string.digits):
    return "".join(random.choice(chars) for x in range(size))


account_sid = "ACe621efa47f1121c4f3f7bde79adb7ad1"
auth_token = "cbd058c6597960c2e3a3a6a555642cdf"
client = Client(account_sid, auth_token)


def sendsms(phone):
    url = "http://smsgw.vas.uz:8808/api/send"
    code = confirmation_code_generator()
    params = {
        "login": settings.SMS_LOGIN,
        "key": settings.SMS_KEY,
        "sender": "Dozolab",
        "phone": phone,
        "text": f"Edumanager.uz \nYour Confirmation Code  \n {code}",
    }
    message = client.messages.create(
        body=f"Your Confirmation Code from edumanager.uz: {code}",
        from_="+17038797832",
        to=f"+{phone}",
    )
    try:
        send = requests.post(url, params=params)
        print(send.text)
    except Exception as ex:
        print(ex)
    return code


@app.task
def invalidate_verification_code(user, time):
    now = timezone.now()
    if not abs((now - time).total_seconds()) > 300:
        user.phone_verification_code = None
        user.save()
