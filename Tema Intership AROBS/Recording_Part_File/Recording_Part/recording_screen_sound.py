
#asa merge cand rulez local
#import constants as c
#import fisier_logging as l

#asa merge cand rulez din main.py
import Recording_Part.constants as c
import Recording_Part.fisier_logging as l

# =======  include audio  ================
import pyaudio
import wave


def record_audio():
    l.logging.info(f"The microphone Device You chose is : {c.selected_device}")
    CHUNK=1024
    CHANNELS=1
    FORMAT=pyaudio.paInt16
    RATE=44100
    output_filename = "integist_ecran_audio.wav"  # Change this to the desired output filename
    
    #p = pyaudio.PyAudio()
    #creează o instanță a clasei PyAudio din modulul pyaudio. Această instanță este folosită pentru a 
    #accesa funcționalitatea oferită de PyAudio, este o bibliotecă Python pentru manipularea audio, 
    #inclusiv pentru înregistrarea și redarea sunetului.
    try:
        p = pyaudio.PyAudio()
    except Exception as e:
        print(f"Error: Instanta clasei [PyAudio] nu a putut fi creata : {e}")
        l.logging.error(f"Error: Instanta clasei [PyAudio] nu a putut fi creata : {e}")
        return

    try:
        #"p": - instance of the pyaudio.PyAudio
        #opens an audio input stream(curent) for recording with the specified format, channel 
        #configuration, sample rate, and input device. Once the stream is opened, you can use it to read 
        #audio data from the selected input device during the recording process.
        stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True,
            input_device_index=c.selected_device, frames_per_buffer=CHUNK)
    except Exception as e:
        print(f"Error opening audio stream: {e}")
        l.logging.error(f"Error opening audio stream: {e}")
        
        # Handle the error appropriately, e.g., exit the program or log it
        return


    print("Start Recording audio")
    l.logging.info("Start Recording audio")
    frames = []

    for _ in range(0, int(RATE / CHUNK * c.record_seconds)):
        try:
            #read audio data from an audio stream, represented by the stream variable.
            data = stream.read(CHUNK)
        except Exception as e:
            print(f"Error reading audio data: {e}")
            l.logging.error(f"Error reading audio data: {e}")
            # Handle the error appropriately, e.g., exit the loop or log it
            break

        #collect and store audio data in a list called frames.
        #frames: a Python list that serves as a container for storing audio data. It is typically 
                 #used to accumulate audio data in chunks as it is read from an audio stream.
        #append(data): This is a method call on the frames list. It adds the data variable (which contains 
                #audio data read from an audio stream) to the end of the list. In other words, it appends 
                #the audio data to the list.
        #In the context of audio recording, this line is often found inside a loop where audio data is 
        #continuously read from the audio stream in chunks (typically specified by a buffer size) and 
        #appended to the frames list. This is a common approach for recording audio because it allows you 
        #to collect and concatenate audio data into a continuous stream, which can later be saved as an 
        #audio file or processed as needed.
        frames.append(data)

    print("Finished recording audio.")
    l.logging.info("Finished recording audio.")

    # Save the recorded audio to a WAV file
    try:
        with wave.open(output_filename, 'wb') as wf:
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

        print(f"Audio file saved to {output_filename}")
        l.logging.info(f"Audio saved to {output_filename}")

    except Exception as e:
        print(f"Error saving audio to {output_filename}: {e}")
        l.logging.error(f"Error saving audio to {output_filename}: {e}")
        # Handle the error appropriately, e.g., exit the program or log it


    
