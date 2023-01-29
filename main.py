from model import draw_keypoints, get_keypoints
import cv2
from database import Database

VID_ID = 'id'
VID_PATH = 'path'
VID_LABEL = 'label'

db = Database('train')

with open('keypoints.csv', 'w') as f:
    f.write('id, label, frame, key0, key1, key2, key3, key4, key5, key6, key7, key8, key9, key10, key11, key12, key13, key14, key15, key16, key17, key18, key19, key20')

    for i in range(len(db)):
        data = db.getVideoFile(i)
        id = data[VID_ID]
        cls = data[VID_LABEL]
        cap = cv2.VideoCapture(data[VID_PATH])

        frame_no = 0
        while cap.isOpened():
            ret, frame = cap.read()

            if ret:
                resize_frame = cv2.resize(frame, (400, 400))
                hands = get_keypoints(resize_frame)
                drawn_frame = draw_keypoints(resize_frame)

                if hands is not None:
                    f.write(f'{id, cls, frame_no, }')
                else:
                    f.write('{1}, {2}, {3}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}, {0}'.format('None', id, cls, i))
                # cv2.imshow('video', drawn_frame)

                # if cv2.waitKey(30) & 0xFF == ord('q'):
                #     break
                frame_no += 1

            else:
                break

        cap.release()
# cv2.destroyAllWindows()
