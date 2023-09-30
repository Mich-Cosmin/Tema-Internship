
import Recording_Part.fisier_logging as l
import pyaudio

def list_audio_input_sources():
    #"pyaudio.PyAudio()" -> creează o instanță a clasei PyAudio din modulul pyaudio. Această instanță 
    #este folosită pentru a accesa funcționalitatea oferită de PyAudio, este o bibliotecă Python 
    #pentru manipularea audio, inclusiv pentru înregistrarea și redarea sunetului.
    try:
        p = pyaudio.PyAudio()
    except Exception as e:
        print("Nu sa putut afla numarul de microfoane !.")
        print(f"Error : Instanta clasei [PyAudio] nu a putut fi creata : {e}")
        l.logging.error(f"Error: Instanta clasei [PyAudio] nu a putut fi creata : {e}")
        return  # iese de aici si continua mai departe

    try:
        #retrieves information about the audio host API (Audio Processing Interface) at index 0
        #"p" instanta ca in struct
        info = p.get_host_api_info_by_index(0)
    except Exception as e:
        print(f"Error getting host API info: {e}")
        l.logging.error(f"Error getting host API info: {e}")
        p.terminate()   #close the PyAudio instance represented
        return

    try:
        #retrieves the number of audio input and output devices
        num_devices = info.get('deviceCount')
    except Exception as e:
        print(f"Error getting device count: {e}")
        l.logging.error(f"Error getting device count: {e}")
        p.terminate()
        return

    print("Available audio input sources:")
    for i in range(num_devices):
        try:
            device_info = p.get_device_info_by_host_api_device_index(0, i)
        except Exception as e:
            print(f"Error getting device info for Device {i}: {e}")
            l.logging.error(f"Error getting device info for Device {i}: {e}")
            continue

        #"device_info": This is a dictionary that contains information about a specific audio input or output
                #device. This information was retrieved using p.get_device_info_by_host_api_device_index(0, i)
        #"get('maxInputChannels')": This is a method used to access a specific property of the device_info 
                #dictionary. It retrieves the value associated with the key 'maxInputChannels'. This key 
                #typically stores the maximum number of input (recording) 
        #"if device_info.get('maxInputChannels') > 0":: This is an if statement that checks if the value 
                #associated with 'maxInputChannels' is greater than 0.
                #it checks if the audio input device supports at least one input channel.

        if device_info.get('maxInputChannels') > 0:
            try:
                print(f"Device {i}: {device_info['name']}")
                l.logging.info(f"Device {i}: {device_info['name']}")
            except Exception as e:
                print(f"Error printing device info: {e}")
                l.logging.error(f"Error printing device info: {e}")

    try:
        p.terminate()   #close the PyAudio instance
    except Exception as e:
        print(f"Error terminating PyAudio: {e}")
        l.logging.error(f"Error terminating PyAudio: {e}")


'''
def main():
    list_audio_input_sources()


if __name__ == "__main__":
    main()

'''