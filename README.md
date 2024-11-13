# Video_Conferencing_Application

Overview:
The combined server and client code implements a real-time video streaming system with audio communication. The server code establishes a socket server, accepts client connections, receives video frames from clients, and displays them in real-time. It also receives audio streams from clients. On the other hand, the client code captures video frames from a camera or video file, sends them to the server for streaming, and simultaneously sends audio to the server.
The server code uses the OpenCV library for video processing and the vidstream library for audio streaming. It utilizes threading to handle multiple client connections concurrently. The client code establishes a socket connection with the server, captures video frames, and sends them to the server for display and streaming. It also utilizes the vidstream library for audio streaming.
The server and client communicate using the pickle and struct modules to serialize and pack the video frames and audio data for transmission over the network.


Server Code Structure:

Importing Required Libraries:
The code begins by importing necessary libraries, including socket, cv2, pickle, struct, threading, datetime, pyshine, and vidstream. These libraries are essential for socket communication, video processing, audio streaming, and other functionalities.
Defining Functions:

A.	handle_client(client_socket, addr, audio_port):
This function handles each client connected to the server.
Parameters:
client_socket: The socket object representing the client connection.
addr: The address of the client.
audio_port: The port number for audio streaming.
Functionality:
Initializes variables for video recording and frame shape. Starts an AudioReceiver to receive audio from the client. Receives video frames from the client and processes them. Writes the frames to a video file. Displays the frames with a timestamp. Listens for user input to stop the streaming. Closes the client socket and stops the audio receiver.

B.	accept_clients(server_socket): 
This function listens for client connections and handles them.
Parameters:
server_socket: The socket object representing the server.
Functionality:
Accepts client connections. Starts a new thread to handle each client connection. Increments the audio port for each new client.

        C. main(): 
The main function that initializes the server, binds it to a host IP and port, and starts accepting client connections.

Functionality:
Creates a socket object for the server. Retrieves the host IP address. Binds the socket to the host IP and a specified port. Sets a timeout for the server socket. Starts listening for client connections. Calls accept_clients function to handle client connections.

Explanation for server side:
The provided code implements a server that enables real-time video streaming with audio reception. It creates a socket server, binds it to a host IP and port, and listens for incoming client connections. When a client connects, a separate thread is started to handle the client. The video frames received from the client are displayed in a window . The frames are annotated with a timestamp and client information.
The handle_client function is responsible for receiving video frames, processing them, and displaying them. It also handles the audio reception using the AudioReceiver class from the vidstream library. The received frames are written to a video file using OpenCV's VideoWriter. The function continuously listens for incoming frames until the user terminates the streaming by pressing 'q'.
The accept_clients function listens for client connections using the server socket. For each new connection, it starts a separate thread by calling the handle_client function, passing the client socket, client address, and audio port.
The main function initializes the server, binds it to a specified IP and port, and starts accepting client connections by calling accept_clients.


Client Code Structure:
Importing Required Libraries:
The code begins by importing necessary libraries, including socket, cv2, pickle, struct, imutils, and vidstream. These libraries are essential for socket communication, video processing, audio streaming, and other functionalities.
Initializing Camera or Video Capture:
If camera is True, the code initializes video capture using cv2.VideoCapture(0) to capture frames from the default camera. If camera is False, it prints a message indicating that the video is not found.

Creating a Client Socket:
Creates a socket object for the client using socket.socket(socket.AF_INET, socket.SOCK_STREAM). Specifies the server's IP address and port to establish a connection.

Initializing Audio Sender:
Creates an AudioSender object to send audio to the server. Specifies the server's IP address and the audio port (5556). Starts the audio stream.

Sending Video Frames:
Enters a while loop to continuously send video frames until the user terminates the streaming. Reads a frame from the camera or video file using vid.read(). Resizes the frame using imutils.resize() to a width of 380 pixels. Serializes the frame using pickle.dumps() and calculates the length of the serialized data. Packs the length and serialized data into a message using struct.pack() and sends it to the server using client_socket.sendall(). Displays the frame in a window with a caption indicating the recipient's IP address. Listens for user input to stop the streaming by pressing 'q'.

Handling Exception:
Catches any exception that may occur during video capture or streaming. Prints a message indicating that the video is finished.
Stops the audio stream.

Explanation for client side:
The provided code demonstrates a client-side implementation for real-time video streaming and audio sending. It first initializes video capture from a camera or video file using OpenCV's VideoCapture function. If the camera variable is set to True, it captures frames from the default camera (index 0). If camera is False, it prints a message indicating that the video is not found.
Next, a client socket is created using the socket module. The client socket is connected to the server's IP address and port specified in host_ip and port variables.
An AudioSender object is initialized to send audio to the server. The IP address of the server and the audio port (5556) are provided to the AudioSender constructor. The audio stream is started using the start_stream() method.
The code enters a while loop to continuously capture frames, send them to the server, and display them on the client side. It reads a frame from the camera or video file using vid.read(), resizes the frame to a width of 380 pixels using imutils.resize(), serializes the frame using pickle.dumps(), and calculates the length of the serialized data. The length and serialized data are packed into a message using `

Conclusion:
The combined server and client code provides a functional real-time video streaming system with audio communication. The server allows multiple clients to connect simultaneously and stream their video frames. It displays the received frames in real-time, annotating them with client information and timestamps. The server also receives audio streams from clients.
This system can be utilized in various applications, such as video conferencing, remote surveillance, and live streaming. It provides a flexible and extensible foundation for building real-time video streaming applications with audio communication.
