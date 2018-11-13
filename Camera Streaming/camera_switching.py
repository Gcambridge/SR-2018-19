import sys
import cv2
from picamera.array import PiRGBArray
from picamera import PiCamera

def surface_stream(): 
    topside_cam = cv2.VideoCapture(0)

    while(True):
        _, frame = topside_cam.read()
        cv2.imshow("Topside", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    topside_cam.release()
    cv2.destroyAllWindows()
    
def underwater_stream():
    camera = PiCamera()
    camera.resolution = (640, 480)
    camera.framerate = 32
    rawCapture = PiRGBArray(camera, size=(640,480))
    time.sleep(1.0)

    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array

        cv2.imshow("Under Water Feed", image)
        rawCapture.truncate(0)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

while(True):
    feed = input("Toggle Camera:")
    if(feed == "u"):
        #start underwater feed
        print("start underwater feed")
        surface_stream()
    elif(feed == "s"):
        #start surface feed
        print("start surface stream")
        underwater_stream()
    if (feed == "q"):
        break