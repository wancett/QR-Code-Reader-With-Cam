import cv2
from pyzbar.pyzbar import decode
cap = cv2.VideoCapture(0)

def read(frame):
    decoded = decode(frame)
    for obj in decoded:
        print("QR Code Content : ",obj.data.decode('utf-8'))

while True:
    ret, frame = cap.read()

    read(frame)

    cv2.imshow('QR Code Reader', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()