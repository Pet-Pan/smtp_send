import base64
import sys
import time
from telnetlib import Telnet


def p_read():
    time.sleep(0.1)
    # print(tn.read_very_eager().decode('ascii'))
    return


if len(sys.argv) != 9:
    sys.exit()

邮件服务器地址 = sys.argv[1]
端口 = int(sys.argv[2])
账号 = sys.argv[3]
密码 = sys.argv[4]
发件人地址 = sys.argv[5]
收件人地址 = sys.argv[6]
标题 = sys.argv[7]
正文 = sys.argv[8]

tn = Telnet(邮件服务器地址, port=端口)
tn.write(b"HELO SMTP\n")
p_read()
tn.write(b"auth login\n")
p_read()
tn.write(base64.b64encode(账号.encode("utf-8")) + b"\n")
p_read()
tn.write(base64.b64encode(密码.encode("utf-8")) + b"\n")
p_read()
tn.write(b"mail from:<" + 发件人地址.encode("utf-8") + b">\n")
p_read()
tn.write(b"rcpt to:<" + 收件人地址.encode("utf-8") + b">\n")
p_read()
tn.write(b"data\n")
p_read()
tn.write(b"subject:" + 标题.encode("utf-8") + b"\n\n")
p_read()
tn.write(正文.encode("utf-8") + b"\n" + b".\n")
p_read()
tn.close()
sys.exit()
