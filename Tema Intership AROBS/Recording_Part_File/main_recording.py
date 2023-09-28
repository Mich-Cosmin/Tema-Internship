
import threading

#deschid pagina youtube, import totul
from Recording_Part.open_a_page import open_a_page_youtube
#inregistrez sunetul ecranului 
from Recording_Part.recording_screen_sound import record_audio
#inregistrez video ecran
from Recording_Part.recording_screen_video import record_video


import Recording_Part.fisier_logging as l



def main():
	l.logger.info("Application started.")

	open_a_page_youtube() 

	#===================================================================  
	            #include threading, fac alt fir pentru audio
	#===================================================================
	#the code is setting up three threads to perform concurrent tasks: 
	# --> recording audio, recording video
	#Using threads allows these tasks to run in parallel, which can be useful 
	#for multitasking or improving the program's responsiveness.
	audio_thread = threading.Thread(target=record_audio)
	video_thread = threading.Thread(target=record_video)  # ????????????????????????
	#page_open_thread = threading.Thread(target=open_a_page_youtube)  # ????????????????????????

	audio_thread.start()
	video_thread.start()
	#page_open_thread.start()
	#==========================================================


	#===============================================================================
	#aștepta terminarea execuției thread-ului se folosește metoda join()
	# Wait for the audio recording thread to finish
	audio_thread.join()
	video_thread.join()
	#page_open_thread.join()
	#===============================================================================


if __name__ == "__main__":
    main()