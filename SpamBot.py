import pyautogui,time,pywhatkit
pywhatkit.sendwhatmsg("+33619625108","Hello",1,19,11)
time.spleep(5)
for i in range(100):
    pyautogui.write("Hello")
    pyautogui.press("enter")
