from PIL import ImageGrab
from PIL import Image
import numpy as np
import cv2 as cv
import pyautogui
        
def checkline(blids,xstart,ystart,xfinish,yfinish):
    if (xstart != xfinish and ystart != yfinish):
        return 0
    if xstart == xfinish:
        mini = min(ystart,yfinish)
        maxi = max(ystart,yfinish)
        for i in range(mini+1,maxi):
            if blids[i][xstart] > 0:
                return 0
    else:
        mini = min(xstart,xfinish)
        maxi = max(xstart,xfinish)
        for i in range(mini+1,maxi):
            if blids[ystart][i] > 0:
                return 0
    return 1

def checkone(blids,xstart,ystart,xfinish,yfinish):
    if (xstart == xfinish or ystart == yfinish):
        return 0
    xturn = xstart
    yturn = yfinish
    if blids[yturn][xturn] == 0:
        checkline1 = checkline(blids,xstart,ystart,xturn,yturn)
        if checkline1 > 0:
            checkline2 = checkline(blids,xfinish,yfinish,xturn,yturn)
        else:
            checkline2 = 0
        if (checkline1 > 0 and checkline2 > 0):
            return 2
    xturn = xfinish
    yturn = ystart
    if blids[yturn][xturn] == 0:
        checkline1 = checkline(blids,xstart,ystart,xturn,yturn)
        if checkline1 > 0:
            checkline2 = checkline(blids,xfinish,yfinish,xturn,yturn)
        else:
            checkline2 = 0
        if (checkline1 > 0 and checkline2 > 0):
            return 2
    return 0

def checktwo(blids,xstart,ystart,xfinish,yfinish):
    precheck = checkline(blids,xstart,ystart,xfinish,yfinish)
    if precheck > 0:
        return 1
    else:
        precheck = checkone(blids,xstart,ystart,xfinish,yfinish)
        if precheck > 0:
            return 2
        else:
            for i in range(0,9):
                if blids[ystart][i] == 0:
                    check1 = checkone(blids,i,ystart,xfinish,yfinish)
                    check2 = checkline(blids,i,ystart,xstart,ystart)
                    if (check1 > 0 and check2 > 0):
                        return 3
            for i in range(0,12):
                if blids[i][xstart] == 0:
                    check1 = checkone(blids,xstart,i,xfinish,yfinish)
                    check2 = checkline(blids,xstart,i,xstart,ystart)
                    if (check1 > 0 and check2 > 0):
                        return 3
    return 0
        
