import socket

def handle_client_request():
    pass


request_text = b"""GET http://192.168.8.12:800/indc.kl HTTP/1.1
HOST: 192.168.8.12:800
User-Agent: curl/8.12.1
Accept: */*
Proxy-Connection: Keep-Alive"""

print(request_text)


class HttpClientRequest():
    
    def __init__(self, httpRequest):
        self.httpRequest :str = httpRequest.decode("utf-8")

    def getHost(self):
        hostStartIndex = self.httpRequest.find("HOST: ") + len("HOST: ")
        print(hostStartIndex)
        print(self.httpRequest[hostStartIndex])



http = HttpClientRequest(request_text)
http.getHost()


# python .find()  value not in string return -1