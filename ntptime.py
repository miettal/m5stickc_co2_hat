import usocket
import ustruct
import machine
import utime

NTP_DELTA = 3155673600 - (9*60*60)  # utime epoch(2000) - ntp epoch(1900) - JST
host = "pool.ntp.org"


def time():
    NTP_QUERY = bytearray(48)
    NTP_QUERY[0] = 0x1B
    addr = usocket.getaddrinfo(host, 123)[0][-1]
    s = usocket.usocket(usocket.AF_INET, usocket.SOCK_DGRAM)
    try:
        s.settimeout(1)
        s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
    finally:
        s.close()
    val = ustruct.unpack("!I", msg[40:44])[0]
    return val - NTP_DELTA


def settime():
    t = time()

    tm = utime.localtime(t)
    machine.RTC().datetime((tm[0], tm[1], tm[2], tm[6] + 1, tm[3], tm[4], tm[5], 0))
