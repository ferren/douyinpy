# -*- coding: utf-8 -*-
"""
    douyinpy.exceptions
    ~~~~~~~~~~~~~~~~~~~~

    Basic exceptions definition.

    :copyright: (c) 2014 by ferren.
    :license: MIT, see LICENSE for more details.
"""


class DouyinException(Exception):
    """Base exception for douyinpy"""

    def __init__(self, errcode, errmsg):
        """
        :param errcode: Error code
        :param errmsg: Error message
        """
        self.errcode = errcode
        self.errmsg = errmsg

    def __str__(self):
        s = f"Error code: {self.errcode}, message: {self.errmsg}"
        return s

    def __repr__(self):
        _repr = f"{self.__class__.__name__}({self.errcode}, {self.errmsg})"
        return _repr


class DouyinClientException(DouyinException):
    """Douyin API client exception class"""

    def __init__(self, errcode, errmsg, client=None, request=None, response=None):
        super().__init__(errcode, errmsg)
        self.client = client
        self.request = request
        self.response = response


class InvalidSignatureException(DouyinException):
    """Invalid signature exception class"""

    def __init__(self, errcode=-40001, errmsg="Invalid signature"):
        super().__init__(errcode, errmsg)


class APILimitedException(DouyinClientException):
    """Douyin API call limited exception class"""

    pass


class InvalidAppIdException(DouyinException):
    """Invalid app_id exception class"""

    def __init__(self, errcode=-40005, errmsg="Invalid AppId"):
        super().__init__(errcode, errmsg)


class InvalidMchIdException(DouyinException):
    """Invalid mch_id exception class"""

    def __init__(self, errcode=-40006, errmsg="Invalid MchId"):
        super().__init__(errcode, errmsg)


class DouyinOAuthException(DouyinClientException):
    """Douyin OAuth API exception class"""

    pass


class DouyinComponentOAuthException(DouyinClientException):
    """Douyin Component OAuth API exception class"""

    pass


class DouyinPayException(DouyinClientException):
    """Douyin Pay API exception class"""

    def __init__(
        self,
        return_code,
        result_code=None,
        return_msg=None,
        errcode=None,
        errmsg=None,
        client=None,
        request=None,
        response=None,
    ):
        """
        :param return_code: 返回状态码
        :param result_code: 业务结果
        :param return_msg: 返回信息
        :param errcode: 错误代码
        :param errmsg: 错误代码描述
        """
        super().__init__(errcode, errmsg, client, request, response)
        self.return_code = return_code
        self.result_code = result_code
        self.return_msg = return_msg

    def __str__(self):
        _str = f"Error code: {self.return_code}, message: {self.return_msg}. Pay Error code: {self.errcode}, message: {self.errmsg}"
        return _str

    def __repr__(self):
        _repr = f"{self.__class__.__name__}({self.return_code}, {self.return_msg}). Pay({self.errcode}, {self.errmsg})"
        return _repr
