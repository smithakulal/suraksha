import socket
import ssl
import os
import sys

def open_listener(port):
    sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sd.bind(('0.0.0.0', port))
    sd.listen(10)
    return sd

def init_server_ctx():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(certfile="mycert.pem", keyfile="mycert.pem")
    return ctx

def show_certs(conn):
    cert = conn.getpeercert()
    if cert:
        print("Server certificates:")
        print("Subject: %s" % cert['subject'])
        print("Issuer: %s" % cert['issuer'])
    else:
        print("No certificates.")

def servlet(conn):
    buf = conn.recv(1024)
    if buf:
        print("Client msg: \"%s\"" % buf.decode())
        conn.sendall(buf)
    conn.close()

def main():
    if os.geteuid() != 0:
        print("This program must be run as root/sudo user!!")
        exit(0)

    if len(sys.argv) != 2:
        print("Usage: %s <portnum>" % sys.argv[0])
        exit(0)

    portnum = int(sys.argv[1])
    ctx = init_server_ctx()
    server = open_listener(portnum)
    while True:
        conn, addr = server.accept()
        print("Connection: %s:%d" % (addr[0], addr[1]))
        conn = ctx.wrap_socket(conn, server_side=True)
        try:
            show_certs(conn)
            servlet(conn)
        finally:
            conn.close()
    
    server.close()

if __name__ == "__main__":
    main()
