#PySynth! v0.1.0

import numpy as np
import sounddevice as sd

def sine_tone (frequency = 440, duration = 1.0, sample_rate = 44100):
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    return 0.5 * np.sin(2 * np.pi * frequency * t)

def play_tone(tone, sample_rate = 44100):
    sd.play(tone, samplerate=sample_rate)
    sd.wait()