import numpy as np
import scipy.io.wavfile as wavfile
import soundfile as sf
import math
import matplotlib.pyplot as plt
import csv

import Analysis_Part.fisier_logging as l

#def calculate_spl(audio_file, output_file, window_size=0.01, overlap=0.5, reference_pressure=20e-6):
def calculate_spl(audio_file, output_file, window_size=0.01, overlap=0.5, reference_pressure=32767):
    try:
        """
        Calculate Sound Pressure Level (SPL) in decibels (dB) from an audio file,
        plot it over time, and save the results to a CSV file.

        :param audio_file: Path to the audio file.
        :param output_file: Path to the output CSV file.
        :param window_size: Size of the analysis window in seconds. Default is 0.01 seconds.
        :param overlap(suprapune): Overlap between successive windows as a fraction of the window size. 
                                    Default is 0.5 (50% overlap).
        :param reference_pressure: Reference sound pressure in pascals (Pa). Default is 20e-6 Pa.
        """
        l.logging.info("Starting SPL calculation.")

        # Read the audio file using soundfile to handle various formats
        audio, sample_rate = sf.read(audio_file)
        #print('SPL Sampling Rate:',audio)                      #48000
        #print('SPL Audio Shape:',np.shape(sample_rate))        #1440000
        
        # Calculate the number of samples in the analysis window
        window_samples = int(window_size * sample_rate)
        
        # Calculate the number of overlapping samples (esntioane suprapuse)
        #este o tehnică folosită pentru a îmbunătăți calitatea și precizia analizei semnalelor,
        #prin atenuarea tranzițiilor între segmente, conservarea informației și îmbunătățirea rezoluției. 
        overlap_samples = int(overlap * window_samples)   #220
        
        # Initialize lists to store SPL values and time indices
        spl_values = []
        time_indices = []
        
        # Iterate through the audio signal with overlapping windows
        start = 0
        while start < len(audio):               #len(audio) = 1321984
            end = start + window_samples        #0+441; 221+441=662
            if end > len(audio):
                end = len(audio)   #1321984, final
            
            # Extract the current window of audio
            window = audio[start:end]
            
            # Calculate the root mean square (RMS) of the window
            rms = np.sqrt(np.mean(window**2))

            # Calculate SPL using the formula
            if reference_pressure <= 0:
                raise ValueError("Reference pressure must be greater than zero.")
            
            # Calculate SPL using the formula
            spl = 20 * math.log10(rms / reference_pressure)
            
            # Append(adauga) SPL value and time index to lists
            spl_values.append(spl)                      #val calc o pun in vector la final
            time_indices.append(start / sample_rate)
            
            # Move to the next window with overlap
            #window_samples=441
            #overlap_samples=220
            start += window_samples - overlap_samples   #pasul, 0; 441-220=221; 442; 663
        
        # Plot the SPL over time
        plt.figure(figsize=(12, 6))
        plt.plot(time_indices, spl_values, color='b')
        plt.xlabel('Time (s)')
        plt.ylabel('SPL (dB)')
        plt.title('Sound Pressure Level (SPL) Over Time')
        plt.grid(True)
        
        # Save the SPL values and time indices to a CSV file, sau excel
        with open(output_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            #writer.writerow(['Time (s)', 'SPL (dB)'])
            writer.writerow(['SPL (dB)'])
            for t, spl in zip(time_indices, spl_values):
                #writer.writerow([t, spl])
                writer.writerow([spl])
        
        # Save the plot as an image file (optional)
        plot_image_file = output_file.replace('.csv', '.png')  #excel file
        plt.savefig(plot_image_file)
        l.logging.info("SPL calculation completed successfully.")
        #plt.show()  

    except FileNotFoundError as e:
        # Log: File not found error
        l.logging.error(f"Error: {str(e)}")
        print(f"Error: The file '{audio_file}' was not found.")
    except Exception as e:
        # Log: Other errors
        l.logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")
    

    