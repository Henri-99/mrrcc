from threadedStream import VideoStreamWidget


url='rtsp://192.168.3.82:8554/mjpeg/1'

#   /cam.bmp
#   /cam-lo.jpg
#   /cam-hi.jpg
#   /cam.mjpeg

esp = VideoStreamWidget(src=url)
while True:
    try:
        esp.show_frame("ESP32-CAM")
    except AttributeError:
        pass




# esp = cv2.VideoCapture(url)

# # t1 = time.time()
# # framecount = 0
# while True:
#     ret, frame = esp.read() #returns ret and the frame

#     if (ret):
#         cv2.imshow('frame',frame)
#         # framecount += 1
#     else:
#         print("no new frame")
#     # if (framecount == 10):
#     #     t2 = time.time()
#     #     print(10/(t2-t1), " fps")
#     #     t1 = t2
#     #     framecount = 0
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break




    # while True:
    #     imgResp=request.urlopen(url)
    #     imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    #     img=cv2.imdecode(imgNp,-1)

    #     # all the opencv processing is done here
    #     cv2.imshow('ESP32-CAM Stream',img)
    #     if ord('q')==cv2.waitKey(10):
    #         exit(0)