while(True):
    pyautogui.click(609, 214,button='left')
    img2 = ImageGrab.grab(bbox=(609,214,1024,809))
    img2_np = np.array(img2)
    cv.imwrite('temp.png', img2_np)
    imgrd = cv.imread("temp.png")
    blwidth = 50
    blheight = 50
    img01 = Image.open("2-1.png")
    img02 = Image.open("2-2.png")
    img03 = Image.open("2-3.png")
    img04 = Image.open("2-4.png")
    img05 = Image.open("2-5.png")
    img06 = Image.open("2-6.png")
    img07 = Image.open("2-7.png")
    imgblank = Image.open("blank.png")
    img01_np = np.array(img01)
    img02_np = np.array(img02)
    img03_np = np.array(img03)
    img04_np = np.array(img04)
    img05_np = np.array(img05)
    img06_np = np.array(img06)
    img07_np = np.array(img07)
    imgblank_np = np.array(imgblank)
    img01_gray = cv.cvtColor(img01_np, cv.COLOR_BGR2GRAY)
    img02_gray = cv.cvtColor(img02_np, cv.COLOR_BGR2GRAY)
    img03_gray = cv.cvtColor(img03_np, cv.COLOR_BGR2GRAY)
    img04_gray = cv.cvtColor(img04_np, cv.COLOR_BGR2GRAY)
    img05_gray = cv.cvtColor(img05_np, cv.COLOR_BGR2GRAY)
    img06_gray = cv.cvtColor(img06_np, cv.COLOR_BGR2GRAY)
    img07_gray = cv.cvtColor(img07_np, cv.COLOR_BGR2GRAY)
    imgblank_gray = cv.cvtColor(imgblank_np, cv.COLOR_BGR2GRAY)

    img01_gray = cv.GaussianBlur(img01_gray, (3, 3), 0)
    img02_gray = cv.GaussianBlur(img02_gray, (3, 3), 0)
    img03_gray = cv.GaussianBlur(img03_gray, (3, 3), 0)
    img04_gray = cv.GaussianBlur(img04_gray, (3, 3), 0)
    img05_gray = cv.GaussianBlur(img05_gray, (3, 3), 0)
    img06_gray = cv.GaussianBlur(img06_gray, (3, 3), 0)
    img07_gray = cv.GaussianBlur(img07_gray, (3, 3), 0)
    imgblank_gray = cv.GaussianBlur(imgblank_gray, (3, 3), 0)

    blids = np.zeros((12, 9), dtype=int)
    bldels1 = np.zeros((12, 9), dtype=int)
    bldels2 = np.zeros((12, 9), dtype=int)
    bldels3 = np.zeros((12, 9), dtype=int)
    bldels4 = np.zeros((12, 9), dtype=int)
    bldels5 = np.zeros((12, 9), dtype=int)
    bldels6 = np.zeros((12, 9), dtype=int)
    bldels7 = np.zeros((12, 9), dtype=int)
    bldelsblank = np.zeros((12, 9), dtype=int)
    for i in range(0,10):
        for j in range(0,7):
            blockpos = (int(4+j*9.2+j*blheight),int(6+i*9.2+i*blwidth),int(4+j*9.2+(j+1)*blheight),int(6+i*9.2+(i+1)*blwidth))
            img = Image.fromarray(imgrd)
            temp = img.crop(blockpos)
            temp_np = np.array(temp)
            temp_gray = cv.cvtColor(temp_np, cv.COLOR_BGR2GRAY)
            temp_gray = cv.GaussianBlur(temp_gray, (3, 3), 0)
            img_delta = cv.absdiff(imgblank_gray, temp_gray)
            thresh = cv.threshold(img_delta, 80, 255, cv.THRESH_BINARY)[1]
            thresh = cv.dilate(thresh, None, iterations=2)
            contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv.contourArea(c) > 300:
                    bldelsblank[i+1][j+1] = 1
                    
            img_delta = cv.absdiff(img01_gray, temp_gray)
            thresh = cv.threshold(img_delta, 80, 255, cv.THRESH_BINARY)[1]
            thresh = cv.dilate(thresh, None, iterations=2)
            contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv.contourArea(c) > 1000:
                    bldels1[i+1][j+1] = 1

            img_delta = cv.absdiff(img02_gray, temp_gray)
            thresh = cv.threshold(img_delta, 80, 255, cv.THRESH_BINARY)[1]
            thresh = cv.dilate(thresh, None, iterations=2)
            contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv.contourArea(c) > 800:
                    bldels2[i+1][j+1] = 1

            img_delta = cv.absdiff(img03_gray, temp_gray)
            thresh = cv.threshold(img_delta, 80, 255, cv.THRESH_BINARY)[1]
            thresh = cv.dilate(thresh, None, iterations=2)
            contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv.contourArea(c) > 1000:
                    bldels3[i+1][j+1] = 1

            img_delta = cv.absdiff(img04_gray, temp_gray)
            thresh = cv.threshold(img_delta, 80, 255, cv.THRESH_BINARY)[1]
            thresh = cv.dilate(thresh, None, iterations=2)
            contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv.contourArea(c) > 1000:
                    bldels4[i+1][j+1] = 1

            img_delta = cv.absdiff(img05_gray, temp_gray)
            thresh = cv.threshold(img_delta, 80, 255, cv.THRESH_BINARY)[1]
            thresh = cv.dilate(thresh, None, iterations=2)
            contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv.contourArea(c) > 1000:
                    bldels5[i+1][j+1] = 1

            img_delta = cv.absdiff(img06_gray, temp_gray)
            thresh = cv.threshold(img_delta, 80, 255, cv.THRESH_BINARY)[1]
            thresh = cv.dilate(thresh, None, iterations=2)
            contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv.contourArea(c) > 1000:
                    bldels6[i+1][j+1] = 1

            img_delta = cv.absdiff(img07_gray, temp_gray)
            thresh = cv.threshold(img_delta, 80, 255, cv.THRESH_BINARY)[1]
            thresh = cv.dilate(thresh, None, iterations=2)
            contours, hierarchy = cv.findContours(thresh.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            for c in contours:
                if cv.contourArea(c) > 1200:
                    bldels7[i+1][j+1] = 1

            if bldelsblank[i+1][j+1] == 0:
                blids[i+1][j+1] = 0
            elif bldels1[i+1][j+1] == 0:
                blids[i+1][j+1] = 1
            elif  bldels2[i+1][j+1] == 0:
                blids[i+1][j+1] = 2
            elif  bldels3[i+1][j+1] == 0:
                blids[i+1][j+1] = 3
            elif  bldels4[i+1][j+1] == 0:
                blids[i+1][j+1] = 4
            elif  bldels5[i+1][j+1] == 0:
                blids[i+1][j+1] = 5
            elif  bldels6[i+1][j+1] == 0:
                blids[i+1][j+1] = 6
            elif  bldels7[i+1][j+1] == 0:
                blids[i+1][j+1] = 7
    check = 1
    while(check == 1 and testmode == 1):
        check = 0
        checkmatch = 0
        for i1 in range(0,12):
            for j1 in range(0,9):
                for i2 in range(0,12):
                    for j2 in range(0,9):
                        if ((i1 != i2 or j1 != j2) and blids[i1][j1] !=0 and blids[i2][j2] !=0 and blids[i1][j1] == blids[i2][j2]):
                            checkmatch = checktwo(blids,j1,i1,j2,i2)
                            if checkmatch > 0:
                                pyautogui.click(609+int(4+(j1-1)*9.2+(j1-1)*blheight)+25, 214+int(6+(i1-1)*9.2+(i1-1)*blwidth)+25,button='left')
                                blids[i1][j1] = 0
                                cv.waitKey(20)
                                pyautogui.click(609+int(4+(j2-1)*9.2+(j2-1)*blheight)+25, 214+int(6+(i2-1)*9.2+(i2-1)*blwidth)+25,button='left')
                                blids[i2][j2] = 0
                                check = 1
                                cv.waitKey(85)

