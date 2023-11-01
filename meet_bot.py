from time import sleep
import pyautogui as auto
import schedule, webbrowser


link = "meet.google.com/zwc-oboq-ftc"

time = "13:00"

def join():
    webbrowser.open_new_tab('https://' + link)
    sleep(7)
    auto.hotkey('ctrl', 'd')
    auto.hotkey('ctrl', 'e')
    auto.click(1352, 541)


schedule.every().day.at(time).do(join)

while True:
    schedule.run_pending()
    sleep(1)



