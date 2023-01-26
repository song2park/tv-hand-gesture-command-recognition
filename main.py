from model import draw_keypoints
import cv2

cap = cv2.VideoCapture(0)

while (cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        drawn_frame = draw_keypoints(frame)

        cv2.imshow('video', drawn_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
