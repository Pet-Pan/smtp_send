# smtp_send


**使用本脚本时，你需要以下内容** 


| variate      | typeof |
| --------- | -----:|
| 邮件服务器地址  | String |
| 端口     |   Numbers |
| 账号      |   String |
| 密码      |   String |
| 发件人地址      |   String |
| 收件人地址      |   String |
| 标题      |   String |
| 正文      |   String |

# 开始使用

单独使用

    >python smtp_send.py 邮件服务器地址 端口 账号 密码 发件人地址 收件人地址 标题 正文

作为模块使用

    import smtp_send
    aa = smtp_send.smtpsend(host=邮件服务器地址, port=端口, account=账号, password=密码)
    aa.mailtext_send(sender=发件人地址, to=收件人地址, subject=标题, body=正文)


----

### End
