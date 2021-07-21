from hand_landmark_model import HandDetector
import cv2
import pyautogui
import time
from pynput.mouse import Button, Controller
import autopy
import numpy as np
from mss import mss
from PIL import Image
import screen_brightness_control as sbc

handDetector = HandDetector(min_detection_confidence=0.7)
webcamFeed = cv2.VideoCapture(0)

mouse = Controller()

pyautogui.FAILSAFE = False

# Declaration of Right Hand Landmarks
right_thumb = 0
right_index = 0
right_middle = 0
right_ring = 0
right_little = 0

# Declaration of Right Hand Landmarks

left_thumb = 0
left_index = 0
left_middle = 0
left_ring = 0
left_little = 0

wCam, hCam = 640, 480
frameR = 100  # Frame Reduction
smoothening = 5

pTime = 0
plocX, plocY = 0, 0
clocX, clocY = 0, 0

############################################################################


def showImage(imgName):
    img = Image.open(imgName)
    img.show()


working1 = False
working2 = False
working3 = False
working4 = False
working5 = False
working6 = False
working7 = False
working8 = False

print("Below are the functionality you can select from")
time.sleep(1)
print("1. Switch Window")
time.sleep(0.5)
print("2. Space")
time.sleep(0.5)
print("3. Enter")
time.sleep(0.5)
print("4. Screenshot")
time.sleep(0.5)
print("5. Volume Up")
time.sleep(0.5)
print("6. Volume Down")
time.sleep(0.5)
print("7. Backspace")
time.sleep(0.5)
print("8. Brightness Up")
time.sleep(1)

showImage("left_index_middle.jpeg")
while not working1:
    try:
        g1 = int(input("Please select which functionality would you like to assign to this gesture [1/2/3/4/5/6/7/8]"))
        working1 = True
    except ValueError:
        print("Please only enter an integer")

showImage("left_index_thumb.jpeg")
while not working2:
    try:
        g2 = int(input("Please select which functionality would you like to assign to this gesture [1/2/3/4/5/6/7/8]"))
        working2 = True
    except ValueError:
        print("Please only enter integer")

showImage("left_thumb.jpeg")

while not working3:
    try:
        g3 = int(input("Please select which functionality would you like to assign to this gesture [1/2/3/4/5/6/7/8]"))
        working3 = True
    except ValueError:
        print("Please only enter integers")


showImage("right_index_middle_ring.jpeg")

while not working4:
    try:
        g4 = int(input("Please select which functionality would you like to assign to this gesture [1/2/3/4/5/6/7/8]"))
        working4 = True

    except ValueError:
        print("Please only enter integers")

showImage("right_index_middle_ring_little.jpeg")

while not working5:
    try:
        g5 = int(input("Please select which functionality would you like to assign to this gesture [1/2/3/4/5/6/7/8]"))
        working5 = True
    except ValueError:
        print("Please only enter integers")

showImage("right_index_thumb_little.jpeg")
while not working6:
    try:
        g6 = int(input("Please select which functionality would you like to assign to this gesture [1/2/3/4/5/6/7/8]"))
        working6 = True
    except ValueError:
        print("Please only enter integers")

showImage("right_pinky_thumb.jpeg")
while not working7:
    try:
        g7 = int(input("Please select which functionality would you like to assign to this gesture [1/2/3/4/5/6/7/8]"))
        working7 = True
    except ValueError:
        print("Please only enter integers")

showImage("right_thumb.jpeg")
while not working8:
    try:
        g8 = int(input("Please select which functionality would you like to assign to this gesture [1/2/3/4/5/6/7/8]"))
        working8 = True
    except ValueError:
        print("Please only enter integers")

#############################################################################


##################################################


def backspace():
    cv2.putText(image, "Backspace", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)  # BACKSPACE
    pyautogui.hotkey('backspace')
    time.sleep(0.2)


def volumeUp():
    cv2.putText(image, "Volume Increase", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)  # VOLUME UP
    pyautogui.press('volumeup')


def volumeDown():
    cv2.putText(image, "Volume Down", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)  # VOLUME DOWN
    pyautogui.press('volumedown')


def windowSwitch():
    cv2.putText(image, "WINDOW SWITCH", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)  # SWITCH WINDOW
    pyautogui.hotkey('ctrl', 'alt', 'tab')
    time.sleep(1)


def screenshot():
    cv2.putText(image, "MOUSE LEFT CLICK", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)  # SCREENSHOT
    filename = mss().shot()
    print(filename)
    time.sleep(1)


def enter():
    cv2.putText(image, "ENTER", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)  # ENTER
    pyautogui.press('enter')
    time.sleep(1)


