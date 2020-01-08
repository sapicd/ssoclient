picbed-ssoclient
================

这是基于 `picbed <https://github.com/staugur/picbed>`_ 的一个小的扩展模块，
用来接入`staugur/passport <https://github.com/staugur/passport>`_ 登录。

安装
------

- 开发版本

    `$ pip install -U git+https://github.com/staugur/picbed-ssoclient.git@master`

开始使用
----------

此扩展请在部署 `picbed <https://github.com/staugur/picbed>`_ 图床后使用，需要
其管理员进行添加扩展、设置钩子等操作。

添加：
^^^^^^^^

请在 **站点管理-钩子扩展** 中添加第三方钩子，输入名称：passport，
确认后提交即可加载这个模块（请先手动安装好此模块）。

配置：
^^^^^^^^

在 **站点管理-网站设置** 底部的钩子配置区域配置Passport接口地址。

使用：
^^^^^^^^

同样在 **站点管理-网站设置** 底部钩子配置区域中选择第三方认证为up2qiniu
即可。

启用后，在登录页面会首先将用户名、密码请求Passport接口验证，成功后会拦截
后续的默认请求，否则直接跳到默认请求（picbed本身的登录系统）。

PS：登录状态是依靠session
