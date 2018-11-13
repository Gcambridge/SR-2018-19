import cv2

topside_cam = cv2.VideoCapture(0)

while(True):
    _, frame = topside_cam.read()
    cv2.imshow("Topside", frame)
        
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

topside_cam.release()
cv2.destroyAllWindows()