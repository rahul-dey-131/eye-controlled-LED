import cv2
import mediapipe as mp
import pyautogui
import time
import serial

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh()

arduinoData = serial.Serial("com3", 9600)
# time.sleep(0.5)

while True:
    while (arduinoData.inWaiting() == 0): pass

    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmarks_points = output.multi_face_landmarks

    frame_h, frame_w, _ = frame.shape

    if landmarks_points:
        landmarks = landmarks_points[0].landmark

        [cv2.circle(frame, (int(landmark.x * frame_w), int(landmark.y * frame_h)), 3, (64, 127, 255)) for landmark in landmarks]

        left_eye_points, right_eye_points = [landmarks[145], landmarks[159]], [landmarks[374], landmarks[386]]
        ldist = (left_eye_points[0].y - left_eye_points[1].y) * 1000
        rdist = (right_eye_points[0].y - right_eye_points[1].y) * 1000
        avgdist = (ldist + rdist) / 2

        distance = float(str(arduinoData.readline(), 'utf-8').strip('\r\n')) * 100

        threshold = 95 - 1.5 * distance
        
        # print(avgdist, distance)
        if (distance <= 60 and distance >= 10): 
            print("Your eyes are closed.") if (avgdist <= threshold) else print("Your eyes are open")
            print(str(int(avgdist <= threshold)))
            arduinoData.write((str(int(avgdist <= threshold)) + '\r').encode())
            # time.sleep(0.5)
        # time.sleep(1)

    cv2.imshow("Eye Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break