from win32gui import FindWindow, GetWindowRect, MoveWindow

windowNameOne = "1.txt - Notepad"
windowNameTwo = "2.txt - Notepad"

while True:
    #Window1
    windowHandleOne = FindWindow(None, windowNameOne)
    windowRectOne = GetWindowRect(windowHandleOne)  
    rectOne = windowRectOne
    x1 = rectOne[2] #- rect[0]
    y1 = rectOne[3] #- rect[1]
    

    #Window2
    #windowHandleTwo = FindWindow(None, windowNameTwo)
    #windowTwo = GetWindowRect(windowHandleTwo)  
    #rectTwo = windowTwo
    #x2 = rectTwo[2] #- rect[0]
    #y2 = rectTwo[3] #- rect[1]
    
    hwnd = FindWindow(None, windowNameTwo)
    MoveWindow(hwnd, x1, y1, 720, 720, True)

    print(x1,y1)

