import pyautogui, time
time.sleep(5)
f = open("spam-domagoj", "r") #INSTEAD OF spam-domagoj type your .txt file
for word in f:
  pyautogui.typewrite(word)
  pyautogui.press("enter")