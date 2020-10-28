import socketserver
import logging
import os
port = ('127.0.0.1', 8000)

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

        # 发回response
        self.request.sendall(echoAll)


if __name__ == "__main__":
    logging.basicConfig(format='[%(levelname)s] %(asctime)s: %(message)s', level=logging.INFO)
    ss = socketserver.ThreadingTCPServer(port, fServer)
    ss.serve_forever()

