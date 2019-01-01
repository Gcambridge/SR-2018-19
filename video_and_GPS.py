import os
import cv2
from multiprocessing import Process

def underwater_stream():
	os.system("raspivid -t 0 -w 640 -h 480 -fps 25 -b 1200000 -p 0,0,640,480")
	
def surface_stream():
	topside_cam = cv2.VideoCapture(0)
	out = cv2.VideoWriter('surface-output/outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (640,480))

	while(True):
		_, frame = topside_cam.read()
		cv2.imshow("Topside", frame)
		out.write(frame)
		if cv2.waitKey(1) & 0xFF == ord('q'):
			topside_cam.release()
			cv2.destroyAllWindows()
			break

def startgpsd():
	os.system("sudo gpsd /dev/ttyAMA0 -F /var/run/gpsd.sock")
	os.system("sudo foxtrotgps")

underwater_stream = Process(target=underwater_stream)
underwater_stream.start()

surface_stream = Process(target=surface_stream)
surface_stream.start()

gpstracker = Process(target=startgpsd)
gpstracker.start()
