import sounddevice as sd
import wavio
def record_audio(duration, filename):
    print("Recording audio...")
    audio_data = sd.rec(int(duration * 44100), samplerate=44100, channels=2, dtype='int16')
    sd.wait()
    wavio.write(filename, audio_data, 44100, sampwidth=2)

def play_audio(filename):
    print("Playing audio...")
    audio_data = wavio.read(filename).data
    sd.play(audio_data, samplerate=44100)
    sd.wait()

duration = int(input("Enter recording duration in seconds: "))
filename = input("Enter filename to save recorded audio (without extension): ") + ".wav"
    
record_audio(duration, filename)
print("Audio recording saved as:", filename)
