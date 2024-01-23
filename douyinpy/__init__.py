# -*- coding: utf-8 -*-
import logging

from douyinpy.client import DouyinClient  # NOQA
# from douyinpy.component import ComponentOAuth, DouyinComponent  # NOQA
from douyinpy.exceptions import (
    DouyinClientException,
    DouyinException,
    DouyinOAuthException,
    DouyinPayException,
)  # NOQA
from douyinpy.oauth import DouyinOAuth  # NOQA
from douyinpy.parser import parse_message  # NOQA
# from douyinpy.pay import DouyinPay  # NOQA
from douyinpy.replies import create_reply  # NOQA

__version__ = "1.0.0.alpha26"
__author__ = "ferren"

# Set default logging handler to avoid "No handler found" warnings.
logging.getLogger(__name__).addHandler(logging.NullHandler())
