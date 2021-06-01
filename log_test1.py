---
Basic:
  dec: "Basic Settings"
  parameters:
    -
      url: /settings/basic.json
      data: slug=da1677475c27
      header: {
                 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko)\
                  Chrome/67.0.3396.99 Safari/537.36",
                 "Content-Type": "keep-alive"
              }

## ```Second, code structure and framework flow

# 1, The code structure is shown in the figure below:
# ![Insert picture description here](https://img-blog.csdnimg.cn/20200920212010248.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L0RlYXRoQWx0aGFz,size_16,color_FFFFFF,t_70#pic_center)

## Three, detailed functions and instructions

# 1, Define the configuration file config.ini
#  Distinguish the test environment in this file[private_debug]And formal environment[online_release]Define related configuration items separately,[mail]Some are mail-related configuration items

# ```python
# http interface test framework configuration information

[private_debug]
# debug test service
tester = your name
environment = debug
versionCode = your version
host = www.jianshu.com
loginHost = /Login
loginInfo = email=wang@user.com&password=123456

[online_release]
# releaseOfficial service
tester = your name
environment = release
versionCode = v1.0
host = www.jianshu.com
loginHost = /Login
loginInfo = email=wang@user.com&password=123456

[mail]
#Send mail information
smtpserver = smtp.163.com
sender = test1@163.com
receiver = wang@user.com
username = wang@user.com
password = 123456
