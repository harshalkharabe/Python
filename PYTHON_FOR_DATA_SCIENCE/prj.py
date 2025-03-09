import os
import numpy as np
import cvzone
import cv2
from cvzone.PoseModule import PoseDetector


def add_alpha_channel(img):
    """ Convert a 3-channel BGR image to a 4-channel BGRA image with an alpha mask. """
    b, g, r = cv2.split(img)
    alpha = np.ones(b.shape, dtype=b.dtype) * 255  # Create an alpha mask (fully visible)
    return cv2.merge([b, g, r, alpha])


cap = cv2.VideoCapture("D:/TUTORIAL/PYTHON FULL STACK/PYTHON/PYTHON_FOR_DATA_SCIENCE/Shirts/Videos/1.mp4")
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

detector = PoseDetector()

shirtFolderPath = "D:/TUTORIAL/PYTHON FULL STACK/PYTHON/PYTHON_FOR_DATA_SCIENCE/Shirts"

if not os.path.isdir(shirtFolderPath):
    print(f"Error: The directory '{shirtFolderPath}' does not exist.")
    exit()

listShirts = os.listdir(shirtFolderPath)

if not listShirts:
    print("Error: No shirts found in the directory.")
    exit()
# print(listShirts)
fixedRatio = 262 / 190  # widthOfShirt/widthOfPoint11to12
shirtRatioHeightWidth = 581 / 440
imageNumber = 0
# imgButtonRight = cv2.imread(f"{shirtFolderPath}/button.jpg", cv2.IMREAD_UNCHANGED)
# Ensure button images have an alpha channel
imgButtonRight = cv2.imread(f"{shirtFolderPath}/button.jpg", cv2.IMREAD_UNCHANGED)
if imgButtonRight.shape[-1] == 3:  # Convert to RGBA if it's RGB
    imgButtonRight = cv2.cvtColor(imgButtonRight, cv2.COLOR_BGR2BGRA)

# imgButtonLeft = cv2.flip(imgButtonRight, 1)
imgButtonLeft = cv2.flip(imgButtonRight, 1)
counterRight = 0
counterLeft = 0
selectionSpeed = 10

while True:
    success, img = cap.read()
    if not success:
        print("Error: Could not read video frame.")
        break

    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    
    if lmList and len(lmList) > 12:
        lm11 = lmList[11][1:3]
        lm12 = lmList[12][1:3]

        if lm11[0] != lm12[0]:  
            widthOfShirt = int(abs(lm11[0] - lm12[0]) * fixedRatio)
            
            if widthOfShirt > 0:
                print(f"Shirt width: {widthOfShirt}")
            else:
                print("Error: Calculated widthOfShirt is zero or negative.")
                continue
        else:
            print("Error: lm11 and lm12 are too close together.")
            continue
        
        shirtPath = os.path.join(shirtFolderPath, listShirts[imageNumber])
        imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)
        # Check if conversion is needed
        if imgShirt.shape[-1] != 4:
            print(f"Converting {listShirts[imageNumber]} to PNG format with alpha channel")
            imgShirt = add_alpha_channel(imgShirt)
        # Check if imgShirt is loaded properly
        # widthOfShirt = int(abs(lm11[0] - lm12[0]) * fixedRatio)
        if imgShirt is None:
            print(f"Error: Could not load {listShirts[imageNumber]}")
            continue  # Skip this frame

        # Ensure widthOfShirt is valid
        if widthOfShirt <= 0:
            print(f"Error: Invalid widthOfShirt: {widthOfShirt}")
            continue  # Skip this frame

        # Resize only if valid
        # imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt * shirtRatioHeightWidth)))
        

        # widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
        imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt * shirtRatioHeightWidth)))

        currentScale = (lm11[0] - lm12[0]) / 190
        offset = int(44 * currentScale), int(48 * currentScale)

        try:
            img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
        except Exception as e:
            print("Error overlaying image:", e)

        img = cvzone.overlayPNG(img, imgButtonRight, (1074, 293))
        img = cvzone.overlayPNG(img, imgButtonLeft, (72, 293))

        if lmList[16][1] < 300:
            counterRight += 1
            cv2.ellipse(img, (139, 360), (66, 66), 0, 0, counterRight * selectionSpeed, (0, 255, 0), 20)
            if counterRight * selectionSpeed > 360:
                counterRight = 0
                if imageNumber < len(listShirts) - 1:
                    imageNumber += 1

        elif lmList[15][1] > 900:
            counterLeft += 1
            cv2.ellipse(img, (1138, 360), (66, 66), 0, 0, counterLeft * selectionSpeed, (0, 255, 0), 20)
            if counterLeft * selectionSpeed > 360:
                counterLeft = 0
                if imageNumber > 0:
                    imageNumber -= 1
        else:
            counterRight = 0
            counterLeft = 0

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to exit
        break

cap.release()
cv2.destroyAllWindows()

# while True:
#     success, img = cap.read()
#     img = detector.findPose(img)
#     # img = cv2.flip(img,1)
#     lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
#     if lmList:
#         # center = bboxInfo["center"]
#         lm11 = lmList[11][1:3]
#         lm12 = lmList[12][1:3]
#         imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)

#         widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
#         print(widthOfShirt)
#         imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt * shirtRatioHeightWidth)))
#         currentScale = (lm11[0] - lm12[0]) / 190
#         offset = int(44 * currentScale), int(48 * currentScale)

#         try:
#             img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
#         except:
#             pass

#         img = cvzone.overlayPNG(img, imgButtonRight, (1074, 293))
#         img = cvzone.overlayPNG(img, imgButtonLeft, (72, 293))

#         if lmList[16][1] < 300:
#             counterRight += 1
#             cv2.ellipse(img, (139, 360), (66, 66), 0, 0,
#                         counterRight * selectionSpeed, (0, 255, 0), 20)
#             if counterRight * selectionSpeed > 360:
#                 counterRight = 0
#                 if imageNumber < len(listShirts) - 1:
#                     imageNumber += 1
#         elif lmList[15][1] > 900:
#             counterLeft += 1
#             cv2.ellipse(img, (1138, 360), (66, 66), 0, 0,
#                         counterLeft * selectionSpeed, (0, 255, 0), 20)
#             if counterLeft * selectionSpeed > 360:
#                 counterLeft = 0
#                 if imageNumber > 0:
#                     imageNumber -= 1

#         else:
#             counterRight = 0
#             counterLeft = 0

#     cv2.imshow("Image", img)
#     cv2.waitKey(1)