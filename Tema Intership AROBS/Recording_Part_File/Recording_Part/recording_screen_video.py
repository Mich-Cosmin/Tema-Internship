
#asa merge cand rulez local
#import constants as c
#asa merge cand rulez din main.py
import Recording_Part.constants as c
import Recording_Part.fisier_logging as l

# =======  include video  ================
import cv2
import numpy as np
import pyautogui


#===================================================================
                # Record the screen video
#==================================================================
#This Python code is used to capture screenshots of your screen at regular intervals 
#and save them as frames in a video file. It uses the pyautogui library to capture the screen, 
#cv2 (OpenCV) to handle video encoding, and numpy to manipulate image data.

def record_video():
    try:
        # display screen resolution (size), get it using pyautogui itself
        # and stores it as a tuple in the SCREEN_SIZE variable.
        SCREEN_SIZE = tuple(pyautogui.size())
        # define the codec (compression algorithm) to be used for the video. 
        #In this case, it's set to XVID, which is a commonly used codec for AVI files.
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        # frames per second. It specifies how many frames should be captured and added to the video per sec.
        fps = 12.0
        # create the video write object
        out = cv2.VideoWriter("integist_ecran_video.avi", fourcc, fps, (SCREEN_SIZE))
        # the time you want to record in seconds

        print("Recording screen...")
        l.logging.info('Recording screen...')
        for i in range(int(c.record_seconds * fps)):
            # make a screenshot
            img = pyautogui.screenshot()
            # convert these pixels to a proper numpy array to work with OpenCV
            frame = np.array(img)
            # convert colors from BGR to RGB
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            # write the frame
            out.write(frame)
            

        print("Finished recording screen.")
        l.logging.info('Finished recording screen.')
        # make sure everything is closed when exited
        cv2.destroyAllWindows()
        out.release()

    except Exception as e:
        # Handle exceptions
        print(f"An error occurred while recording the screen: {str(e)}")
        l.logging.error(f'ERROR: The page could not opened: {e}')


