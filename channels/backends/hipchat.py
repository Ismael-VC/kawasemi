# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

import requests

from .base import BaseChannel
from channels.exceptions import HttpError, ImproperlyConfigured


class HipChatChannel(BaseChannel):
    def __init__(self, config):
        # Required
        self.load_required_config(config, {
            "API_ID": "api_id",
            "TOKEN": "token"
        })

        # Optional
        self.load_optional_config(config, {
            "BASE_URL": "base_url",
            "COLOR": "color",
            "NOTIFY": "notify"
        })

        if not hasattr(self, "base_url"):
            self.base_url = "https://api.hipchat.com/v2/"
        self.url = "{0}room/{1}/notification?auth_token={2}".format(
            self.base_url, self.api_id, self.token)

        colors = ("yellow", "green", "red", "purple", "gray", "random")
        if hasattr(self, "color"):
            if self.color not in colors:
                raise ImproperlyConfigured("Invalid color")

        if hasattr(self, "notify"):
            if not isinstance(self.notify, bool):
                raise ImproperlyConfigured("Notify must be bool")

    def send(self, message, fail_silently=False, options=None):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        payload = {
            "message": message
        }
        if hasattr(self, "color"):
            payload["color"] = self.color
        if hasattr(self, "notify"):
            payload["notify"] = self.notify
        try:
            response = requests.post(self.url,
                                     headers=headers,
                                     data=json.dumps(payload))
            if response.status_code != requests.codes.no_content:
                raise HttpError(response.status_code)
        except:
            if not fail_silently:
                raise
