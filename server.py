import socketserver
import socket
from http.server import HTTPServer, CGIHTTPRequestHandler
import logging
import os
import sys
import getpass
import time
import datetime

port = ('127.0.0.1', 8010)
def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip
class fServer(socketserver.BaseRequestHandler):
    def handle(self):
        print("Connection:  ", self.request)
        print("Address: ", self.client_address)

        msg = self.request.recv(4096).decode()

        httpHead = msg.split('\r\n')[:-1]   # 去除最后一部分HTTP请求正文，保留请求头部，并按行分割
        # 首行
        firstLine = httpHead[0].split(' ')  # 按空格分割首行基本信息
        method = firstLine[0]
        url = firstLine[1]
        version = firstLine[2]
        src=self.client_address[0]
        labels = []
        current_path = os.path.dirname(__file__)
        file = open("log/log.txt", 'w+')
        file.write('recv http request to {} from {}    method:{} version:{}\n'.format(
            url,src,method,version))
        logging.info('recv http request to {} from {}    method:{} version:{}'.format(
            url,src,method,version))
        logging.info('labels:')
        file.write('labels:\n')
        for label in httpHead[1:]:
            labels.append(label.split(': '))
            logging.info('  {}'.format(labels))
            file.write('  {}\n'.format(labels))
        # 简单HTTP示例
        echoBody = """Hi, It's {}\nYou are {}""".format(url, self.client_address).encode()
        echoHead = """HTTP/1.0 200 OK\r\nContent-Length: {}\r\nServer: Fever's\r\nContent-Type: text/html""".format(len(echoBody)).encode()
        echoAll = echoHead + b'\r\n\r\n' + echoBody + b'\r\n'

class kserver( CGIHTTPRequestHandler):
    def log_message(self, format, *args):
        hostname = socket.gethostname()  # 获取当前主机名
        username = getpass.getuser()  # 获取当前用户名
        hostip = get_host_ip()
        # fullname=socket.getfqdn(hostname)
        sys.stderr.write(hostip)
        sys.stderr.write(" - - ")
        sys.stderr.write(hostname)
        sys.stderr.write(" - - ")
        # sys.stderr.write(fullname)
        # sys.stderr.write(" - - ")
        sys.stderr.write(username)
        sys.stderr.write(" - - ")
        sys.stderr.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))
        current_path = os.path.dirname(__file__)

        file = open("log/log.txt", 'a')
        file.write(hostip)
        file.write(" - - ")
        file.write(hostname)
        file.write(" - - ")
        # file.write(fullname)
        # file.write(" - - ")
        file.write(username)
        file.write(" - - ")
        file.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))


if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(asctime)s: %(message)s', level=logging.INFO)
    # ss = socketserver.ThreadingTCPServer(port, fServer)
    # ss.serve_forever()
    try:
        # CGIHTTPRequestHandler.cgi_directories = ['/cgi-bin']
        kserver.cgi_directories = ['/cgi-bin']
        # server = HTTPServer(port, CGIHTTPRequestHandler)
        server = HTTPServer(port, kserver)
        print(f"Running server. Use [ctrl]-c to terminate.")
        server.serve_forever()

    except KeyboardInterrupt:
        print(f"\nReceived keyboard interrupt. Shutting down server.")
        server.socket.close()

