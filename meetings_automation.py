import pyautogui as pag
import time


def main():
    global meeting_id, meeting_pswd
    
    meeting_id = input("Enter Meeting ID: ")
    meeting_pswd = input("Enter Meeting Password: ")
    time.sleep(0.5)

    go_desktop()
    
    # success variables can contain only True or False 
    success_zoom = find_zoom()
    if not success_zoom:
        return      # If find_zoom() fails, this stops the whole program 
    
    success_join_plus = find_join_plus_icon()
    if not success_join_plus:
        return 
    
    success_meet_id = find_join_meeting_window()
    if not success_meet_id:
        return

    if meeting_pswd == "":  # If a meeting does not require a password, skip the find_meeting_password_window()
        return 
    else:
        success_meeting_password = find_meeting_password_window()
        if not success_meeting_password:
            return


# Simulates the pressing of Windows+D to go to the Desktop
def go_desktop():
    pag.hotkey("win", "d")


# In this function, we first create a variable called "zoom_icon_cord" and set it equal to None.
# We take advantage of the fact that the PyAutoGUI module is designed in such a way that if an image can't be found on the screen, it returns None.
# As long as the image (in this case, the Zoom icon) can't be found and the time elapsed is lesser than 50 sec, the while loop will keep executing and will keep searching for the image.
# But if it does find the image, the x and y values of the coordinates of the image are assigned to the zoom_icon_cord variable. Then, it double clicks on those coordinates.
def find_zoom():
    zoom_icon_cord = None
    
    # start gets the time at which this function starts executing
    start = time.time()
    now = time.time()

    while zoom_icon_cord == None:
        while (now - start) < 50:   # As long as time elapsed (now - start) is less than 50 seconds, it will keep searching for the image
            print("Finding Zoom Icon...")
            zoom_icon_cord = pag.locateCenterOnScreen("all_icons\icon_zoom.png", confidence=0.7)
            now = time.time()   # Gets the current time (in seconds) to update the time eleapsed 

            # If the image is found, then do...
            if zoom_icon_cord != None:
                pag.click(zoom_icon_cord, clicks=2)
                print("\nFound Zoom Icon!\n")
                return True

        # If time elapsed is greater than 50 sec, it stops the current function (find_zoom()) by returning False
        else:
            print("\nCould not find Zoom icon on Desktop! \n")
            return False


def find_join_plus_icon():
    join_plus_cord = None

    start = time.time() 
    now = time.time()

    while join_plus_cord == None:
        while (now - start) < 50:
            print("Finding Join Plus Icon...")
            join_plus_cord = pag.locateCenterOnScreen("all_icons\join_plus_icon.png", confidence=0.8)
            now = time.time()

            if join_plus_cord != None:
                pag.click(join_plus_cord)
                print("\nFound Join Plus Icon! \n")
                return True
        else:
            print("\nCould not find Join Plus Icon! \n")
            return False


def find_join_meeting_window():
    global meeting_id
    
    join_grey_btn = None

    start = time.time()
    now = time.time()

    while join_grey_btn == None:
        while (now - start) < 50:
            join_grey_btn = pag.locateOnScreen("all_icons\join_grey_btn.png", confidence=0.7)
            now = time.time()

            if join_grey_btn != None:
                pag.write(meeting_id, interval=0.07)
                print("Finished typing Meeting ID \n")
                pag.click(pag.locateCenterOnScreen("all_icons\join_btn.png", confidence=0.7))
                #pag.press("enter")
                return True
        else:
            print("\nCould not type Meeting ID! \n")
            return False

                
def find_meeting_password_window():
    global meeting_pswd
    
    join_meet_grey_btn = None
    m_p_img = None

    start = time.time()
    now = time.time()

    while join_meet_grey_btn == None and m_p_img == None:
        while (now - start) < 50:
            join_meet_grey_btn = pag.locateCenterOnScreen("all_icons\join_meeting_grey_btn.png", confidence=0.7)
            m_p_img = pag.locateCenterOnScreen("all_icons\m_password_img.png", confidence=0.7)
            now = time.time()

        if join_meet_grey_btn != None:
            pag.write(meeting_pswd)
            print("Finished typing Meeting Password \n")
            pag.click(pag.locateCenterOnScreen("all_icons\join_meeting_btn.png", confidence=0.7))
            #pag.click("enter")
            return True
        
        else:
            print("\nCould not type Meeting Password! \n")
            return False

        
if __name__ == "__main__":
    main()

