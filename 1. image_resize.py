from configparser import Interpolation
import cv2

def rescaleFrame(frame, scale = 0.75):
    # Images, Videos and Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation = cv2.INTER_AREA)

def changeRes(width, height):
    # Live Video
    capture.set(3, width)
    capture.set(4, height)

# Reading Videos
capture = cv2.VideoCapture('Videos/dog.mp4')
while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale = .2)

    cv2.imshow('Video', frame)
    cv2.imshow('Video Resized', frame_resized)

    if cv2.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv2.destroyAllWindows()
