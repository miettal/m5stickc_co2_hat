import socket
import ssl
import json


def send2slack(channel, username, text):
    host = 'hooks.slack.com'
    port = 443
    path = '/services/T018UBZFSL8/B017XQSNUPQ/uqLvRpkUHe2qiaLZEW8jHsSA'

    ai = socket.getaddrinfo(host, port)
    addr = ai[0][-1]

    s = socket.socket()
    s.connect(addr)
    s = ssl.wrap_socket(s)

    data = json.dumps({
        'channel': channel,
        'username': username,
        'text': text,
    }).encode('ascii')

    s.write("POST {:s} HTTP/1.1\r\n".format(path).encode('ascii'))
    s.write("Host: {:s}\r\n".format(host).encode('ascii'))
    s.write(b"Content-Length: %d\r\n" % len(data))
    s.write(b"Connection: close\r\n")
    s.write(b"\r\n")
    s.write(data)

    print(s.read(4096))
    s.close()


if __name__ == '__main__':
    send2slack('#notify-co2', 'co2sensor', 'test')
