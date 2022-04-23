import base64
import sys
import time
from telnetlib import Telnet


def single_file_execution(): """单独执行时获取参数方法"""
    global 邮件服务器地址, 端口, 账号, 密码, 发件人地址, 收件人地址, 标题, 正文
    if len(sys.argv) != 9:
        print("参数错误，请重新输入\n")
        sys.exit()

    邮件服务器地址 = sys.argv[1]
    端口 = int(sys.argv[2])
    账号 = sys.argv[3]
    密码 = sys.argv[4]
    发件人地址 = sys.argv[5]
    收件人地址 = sys.argv[6]
    标题 = sys.argv[7]
    正文 = sys.argv[8]


class smtpsend:
    def __init__(self, host=None, port=0, account=None, password=None):
        self.邮件服务器地址 = host
        self.端口 = port
        self.账号 = account
        self.密码 = password

    def p_read(self, tn):
        time.sleep(0.1)

    def mailtext_send(self, sender=None, to=None, subject=None, body=None):
        if sender is None:
            self.发件人地址 = self.账号
        else:
            self.发件人地址 = sender
        self.收件人地址 = to
        self.标题 = subject
        self.正文 = body
        # start
        tn = Telnet(host=self.邮件服务器地址, port=self.端口)
        tn.write(b"HELO SMTP\n")
        self.p_read(tn)
        tn.write(b"auth login\n")
        self.p_read(tn)
        tn.write(base64.b64encode(self.账号.encode("utf-8")) + b"\n")
        self.p_read(tn)
        tn.write(base64.b64encode(self.密码.encode("utf-8")) + b"\n")
        self.p_read(tn)
        tn.write(b"mail from:<" + self.发件人地址.encode("utf-8") + b">\n")
        self.p_read(tn)
        tn.write(b"rcpt to:<" + self.收件人地址.encode("utf-8") + b">\n")
        self.p_read(tn)
        tn.write(b"data\n")
        self.p_read(tn)
        tn.write(b"subject:" + self.标题.encode("utf-8") + b"\n\n")
        self.p_read(tn)
        tn.write(self.正文.encode("utf-8") + b"\n" + b".\n")
        time.sleep(0.1)
        a = tn.read_very_eager().decode('ascii')
        print(a)
        if a.startswith('250'):
            self.返回值 = 1    # 邮件发送成功
        else:
            self.返回值 = 0    # 邮件发送失败
        tn.write(b"QUIT\n")
        self.p_read(tn)
        tn.close()
        return self.返回值


if __name__ == '__main__':
    single_file_execution()
    aa = smtpsend(host=邮件服务器地址, port=端口, account=账号, password=密码)
    aa.mailtext_send(sender=发件人地址, to=收件人地址, subject=标题, body=正文)
else:
    del single_file_execution
