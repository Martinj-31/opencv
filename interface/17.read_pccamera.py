import cv2

def display_info(frame, text, pt, value, color=(120, 200, 90)): 
    text += str(value)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, pt, font, 0.7, color, 2)


capture = cv2.VideoCapture(1)  # 0번 카메라 연결
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

# 카메라 속성 획득 및 출력
print("너비 %d" % capture.get(cv2.CAP_PROP_FRAME_WIDTH))
print("높이 %d" % capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
print("노출 %d" % capture.get(cv2.CAP_PROP_EXPOSURE))
print("밝기 %d" % capture.get(cv2.CAP_PROP_BRIGHTNESS))

while True:  # 무한 반복
    ret, frame = capture.read()  # 카메라 영상 받아오기
    if not ret:
        break
    if cv2.waitKey(30) >= 0:
        break
    
    brightness = capture.get(cv2.CAP_PROP_BRIGHTNESS)
    contrast = capture.get(cv2.CAP_PROP_CONTRAST)
    saturation = capture.get(cv2.CAP_PROP_SATURATION)
    display_info(frame, "Brightness: ", (10, 40), brightness)
    display_info(frame, "Contrast: ", (10, 70), contrast)
    display_info(frame, "Saturation: ", (10, 100), saturation)
    title = "Camera Frame"
    
    title = "View Frame from Camera"
    cv2.imshow(title, frame)  # 윈도우에 영상 띄우기
capture.release()