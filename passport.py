# -*- coding: utf-8 -*-
"""
    passport
    ~~~~~~~~

    An auth method for passport.

    :copyright: (c) 2020 by staugur.
    :license: BSD 3-Clause, see LICENSE for more details.
"""

__version__ = '0.1.0'
__author__ = 'staugur <staugur@saintic.com>'
__description__ = '通过Passport认证'


import json
from flask import g, jsonify, session, make_response
from flask._compat import PY2
if PY2:
    from urllib import urlencode
    from urllib2 import Request, urlopen
else:
    from urllib.parse import urlencode
    from urllib.request import Request, urlopen

site_auth = True
intpl_hooksetting = u'''
<div class="layui-form-item">
    <label class="layui-form-label">
        <b style="color: red;">*</b> Passport接口地址
    </label>
    <div class="layui-input-block">
        <input type="url" name="passport_url" value="{{ g.site.passport_url }}"
        placeholder="passport程序登录接口地址" 
        autocomplete="off" class="layui-input">
    </div>
</div>
'''


def post(url, data=None):
    if data and isinstance(data, dict):
        data = urlencode(data).encode("utf-8")
    req = Request(
        url,
        data=data,
        headers={"User-Agent": "picbed-ssoclient/v1"}
    )
    res = urlopen(req)
    res = res.read()
    return json.loads(res)


def login_api(usr, pwd, set_state, max_age, is_secure):
    if g.cfg.passport_url:
        res = post(g.cfg.passport_url, dict(
            account=usr,
            password=pwd
        ))
        if res["code"] == 0:
            data = res["data"]
            if set_state:
                session.update(
                    signin=True,
                    username=usr,
                    avatar=data.get("avatar"),
                    is_admin=data.get("is_admin"),
                    nickname=data.get("nick_name"),
                )
            return make_response(jsonify(res))


def logout_handler():
    session.pop("signin", None)
    session.pop("username", None)
    session.pop("avatar", None)
    session.pop("is_admin", None)
    session.pop("nickname", None)


def before_request():
    if g.signin is False and session.get("signin"):
        g.signin = True
        g.userinfo = dict(
            username=session.get("username"),
            avatar=session.get("avatar"),
            is_admin=session.get("is_admin"),
            nickname=session.get("nickname"),
        )
