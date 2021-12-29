import socket
import DATA
server_con = True
def answer(client_msg_action,client_msg_data):
    if(client_msg_action == '1'):
       return DATA.List_of_albums(DATA.FILE)
    elif (client_msg_action == '2'):
       return DATA.list_of_Song_in_album(DATA.FILE, client_msg_data)
    elif (client_msg_action == '3'):
       return Data.song_length(DATA.FILE, client_msg_data)
    elif (client_msg_action == '4'):
        return DATA.word_in_song_name(DATA.FILE, client_msg_data)
    elif (client_msg_action == '5'):
        return DATA.What_album_is_the_song_on(DATA.FILE,client_msg_data)
    elif (client_msg_action == '6'):
        return DATA.word_in_song_name(DATA.FILE,client_msg_data)
    elif (client_msg_action == '7'):
        return DATA.words_in_the_song(DATA.FILE,client_msg_data)
    elif (client_msg_action == '8'):
        return 'BAY BAY'


LISTEN_PORT = 8002
# Create a TCP/IP socket
listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Binding to local port 80
server_address = ('127.0.0.1', LISTEN_PORT)
try:
    listening_sock.bind(server_address)

except Exception as e:
    print(e)
    new_port = 900
    new_server_address = ('127.0.0.1', new_port)
    listening_sock.bind(new_server_address)
    print("Start listening on port " + new_port)
while(server_con):
    print("Start listening on port " + str(LISTEN_PORT))
    # Listen for incoming connections
    listening_sock.listen(10)
    # Create a new conversation socket
    client_soc, client_address = listening_sock.accept()
    # Receiving data from the client
    client_msg = client_soc.recv(1024).decode()
    print(client_msg)
    client_msg_action,client_msg_data = client_msg.split(',')
    server_msg_to_client = answer(client_msg_action,client_msg_data)
    print(client_msg_action)
    print(client_msg_data)
    server_msg_to_client = str(server_msg_to_client)
    print(server_msg_to_client)
    # Sending data back
    client_soc.sendall(server_msg_to_client.encode())
    client_soc.close()
    if(server_msg_to_client == '8'):
        server_con = False
# Closing the conversation socket
# Closing the listening socket
listening_sock.close()


