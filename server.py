import socketserver
from http.server import HTTPServer, CGIHTTPRequestHandler
import logging
import os
import sys
import time
import datetime
port = ('127.0.0.1', 8010)

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
        file = open(current_path + "/log/log.txt", 'w+')
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
        sys.stderr.write("%s - - [%s] %s\n" %
                         (self.address_string(),
                          self.log_date_time_string(),
                          format%args))
        current_path = os.path.dirname(__file__)
        file = open(current_path + "/log/log.txt", 'a')
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

