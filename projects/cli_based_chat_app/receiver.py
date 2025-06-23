import socket
try :
    s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("socket created")
    ##Sender KE ANDAR IP ADD RECEIVER KA HI AAEYGA
    ##hamesha and 
    ip_add = "172.16.2.68"
    port = 8888
    complete_add = (ip_add,port)
    s.bind(complete_add)
    while True:
        message , sender_address = s.recvfrom(1024)
        print("raw msg", message)
        print("sender address", sender_address)

        decoded_msg = message.decode("ascii")
        print("message : ", decoded_msg)
except Exception as e:
    print("an error occured", e)