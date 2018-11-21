import cv2
import hashlib

def sha256sum(filename):
    h = hashlib.sha256()
    with open(filename, 'rb', buffering=0) as f:
        for b in iter(lambda : f.read(128*1024), b''):
            h.update(b)
    return h.hexdigest()

cap = cv2.VideoCapture(0)
fadd = './frame.png'

# Check if the webcam is opened correctly
if not cap.isOpened():
    raise IOError("Cannot open webcam")

i = 0
while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
    cv2.imshow('Input', frame)
    c = cv2.waitKey(1)

    cv2.imwrite(fadd,frame)
    print("frame hash",sha256sum(fadd))

    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
