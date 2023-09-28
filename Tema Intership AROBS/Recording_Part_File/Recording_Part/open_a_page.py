
#===== asa merge cand rulez local ==== 
#import constants as c
#import fisier_logging as l

#=== asa merge cand rulez din main.py ====
import Recording_Part.fisier_logging as l

#====== open a page youtube ==========
import pywhatkit
import time


#///////////////////////////////////////////////////////////////////////////
        #open a page youtube
#////////////////////////////////////////////////////////////////////////
# This line creates an instance of the Microsoft Edge WebDriver. It initializes 
# a browser session that you can use to control the web browser programmatically.
#=====================================================================================
def open_a_page_youtube():
    try:
        print("Opening the youtube page")
        l.logging.info(f"Opening the youtube page")
        pywhatkit.playonyt("https://www.youtube.com/watch?v=LHvYrn3FAgI")
        print("The page was opened with success")
        l.logging.info('The page was opened with success')
        time.sleep(7)
    
    #If a TimeoutException occurs if the web page loading takes too long    
    except TimeoutException as timeout_exception:
        error_message = f"Timeout exception occurred: {timeout_exception}"
        l.logging.warning(error_message)
        l.logging.info("Web page opening timed out")

    except Exception as e:
        l.logging.error(f'ERROR: The page could not opened: {e}')
        print(f'ERROR: The page could not opened: {e}')
        sys.exit(1)  # Exit the program with a non-zero status code to indicate an error
#=====================================================================================


#def main():
#	open_a_page_youtube()

#if __name__ == "__main__":
#    main()