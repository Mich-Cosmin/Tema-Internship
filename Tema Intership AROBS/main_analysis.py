
from Analysis_Part.Sound_Level import calculate_spl
from Analysis_Part.Audio_Analysis import calc_audio_analysis


def main():
    # Example usage:
    audio_file = 'Recording_Part_File/integist_ecran_audio.wav'  # Replace with the path to your audio file
    output_file = 'output_spl_data.csv'  # Replace with the desired output CSV file path
    
    #======== calcul SPL[dB] ========
    calculate_spl(audio_file, output_file)
    
    #======= analiza sunetului =========
    calc_audio_analysis(audio_file)



if __name__ == "__main__":
    main()


