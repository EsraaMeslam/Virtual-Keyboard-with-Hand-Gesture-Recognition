
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import cvzone
from pynput.keyboard import Controller
from time import sleep

cap = cv2.VideoCapture(0)

cap.set(3, 743.49)
cap.set(4, 840)

detector = HandDetector(detectionCon=0.5)

chars = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
         ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
         ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/'],
         [' ']]
final_txt = ""

keyboard = Controller()

def draw_all(img, btn_list):
    for btn in btn_list:
        x, y = btn.pos
        w, h = btn.size
        cv2.rectangle(img, btn.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
        cv2.putText(img, btn.text, (x + 13, y + 45), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
        cvzone.cornerRect(img, (btn.pos[0], btn.pos[1], btn.size[0], btn.size[1]),
                          20, t=2, rt=0, colorC=(255, 255, 255))
    return img

class Btn():
    def __init__(self, pos, text, size=[60, 60]):
        self.pos = pos
        self.text = text
        self.size = size

btn_list = []
for i in range(len(chars)):
    for x, char in enumerate(chars[i]):
        if char == ' ':
            btn_list.append(Btn([70 * x + 10, 70 * i + 200], char, size=[620, 60]))
        else:
            btn_list.append(Btn([70 * x + 10, 70 * i + 200], char))

while True:
    ret, img = cap.read()
    img = cv2.flip(img, 1)

    # Detect hands and get landmarks
    hands, img = detector.findHands(img, draw=False)

    if hands:
        # Use only the first detected hand
        hand = hands[0]
        lmlist = hand['lmList']  # List of landmarks

        # Draw the keyboard and detect interactions
        img = draw_all(img, btn_list)

        if lmlist:
            for btn in btn_list:
                x, y = btn.pos
                w, h = btn.size
                if x < lmlist[8][0] < x + w and y < lmlist[8][1] < y + h:
                    # Highlight color when a key is selected
                    cv2.rectangle(img, btn.pos, (x + w, y + h), (50, 50, 50), cv2.FILLED)
                    cv2.putText(img, btn.text, (x + 13, y + 45), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

                    # Extract coordinates of thumb and index finger tips
                    thumb_tip = (lmlist[8][0], lmlist[8][1])
                    index_tip = (lmlist[12][0], lmlist[12][1])

                    # Compute the distance using coordinates
                    dis, _, _ = detector.findDistance(thumb_tip, index_tip, img)  # Pass coordinates directly
                    print(dis)

                    if dis < 22:
                        keyboard.press(btn.text)
                        # Green highlight when the key is pressed
                        cv2.rectangle(img, btn.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                        cv2.putText(img, btn.text, (x + 13, y + 45), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

                        final_txt += btn.text
                        sleep(.9)

    # Draw the title at the top center of the window
    title = "Virtual Keyboard"
    text_size = cv2.getTextSize(title, cv2.FONT_HERSHEY_PLAIN, 3, 3)[0]
    text_x = (img.shape[1] - text_size[0]) // 2
    cv2.putText(img, title, (text_x, 50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 2)

    # Draw the input box and text
    input_box_y = 100  # Position just below the title
    cv2.rectangle(img, (10, input_box_y), (629, input_box_y + 60), (0, 0, 0), cv2.FILLED)
    cv2.putText(img, final_txt, (60, input_box_y + 45), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)

    cv2.imshow("Virtual Keyboard", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
