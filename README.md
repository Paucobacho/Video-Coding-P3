# Video-Coding-P3

## Task 1
Python script that invokes FFMPEG to create a HLS transport stream container with a provided video. The .ts and .m3u8 files will be created with its execution. 

## Task 2

A MPD video file with encryption is created using bento4. Here are the commands executed to fragment, encrypt and dash the file.  

- Fragmentation step: 
```bash
mp4fragment BBB.mp4 BBB-frag.mp4
```
- Encryption and dashing step: 
```bash
mp4dash --marlin --encryption-key=121a0fca0f1b475b8910297fa8e0a07e:a0a1a2a3a4a5a6a7a8a9aaabacadaeaf BBB-frag.mp4
```

When trying to open the resulting video at resources/output/video/avc1/init.mp4 an error pops up since it is encrypted.  

## Task 3 
Python script that invokes FFMPEG to livestream a provided video to another machine from the same LAN as the provider. 

## Task 4
Once connected to a twitch [streaming](https://twitch.tv/leekbeats) some information can be extracted through the Google Chrome browser developer tools. For example, going to the network tab and playing the stream it can be observed that it is using the HLS technology since some .m3u8 and .ts files are being requested by the client through the HTTP GET method. 

![screenshot][image1]

[image1]: https://github.com/Paucobacho/Video-Coding-P3/blob/main/captura.png

Now, downloading a transport stream (.ts) file from the streaming and analyzing it with FFMPEG it can be seen that the stream video is encoded with h264 and the audio with aac:

```bash
$ ffprobe -i twitch_stream.ts
ffprobe version N-109086-geb1e359a14-tessus  https://evermeet.cx/ffmpeg/  Copyright (c) 2007-2022 the FFmpeg developers
  built with Apple clang version 11.0.0 (clang-1100.0.33.17)
  configuration: --cc=/usr/bin/clang --prefix=/opt/ffmpeg --extra-version=tessus --enable-avisynth --enable-fontconfig --enable-gpl --enable-libaom --enable-libass --enable-libbluray --enable-libdav1d --enable-libfreetype --enable-libgsm --enable-libmodplug --enable-libmp3lame --enable-libmysofa --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenh264 --enable-libopenjpeg --enable-libopus --enable-librubberband --enable-libshine --enable-libsnappy --enable-libsoxr --enable-libspeex --enable-libtheora --enable-libtwolame --enable-libvidstab --enable-libvmaf --enable-libvo-amrwbenc --enable-libvorbis --enable-libvpx --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxavs --enable-libxvid --enable-libzimg --enable-libzmq --enable-libzvbi --enable-version3 --pkg-config-flags=--static --disable-ffplay
  libavutil      57. 42.100 / 57. 42.100
  libavcodec     59. 52.102 / 59. 52.102
  libavformat    59. 34.101 / 59. 34.101
  libavdevice    59.  8.101 / 59.  8.101
  libavfilter     8. 50.100 /  8. 50.100
  libswscale      6.  8.112 /  6.  8.112
  libswresample   4.  9.100 /  4.  9.100
  libpostproc    56.  7.100 / 56.  7.100
Input #0, mpegts, from 'twitch_stream.ts':
  Duration: 00:00:02.00, start: 50226.000000, bitrate: 1434 kb/s
  Program 1 
  Stream #0:0[0x100]: Audio: aac (LC) ([15][0][0][0] / 0x000F), 48000 Hz, stereo, fltp, 279 kb/s
  Stream #0:1[0x101]: Video: h264 (Main) ([27][0][0][0] / 0x001B), yuv420p(tv, bt709, progressive), 852x480 [SAR 1:1 DAR 71:40], 30 fps, 30 tbr, 90k tbn
  Stream #0:2[0x102]: Data: timed_id3 (ID3  / 0x20334449)
Unsupported codec with id 98313 for input stream 2
```







