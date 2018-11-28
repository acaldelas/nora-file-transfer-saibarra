import socket

def Main():
    host = '127.0.0.1'
    port = 50001
    s = socket.socket( socket.AF_INET, socket.SOCK_STREAM)
    s.connect( (host, port) )

    message = "this is my personal message"
    while True:
        s. send( mesage.encode('ascii') )
        data = s.recv(1024)
        print('Received from the server :', str(data.decode('ascii')) )
        
        user_input = input('\nContinue? y/n :')
        if user_input == 'y':
            continue
        else:
            break
    s.close()

if __name__ == '__main__':
    Main()
