# -*- coding: utf-8 -*-


import time

from douyinpy.client.base import BaseDouyinClient
from douyinpy.client import api


class DouyinClient(BaseDouyinClient):

    """
    微信 API 操作类
    通过这个类可以操作微信 API，发送主动消息、群发消息和创建自定义菜单等。
    """

    API_BASE_URL = "https://api.weixin.qq.com/cgi-bin/"

    # card = api.DouyinCard()
    # cloud = api.DouyinCloud()
    # customservice = api.DouyinCustomService()
    # datacube = api.DouyinDataCube()
    # device = api.DouyinDevice()
    # draft = api.DouyinDraft()
    # freepublish = api.DouyinFreePublish()
    # group = api.DouyinGroup()
    # invoice = api.DouyinInvoice()
    # jsapi = api.DouyinJSAPI()
    # marketing = api.DouyinMarketing()
    # material = api.DouyinMaterial()
    # media = api.DouyinMedia()
    # menu = api.DouyinMenu()
    # merchant = api.DouyinMerchant()
    # message = api.DouyinMessage()
    # misc = api.DouyinMisc()
    # poi = api.DouyinPoi()
    # qrcode = api.DouyinQRCode()
    # scan = api.DouyinScan()
    # semantic = api.DouyinSemantic()
    # shakearound = api.DouyinShakeAround()
    # tag = api.DouyinTag()
    # template = api.DouyinTemplate()
    # user = api.DouyinUser()
    # wifi = api.DouyinWiFi()
    # wxa = api.DouyinWxa()

    def __init__(
        self,
        appid,
        secret,
        access_token=None,
        session=None,
        timeout=None,
        auto_retry=True,
    ):
        super().__init__(appid, access_token, session, timeout, auto_retry)
        self.appid = appid
        self.secret = secret

    def fetch_access_token(self):
        """
        获取 access token
        详情请参考
        https://developer.open-douyin.com/docs/resource/zh-CN/mini-app/develop/server/interface-request-credential/non-user-authorization/get-client_token

        :return: 返回的 JSON 数据包
        """
        return self._fetch_access_token(
            url="https://open.douyin.com/oauth/client_token/",
            params={
                "grant_type": "client_credential",
                "appid": self.appid,
                "secret": self.secret,
            },
        )


# class DouyinComponentClient(DouyinClient):

#     """
#     开放平台代公众号调用客户端
#     """

#     def __init__(
#         self,
#         appid,
#         component,
#         access_token=None,
#         refresh_token=None,
#         session=None,
#         timeout=None,
#     ):
#         # 未用到secret，所以这里没有
#         super().__init__(appid, "", "", session, timeout)
#         self.appid = appid
#         self.component = component
#         # 如果公众号是刚授权，外部还没有缓存access_token和refresh_token
#         # 可以传入这两个值，session 会缓存起来。
#         # 如果外部已经缓存，这里只需要传入 appid，component和session即可
#         cache_access_token = self.session.get(self.access_token_key)

#         if access_token and (not cache_access_token or cache_access_token != access_token):
#             self.session.set(self.access_token_key, access_token, 7200)
#         if refresh_token:
#             self.session.set(self.refresh_token_key, refresh_token)

#     @property
#     def access_token_key(self):
#         return f"{self.appid}_access_token"

#     @property
#     def refresh_token_key(self):
#         return f"{self.appid}_refresh_token"

#     @property
#     def access_token(self):
#         access_token = self.session.get(self.access_token_key)
#         if not access_token:
#             self.fetch_access_token()
#             access_token = self.session.get(self.access_token_key)
#         return access_token

#     @property
#     def refresh_token(self):
#         return self.session.get(self.refresh_token_key)

#     def fetch_access_token(self):
#         """
#         获取 access token
#         详情请参考 https://open.weixin.qq.com/cgi-bin/showdocument?action=dir_list\
#         &t=resource/res_list&verify=1&id=open1419318587&token=&lang=zh_CN

#         这是内部刷新机制。请不要完全依赖！
#         因为有可能在缓存期间没有对此公众号的操作，造成refresh_token失效。

#         :return: 返回的 JSON 数据包
#         """
#         expires_in = 7200
#         result = self.component.refresh_authorizer_token(self.appid, self.refresh_token)
#         if "expires_in" in result:
#             expires_in = result["expires_in"]
#         self.session.set(self.access_token_key, result["authorizer_access_token"], expires_in)
#         self.expires_at = int(time.time()) + expires_in
#         return result
