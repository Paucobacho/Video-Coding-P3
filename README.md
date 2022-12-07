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

