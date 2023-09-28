
#asa merge cand rulez local
#import constants as c

#asa merge cand rulez din main.py
import Recording_Part.constants as c
import Recording_Part.fisier_logging as l

# =======  include audio  ================
import soundcard as sc
import soundfile as sf


#===================================================================
                # Record the screen audio
#==================================================================
OUTPUT_FILE_NAME = "integist_ecran_audio.wav"    # file name.
SAMPLE_RATE = 48000              # [Hz]. sampling rate, rata de eșantionare

# ========= Function to record audio from the microphone ============
def record_audio():
    try:
        print("Recording audio...")
        l.logging.info('Recording audio...')
        #configurarea microfonului; "include_loopback" -> it will capture both the input 
        #from the microphone and the audio playing through the default speaker(difuzor implicit).
        with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic:
            # record audio with loopback from default speaker
            data = mic.record(numframes=SAMPLE_RATE*c.record_seconds)
            
            #This line saves the recorded audio data to a file named OUTPUT_FILE_NAME in WAV format. 
            #It specifies the data to be written (data[:, 0] if you want to save it as a mono-channel audio) 
            #and the sampling rate for the saved audio.
            sf.write(file=OUTPUT_FILE_NAME, data=data[:, 0], samplerate=SAMPLE_RATE)

        print("Finished recording audio.")
        l.logging.info('Finished recording audio.')

    except Exception as e:
        # Handle exceptions
        print(f"An error occurred while recording audio: {str(e)}")
        l.logging.error(f"An error occurred while recording audio: {str(e)}")



