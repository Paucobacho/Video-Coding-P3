# script to livestream with ffmpeg (any protocol you want) and open it
# from mobile or any other device in the same network

import os

source = 'resources/BBB.mp4'


def stream(video_path):
    """
    Invokes ffmpeg to livestream through udp a provided video to a user-specified IP
    (the receiving IP must be inside the same LAN as that of the stream provider)
    param video_path: local path to the video file
    """

    ip = input('Type an IP (same LAN) to send the stream to: ')
    print('Streaming video to {0}:23000 through udp ...'.format(ip))
    print('--> execute ffplay://127.0.0.1:2300 on the receiver')
    cmd = 'ffmpeg -re -i {0} -c:v copy -loglevel quiet -f mpegts udp://{1}:23000'.format(video_path, ip)

    os.system(cmd)


stream(source)