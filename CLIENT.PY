import socket

SERVER_IP = '127.0.0.1'
SERVER_PORT = 8002

flag = True

def answer(claient_msg):
    if (claient_msg == '1'):
       return '1'
    elif (claient_msg == '2'):
        return input("select the album to view the list of songs " )
    elif (claient_msg == '3'):
        return input("Enter song name to get its length")
    elif (claient_msg == '4'):
        return input("Enter song name to get its lyrics")
    elif (claient_msg == '5'):
        return input("Enter song name to get its album")
    elif (claient_msg == '6'):
        return input("Enter a word to get all the song with the word in the song name")
    elif (claient_msg == '7'):
        return input("Enter a word to get all the song with the word in the song lyrics")
    elif (claient_msg == '8'):
        return '8'

def sec_connect(SERVER_IP,SERVER_PORT,msg):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connecting to remote computer 800
    server_address = (SERVER_IP, SERVER_PORT)
    sock.connect(server_address)
    sock.sendall(msg.encode())
    # Receiving data from the server
    server_msg = sock.recv(1024)
    print(server_msg.decode())
    sock.close()

# Create a TCP/IP socket

while(flag):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connecting to remote computer 800
    server_address = (SERVER_IP, SERVER_PORT)
    sock.connect(server_address)
    print ('''1 - Album list - The user receives the album list.
                 2 - Song list in the album - The user clicks on an album name and gets the list of all the songs in that album.
                 3 - Accept a song length - The user enters a song name and gets its length.
                 4 -  Receive lyrics of a song - The user enters the name of a song and receives all the lyrics.
                 5 - What album is the song on? - The user clicks on a song name and gets his album
                 6 - Search for a song - the username Tap a word and get the names of all the songs that contain that word (* does not matter letter size)
                 7 - Search for a song by words In the song - the user clicks a word and gets the names of all the songs that contain that word (* no matter the size of the letters)
                 8 - Exit
           ''')
    action_selection = str(input())
    client_msg = str(answer(action_selection))
    client_msg_to_server = action_selection + ',' + client_msg
    # Sending data to server
    sock.sendall(client_msg_to_server.encode())
    # Receiving data from the server
    server_msg = sock.recv(1024)
    print(server_msg.decode())
    if(action_selection == '8'):
        flag = False
    # Closing the socket
    sock.close()


