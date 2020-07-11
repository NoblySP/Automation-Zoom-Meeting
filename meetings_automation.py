import pyautogui as pag
import time


def main():
    global meeting_id, meeting_pswd
    
    meeting_id = input("Enter Meeting ID: ")
    meeting_pswd = input("Enter Meeting Password: ")
    time.sleep(0.5)

    go_desktop()
    find_zoom()
    find_join_plus_icon()

    find_join_meeting_window()
    find_meeting_password_window()
    


def go_desktop():
    pag.hotkey("win", "d")

    
def find_zoom():
    zoom_icon_cord = None

    while zoom_icon_cord == None:
        print("Finding Zoom Icon...")
        zoom_icon_cord = pag.locateCenterOnScreen("icon_zoom.png", confidence=0.7)
    else:
        pag.click(zoom_icon_cord, clicks=2)
        print("\nFound Zoom Icon!\n")


def find_join_plus_icon():
    join_plus_cord = None

    while join_plus_cord == None:
        print("Finding Join Plus Icon...")
        join_plus_cord = pag.locateCenterOnScreen("join_plus_icon.png", confidence=0.8)
    else:
        pag.click(join_plus_cord)
        print("\nFound Join Plus Icon! \n")


def find_join_meeting_window():
    global meeting_id
    
    join_grey_btn = None

    while join_grey_btn == None:
        join_grey_btn = pag.locateOnScreen("join_grey_btn.png", confidence=0.7)
    else:
        pag.write(meeting_id)
        time.sleep(1)
        print("Finished typing Meeting ID \n")
        pag.click(pag.locateCenterOnScreen("join_btn.png", confidence=0.7))
        #pag.press("enter")
                
def find_meeting_password_window():
    global meeting_pswd
    
    join_meet_grey_btn = None
    m_p_img = None

    while join_meet_grey_btn == None and m_p_img == None:
        join_meet_grey_btn = pag.locateCenterOnScreen("join_meeting_grey_btn.png", confidence=0.7)
        m_p_img = pag.locateCenterOnScreen("m_password_img.png", confidence=0.7)
    else:
        pag.write(meeting_pswd)
        print("Finished typing Meeting Password \n")
        pag.click(pag.locateCenterOnScreen("join_meeting_btn.png", confidence=0.7))
        #pag.click("enter")



if __name__ == "__main__":
    main()




