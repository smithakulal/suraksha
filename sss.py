import socket
import ssl
import sys

def open_connection(hostname, port):
    try:
        sd = socket.create_connection((hostname, port))
        return sd
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def init_ctx():
    ctx = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
    return ctx

def show_certs(conn):
    cert = conn.getpeercert()
    if cert:
        print("Server certificates:")
        print("Subject: %s" % cert['subject'])
        print("Issuer: %s" % cert['issuer'])
    else:
        print("Info: No server certificates configured.")

def main():
    if len(sys.argv) != 3:
        print(f"usage: {sys.argv[0]} <hostname> <portnum>")
        sys.exit(1)

    hostname = sys.argv[1]
    portnum = int(sys.argv[2])
    ctx = init_ctx()
    server = open_connection(hostname, portnum)
    with ctx.wrap_socket(server, server_hostname=hostname) as ssl_conn:
        try:
            print(f"Connected with {ssl_conn.version()} encryption")
            show_certs(ssl_conn)
            msg = b"Hello???"
            ssl_conn.sendall(msg)
            data = ssl_conn.recv(1024)
            print(f"Received: \"{data.decode()}\"")
        except Exception as e:
            print(f"Error: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()

