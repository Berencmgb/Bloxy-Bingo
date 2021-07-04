import numpy as np
import time
from PIL import ImageGrab
import pydirectinput as directInput

cardY = np.array([1230, 1265, 1300, 1335, 1370])

card1X = np.array([710, 745, 780, 815, 850])
card2X = np.array([910, 945, 980, 1015, 1050])
card3X = np.array([1110, 1145, 1180, 1215, 1250])
card4X = np.array([1310, 1345, 1380, 1415, 1450])
card5X = np.array([1510, 1545, 1580, 1615, 1650])
card6X = np.array([1710, 1745, 1780, 1815, 1850])

BingoPos = 1280, 1110


def CalculateTime(duration):
    start = time.time()   # A beginning time

    timer = 0

    while timer < duration:
        duration = start - time.time()
        print(duration)
        time.sleep(1)

# Need to make a GUI to select game version. Is it American bingo? Arcade?


def TryBingo():
    directInput.PAUSE = 0.006
    directInput.click(BingoPos[0], BingoPos[1])


while True:
    for x in card1X:
        for y in cardY:
            directInput.PAUSE = 0.006
            directInput.click(x,y)
    for x in card2X:
        for y in cardY:
            directInput.PAUSE = 0.006
            directInput.click(x,y)
    for x in card3X:
        for y in cardY:
            directInput.PAUSE = 0.006
            directInput.click(x,y)
    for x in card4X:
        for y in cardY:
            directInput.PAUSE = 0.006
            directInput.click(x,y)
    for x in card5X:
        for y in cardY:
            directInput.PAUSE = 0.006
            directInput.click(x,y)
    for x in card6X:
        for y in cardY:
            directInput.PAUSE = 0.006
            directInput.click(x,y)
    TryBingo()