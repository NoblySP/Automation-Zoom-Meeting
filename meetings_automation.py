# Importing required libraries
import pyautogui as pag
import time


# This main() function executes all the other functions in a particular order
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
    

# This function simulates the pressing of Windows+D to go to the Desktop
def go_desktop():
    pag.hotkey("win", "d")

  
# In this function, we first create a variable called "zoom_icon_cord" and set it equal to None.
# We take advantage of the fact that the PyAutoGUI module is designed in such a way that if an image can't be found on the screen, it returns None.
# As long as the image (in this case, the Zoom icon) can't be found, the while loop will keep executing and will keep searching for the image.
# But if it does find the image, the x and y values of the coordinates of the image are assigned to the zoom_icon_cord variable. Then, it double clicks on those coordinates.

def find_zoom():
    zoom_icon_cord = None

    while zoom_icon_cord == None:
        print("Finding Zoom Icon...")
        zoom_icon_cord = pag.locateCenterOnScreen("all_icons\icon_zoom.png", confidence=0.7)
    else:
        pag.click(zoom_icon_cord, clicks=2)
        print("\nFound Zoom Icon!\n")


def find_join_plus_icon():
    join_plus_cord = None

    while join_plus_cord == None:
        print("Finding Join Plus Icon...")
        join_plus_cord = pag.locateCenterOnScreen("all_icons\join_plus_icon.png", confidence=0.8)
    else:
        pag.click(join_plus_cord)
        print("\nFound Join Plus Icon! \n")


def find_join_meeting_window():
    global meeting_id
    
    join_grey_btn = None

    while join_grey_btn == None:
        join_grey_btn = pag.locateOnScreen("all_icons\join_grey_btn.png", confidence=0.7)
    else:
        pag.write(meeting_id, interval=0.07)
        print("Finished typing Meeting ID \n")
        pag.click(pag.locateCenterOnScreen("all_icons\join_btn.png", confidence=0.7))
        #pag.press("enter")
                
def find_meeting_password_window():
    global meeting_pswd
    
    join_meet_grey_btn = None
    m_p_img = None

    while join_meet_grey_btn == None and m_p_img == None:
        join_meet_grey_btn = pag.locateCenterOnScreen("all_icons\join_meeting_grey_btn.png", confidence=0.7)
        m_p_img = pag.locateCenterOnScreen("all_icons\m_password_img.png", confidence=0.7)
    else:
        pag.write(meeting_pswd)
        print("Finished typing Meeting Password \n")
        pag.click(pag.locateCenterOnScreen("all_icons\join_meeting_btn.png", confidence=0.7))
        #pag.click("enter")



if __name__ == "__main__":
    main()




