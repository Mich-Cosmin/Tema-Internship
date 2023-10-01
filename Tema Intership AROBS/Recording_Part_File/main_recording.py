

import threading

#deschid pagina youtube, import totul
from Recording_Part.open_a_page import open_a_page_youtube
#inregistrez sunetul ecranului 
from Recording_Part.recording_screen_sound import record_audio
#===================================

#inregistrez video ecran
from Recording_Part.recording_screen_video import record_video

#pentru a calcula nr de microfoane
from Recording_Part.list_microphone_input import list_audio_input_sources
import Recording_Part.fisier_logging as l
#*******************************************************************************


def main():
    l.logger.info("Application started.")  
    l.logger.info('')  # Insert a blank line
    
    print("========= Start Subrutina de deschidere pagina youtube =========")
    l.logger.info("========= Start Subrutina de deschidere pagina youtube =========")
    open_a_page_youtube()  ## ==== Open a page on youtube =====
    print("========= Final Subrutina de deschidere pagina youtube =========")
    l.logger.info("========= Final Subrutina de deschidere pagina youtube =========")
    l.logger.info('')  # Insert a blank line

    # verific numarul de microfoane
    print("\n========= Start Subrutina de numarare a numarului de microfoane =========")
    l.logger.info("========= Start Subrutina de numarare a numarului de microfoane =========")
    list_audio_input_sources()
    print("========= Final Subrutina de numarare a numarului de microfoane =========")
    l.logger.info("========= Final Subrutina de numarare a numarului de microfoane =========")
    l.logger.info('')  # Insert a blank line
    #===================================================================  
                #include threading, fac alt fir pentru audio
    #===================================================================
    #the code is setting up 2 threads to perform concurrent tasks: 
    # --> recording audio, recording video
    #Using threads allows these tasks to run in parallel, which can be useful 
    #for multitasking or improving the program's responsiveness.
    video_thread = threading.Thread(target=record_video)  
    audio_thread = threading.Thread(target=record_audio) 
    
    print("\n========= Start Thread audio + video =========")
    l.logger.info("========= Start Thread audio + video =========")
    video_thread.start()
    audio_thread.start()

    #==============================================================================
    #aștepta terminarea execuției thread-ului se folosește metoda join()
    video_thread.join()
    audio_thread.join()
    print("\n========= Final Thread audio + video =========")
    l.logger.info("========= Final Thread audio + video =========")
    #===============================================================================


if __name__ == "__main__":
    main()