def space():
    cv2.putText(image, "SPACE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)  # SPACE
    pyautogui.press('space')
    time.sleep(1)


def brightness():
    cv2.putText(image, "BRIGHTNESS UP", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)  # BRIGHTNESS UP
    current_brightness = sbc.get_brightness()
    print(current_brightness)
    new_brightness = sbc.set_brightness(current_brightness + 5)
    print(new_brightness)



functions_dict = {
    '1': windowSwitch,
    '2': space,
    '3': enter,
    '4': screenshot,
    '5': volumeUp,
    '6': volumeDown,
    '7': backspace,
    '8': brightness
}
#################################################

while True:
    status, image = webcamFeed.read()
    # webcamFeed.set(3, wCam)
    # webcamFeed.set(4, hCam)
    wScr, hScr = autopy.screen.size()
    handLandmarks = handDetector.findHandLandMarks(image=image, draw=True)
    count = 0

    if len(handLandmarks) != 0:

        right_thumb = True if (handLandmarks[4][3] == "Right" and handLandmarks[4][1] > handLandmarks[3][1]) else False
        right_index = True if (handLandmarks[4][3] == "Right" and handLandmarks[8][2] < handLandmarks[6][2]) else False
        right_middle = True if (
                handLandmarks[4][3] == "Right" and handLandmarks[12][2] < handLandmarks[10][2]) else False
        right_ring = True if (handLandmarks[4][3] == "Right" and handLandmarks[16][2] < handLandmarks[14][2]) else False
        right_little = True if (
                handLandmarks[4][3] == "Right" and handLandmarks[20][2] < handLandmarks[18][2]) else False

        left_thumb = True if (handLandmarks[4][3] == "Left" and handLandmarks[8][2] < handLandmarks[6][2]) else False
        left_index = True if (handLandmarks[4][3] == "Left" and handLandmarks[8][2] < handLandmarks[6][2]) else False
        left_middle = True if (handLandmarks[4][3] == "Left" and handLandmarks[12][2] < handLandmarks[10][2]) else False
        left_ring = True if (handLandmarks[4][3] == "Left" and handLandmarks[16][2] < handLandmarks[14][2]) else False
        left_little = True if (handLandmarks[4][3] == "Left" and handLandmarks[20][2] < handLandmarks[18][2]) else False

        if right_thumb and right_little and not right_middle and not right_ring and not right_index:
            # backspace()
            functions_dict[str(g7)]()

        elif right_thumb and not right_index and not right_middle and not right_ring and not right_little:
            functions_dict[str(g8)]()

        elif left_thumb and left_index and not left_little and not left_ring and not left_middle:
            functions_dict[str(g2)]()

        elif right_thumb and right_index and right_little and not right_middle and not right_ring:
            functions_dict[str(g6)]()

        elif left_index and left_middle and not left_ring and not left_little and left_thumb:
            functions_dict[str(g1)]()

        elif right_index and right_middle and right_ring and not right_little and not right_thumb:
            functions_dict[str(g4)]()

        elif right_index and right_middle and right_ring and right_little and not right_thumb:
            functions_dict[str(g5)]()

        elif left_thumb and not left_little and not left_ring and not left_index and not left_middle:
            functions_dict[str(g3)]()

    image = handDetector.findHands(image)
    lmList, bbox = handDetector.findPosition(image)

    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
    cv2.rectangle(image, (frameR, frameR), (wCam - frameR, hCam - frameR), (255, 0, 255), 2)

    if right_index and not right_middle and not right_ring and not right_little and not right_thumb:
        cv2.putText(image, "MOVE CURSOR", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)  # MOVE CURSOR
        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
        y3 = np.interp(y1, (frameR, hCam - frameR), (0, hScr))
        clocX = plocX + (x3 - plocX) / smoothening
        clocY = plocY + (y3 - plocY) / smoothening

        autopy.mouse.move(wScr - clocX, clocY)
        cv2.circle(image, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        plocX, plocY = clocX, clocY

    if right_index and right_middle and not right_ring and not right_little and not right_thumb:
        cv2.putText(image, "MOVE CURSOR", (45, 375), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 5)  # CLICK
        length, img, lineInfo = handDetector.findDistance(8, 12, image + 5000)
        print(length)
        if length < 40:
            cv2.circle(img, (lineInfo[4], lineInfo[5]),
                       15, (0, 255, 0), cv2.FILLED)
            autopy.mouse.click()

    cv2.imshow("Webcam", image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcamFeed.release()
cv2.destroyAllWindows()
