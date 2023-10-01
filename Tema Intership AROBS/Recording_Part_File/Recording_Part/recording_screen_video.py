
#asa merge cand rulez local
#import constants as c
#import fisier_logging as l

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
#pyautogui->capture the screen, cv2 (OpenCV) to handle video encoding, and numpy to manipulate image data
#"PyAutoGUI library" -> retrieves the dimensions (width and height) of the primary screen or monitor.

def record_video():
    try:
        #capture screenshots of your screen at regular intervals and save them as frames in a video file
        SCREEN_SIZE = tuple(pyautogui.size())
        #tuple(...): convert the result of pyautogui.size() into a tuple. 
                #The tuple() constructor takes an iterable (such as a list or tuple) and converts it  
                #into a tuple data structure. In this case, it's converting the result into a tuple to 
                #make it easier to work with.
        #After executing SCREEN_SIZE = tuple(pyautogui.size()), the SCREEN_SIZE variable will contain a 
        #tuple with the screen dimensions, like (width, height).
        
    except Exception as e:
        print(f"Error getting screen size: {e}")
        l.logging.error(f"Error getting screen size: {e}")
        return

    try:
        #This line is used to specify the codec (compression algorithm) to be used for encoding video when 
        #creating a VideoWriter object in OpenCV (cv2). 
        #cv2: This is the OpenCV library, commonly used for computer vision and image/video processing task it
        #VideoWriter_fourcc(...): This is a function provided by OpenCV for creating a VideoWriter object 
                                  #with a specified codec. 
        #"XVID":-> This is the codec identifier passed as a string argument to VideoWriter_fourcc(). 
                 #In this case, "XVID" represents the Xvid codec, which is a popular and widely supported  
                 #codec for compressing video in the Xvid format.                                 
        
        #In this example, fourcc is used to specify the Xvid codec when creating the VideoWriter object (out). 
        #The VideoWriter object will use this codec to compress and write video frames to the output 
        #file in the AVI format. The codec chosen can affect the video file's size, quality, and 
        #compatibility with different media players.
        fourcc = cv2.VideoWriter_fourcc(*"XVID")       #stores the codec identifier 

    except Exception as e:
        print(f"Error creating VideoWriter object: {e}")
        l.logging.error(f"Error creating VideoWriter object: {e}")
        return

    try:
        # In the context of video processing, FPS refers to the number of individual frames (images) 
        #displayed or recorded per second.
        #The 12.0 is a floating-point number to specify the frame rate with a decimal point.
        fps = 12.0          #The frame rate determines how smoothly the video appears.
        #A higher frame rate, such as 30 or 60 FPS, results in smoother motion but may require more storage
        #space and processing power. A lower frame rate, 12 FPS, may appear less smooth but
        #can be suitable for certain applications where lower resource usage is acceptable.
        #In practice, you would use this fps variable when creating a VideoWriter object (for recording) 
        #or when specifying the frame rate for video playback to control the speed at which frames are 
        #displayed or recorded.
    except Exception as e:
        print(f"Error setting frames per second: {e}")
        l.logging.error(f"Error setting frames per second: {e}")
        return

    #numele fisierului in care este salvat
    out = cv2.VideoWriter("integist_ecran_video.avi", fourcc, fps, SCREEN_SIZE)
    

    print("Start recording screen...")
    l.logging.info('Start recording screen.')
    
    for i in range(int(c.record_seconds * fps)):
        try:
            #the code img = pyautogui.screenshot() is used to capture a screenshot of the entire screen 
            #(or primary monitor) using the PyAutoGUI library in Python.
            img = pyautogui.screenshot()
            #pyautogui: This is the PyAutoGUI library, which provides functions for automating tasks 
                        #related to mouse and keyboard interactions and screen capturing.
            #screenshot(): When called without any arguments, it captures a screenshot of the entire
                        #screen and returns it as an image object.
            #img: This is a variable that stores the captured screenshot as an image object. 

            #After executing img = pyautogui.screenshot(), the img variable contains the screenshot of 
            #the entire screen as an image. You can then manipulate, save, or process                                    
        except Exception as e:
            print(f"Error taking screenshot: {e}")
            l.logging.error(f"Error taking screenshot: {e}")
            break  # Exit the loop if an error occurs

        try:
            #This line converts the screenshot image (img) into a NumPy array. The np.array() function 
            #from the NumPy library is used for this conversion. This step allows you to work with the 
            #image as a NumPy array, which can be helpful for various image processing tasks.
            frame = np.array(img)
            
            #This line changes the color space of the image from BGR (Blue, Green, Red) to RGB using the
            #OpenCV library (cv2). In the BGR color space, pixel values are stored in the order Blue,Green,Red
            #while in the RGB color space, they are stored in the order Red, Green, Blue.
            #This conversion is often necessary when working with images in OpenCV because it uses 
            #the RGB color space by default.
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            #This line writes the processed frame to a video file. It is typically used when you are 
            #capturing a series of frames and want to save them as a video. The out variable represents 
            #a VideoWriter object created earlier, and it specifies the output video file format and settings.
            #The frame is added to the video file, effectively creating a video sequence frame by frame.
            out.write(frame)

        except Exception as e:
            print(f"Error processing and writing frame: {e}")
            l.logging.error(f"Error processing and writing frame: {e}")
            break  # Exit the loop if an error occurs

    print("Finished recording screen.")
    l.logging.info('Finished recording screen.')
    l.logging.info('Video File saved to integist_ecran_video')

    try:
        #This function closes all open OpenCV windows that were created during the course of your 
        #script's execution. OpenCV allows you to display images in windows, and this function is used to 
        #close those windows when you no longer need them. It's a good practice to call this function at 
        #the end of your script to ensure that any open windows are closed.
        cv2.destroyAllWindows()

        #This line releases the VideoWriter object represented by the variable out. A VideoWriter object 
        #is used to write video frames to an output file during video recording. When you're done recording 
        #and have added all the frames, you should release the VideoWriter object. Releasing it ensures 
        #that any buffered data is written to the output file, and the file is properly closed. Failing 
        #to release the VideoWriter object may result in an incomplete or corrupted video file.
        out.release()
    except Exception as e:
        print(f"Error releasing resources: {e}")
        l.logging.error(f"Error releasing resources: {e}")
