import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import signal
from pydub import AudioSegment

import Analysis_Part.fisier_logging as l


def calc_audio_analysis(audio_file):
    try:
        l.logging.info("Starting audio analysis.")
        
        # Check if the audio file exists, Import the .wav audio
        s,a = wavfile.read(audio_file)
        #s = sampling (int) / esantionare
             #Rata de eșantionare reprezintă numărul de eșantioane luate pe secundă din semnalul audio. 
             #Aceasta este importantă pentru a interpreta corect semnalul audio în timp.
        #a = audio signal (numpy array)
             #Această variabilă primește semnalul audio sub formă de numpy array. Semnalul audio constă într-o 
             #secvență de valori numerice care reprezintă amplitudinea semnalului la fiecare eșantion. 
             #În acest array, fiecare element corespunde unui eșantion de timp din semnal.
        print('Sampling Rate:',s)               #48000
        print('Audio Shape:',np.shape(a))       #1439744

        # ==================== display Original Sound ======================
        #Display the magnitude of the sound
        #number of samples, atribui variabilei na valoarea numărului de elemente din primua linie
        na = a.shape[0]          
        #print('na = ',na)       #1439744
        #audio time duration
        la = na / s   
        #print('la = ',la)       #30.0

        #plot signal versus time
        t = np.linspace(0,la,na)
        plt.plot(t,a,'k-',color='purple')
        plt.xlabel('Time (s)')
        plt.savefig('plot_signal_vs_time.png')
        l.logging.info("The original sound was plotted and saved.")
        #plt.show()


        # ==================== Frequency Analysis ======================
        #Fast Fourier Transform (FFT), analyze entire audio clip
        na = len(a)         #1321984
        
        #FFT asupra semnalului audio 
        #Then selects the first half of the FFT results (0 to na/2) because the FFT of real-valued signals 
        #is symmetric, and the second half is redundant. To ensure that the amplitude values are correctly scaled, 
        #it divides the FFT result by "na". The result, stored in a_k, represents the complex spectrum of the audio signal.
        a_k = np.fft.fft(a)[0:int(na/2)]/na # FFT function from numpy
        
        #This line doubles the amplitude values of all elements in a_k except for the DC component at index 0. 
        #This adjustment is made because when you calculate the one-sided spectrum from a real-valued signal, 
        #you lose half of the energy in the negative frequencies. By doubling the values, you account for this loss 
        #of energy and create a correct one-sided spectrum.
        a_k[1:] = 2*a_k[1:] # single-sided spectrum only
        
        #Pxx = np.abs(a_k): Here, the absolute values of the complex elements in a_k are computed, effectively 
        #removing the imaginary part. Pxx now contains the one-sided amplitude spectrum of the audio signal.
        Pxx = np.abs(a_k)   # remove imaginary part

        #This line generates a frequency vector f that corresponds to the one-sided amplitude spectrum. 
        #It is computed using the sampling rate s and covers frequencies from 0 Hz to half the Nyquist frequency.
        f = s*np.arange((na/2))/na # frequency vector

        #plotting
        fig,ax = plt.subplots()
        plt.plot(f,Pxx,'b-',label='Audio Signal')

        #***************** Subplot zona in care urechea aude sunetul ****************************
        #[20, 20000] -Hz represents the x-values, indicating the frequency range.
        #[0.1, 0.1] represents the y-values, create a horizontal line at a constant value of 0.1 on the y-axis.
        #alpha=0.7 sets the transparency of the line to 0.7 (making it somewhat transparent).
        #label='Audible (Humans)' is used to label this line in the plot.
        plt.plot([20,20000],[0.1,0.1],'r-',alpha=0.7,\
                 linewidth=10,label='Audible (Humans)')
        ax.set_xscale('log'); ax.set_yscale('log')
        plt.grid(); plt.legend()
        plt.ylabel('Amplitude')
        plt.xlabel('Frequency (Hz)')
        plt.savefig('Amp_vs_Freq.png')
        #plt.show()
        l.logging.info("The Amplitude vs Frequency (Hz) was plotted and saved.")


        #===================== Spectrogram =========================
        #fr: An array of frequencies.
        #tm: An array of time intervals.
        #spgram: The spectrogram, which is a 2D array representing the time-frequency content of the audio signal.
        fr, tm, spgram = signal.spectrogram(a,s)
        lspg = np.log(spgram)
        plt.figure(figsize=(6,5)) #??????????????????????????????????????
        #x,y, lspg is the data that will be color-mapped onto the plot.
        #shading='auto' is used to automatically determine the shading of the pseudocolor plot.
        plt.pcolormesh(tm,fr,lspg,shading='auto')
        plt.ylabel('Frequency (Hz)')
        plt.xlabel('Time (sec)')
        plt.savefig('Spectrogram.png')
        #plt.show()
        l.logging.info("The Spectrogram was plotted and saved.")
    
    except FileNotFoundError as e:
        # Log: File not found error
        l.logging.error(f"Error: {str(e)}")
        print(f"Error: The file '{audio_file}' was not found.")
    except Exception as e:
        # Log: Other errors
        l.logging.error(f"An error occurred: {str(e)}")
        print(f"An error occurred: {str(e)}")


