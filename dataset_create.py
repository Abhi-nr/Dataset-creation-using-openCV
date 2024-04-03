import os
import cv2
import time
import uuid

IMAGE_PATH=r"C:\Users\HP\Desktop\CollectImages"
labels=['Hello','yes','no','thanks','iloveyou','please']

number_of_images=20

for label in labels:
    img_path= os.path.join(IMAGE_PATH,label)
    os.makedirs(img_path, exist_ok=True)
    #os.markedirs(img_path)
    cap=cv2.VideoCapture(0)
    print('collecting images for {}'.format(label))
    time.sleep(5)
    cont= input("enter continue or quit: ")
    for imgnum in range(number_of_images):
        ret,frame= cap.read()
        imagename=os.path.join(IMAGE_PATH,label, label+'-'+'{}.jpg'.format(str(uuid.uuid1())))
        cv2.imwrite(imagename, frame)
        cv2.imshow('frame', frame)
        time.sleep(2)
        
        if cv2.waitKey(1) & 0xFF==ord('q') and cont=='quit':
            break
    cap.release()
