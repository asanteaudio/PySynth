#PySynth! v0.1.0

import numpy as np
import sounddevice as sd

def main ():
    # Ask for desired sound from user.

    print("Please select a sound from the following:\n1 for noise.\n2 for sine.")

    sound = input()

    if sound == "1":
        playsound = noise()
        sd.play(playsound)
        sd.wait()
    elif sound == "2":
        playsound = sine_tone()
        sd.play(playsound)
        sd.wait()

def noise(duration: float=1.0, amplitude: float=0.25, samplerate: int=44100) -> np.ndarray:
    #Genrate white noise

    #Calculate the nnumber of samples needed for set duration. Must be a whole number hence cast to int
    n_samples = int(duration * samplerate)

    #Represent white noise digitally, within -1 and 1 to prevent distortion.
    noise = np.random.uniform(-1, 1, n_samples)

    #Scale spltitude of samples in noise array
    noise *= amplitude
    return noise

def sine_tone(duration: float=1.0, amplitude: float=0.25, samplerate: int=44100, frequency: int=440) -> np.ndarray:
    #Generate a sine wave.

    #Calculate samples required
    n_samples = int(duration * samplerate)

    #Create array of time points
    time_points = np.linspace(0, duration, n_samples, False)

    #Generate the sine wave.
    sine = np.sin(2 * np.pi * frequency * time_points)

    sine *= amplitude
    return sine

main()