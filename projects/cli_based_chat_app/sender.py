import socket
while True:
    try:
        ##creating socket
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #dgram-- DATAGRAM
        print("socket created")
        ip_add = "172.16.2.68"
        port =8888
        target_add = (ip_add,port)
        message = input("enter a message: ")
        if message == 'exit':
            break
        encoded_msg = message.encode("ascii")
        s.sendto(encoded_msg,target_add)
        print("message sent successfully!")
        s.close()
    except Exception as e:
        print("an error occured", e)