import numpy as np
import time
from PIL import ImageGrab
import pydirectinput as input

card1X = np.array([710, 745, 780, 815, 850])
card1Y = np.array([1230, 1265, 1300, 1335, 1370])


def CalculateTime(duration):
    start = time.time()   # A beginning time

    timer = 0

    while timer < duration:
        duration = start - time.time()
        print(duration)
        time.sleep(1)


while True:
    for x in card1X:
        for y in card1Y:
            input.click(x,y)