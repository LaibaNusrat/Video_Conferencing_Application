import socket
import cv2
import pickle
import struct
import imutils
from vidstream import CameraClient, AudioSender

camera = True

if camera == True:
    vid = cv2.VideoCapture(0)
else:
    print('Video Not Found!')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_ip = '192.168.18.123'
port = 5003
client_socket.connect((host_ip, port))
audio_sender = AudioSender(host_ip, 5556)
audio_sender.start_stream()

if client_socket:
    while vid.isOpened():
        try:
            img, frame = vid.read()
            frame = imutils.resize(frame, width=380)
            a = pickle.dumps(frame)
            message = struct.pack("Q", len(a)) + a
            client_socket.sendall(message)
            cv2.imshow(f"TO: {host_ip}", frame)
            key = cv2.waitKey(1) & 0xFF
            if key == ord("q"):
                audio_sender.stop_stream()
                client_socket.close()
                break
        except:
            print('VIDEO FINISHED!')
            audio_sender.stop_stream()
            break
