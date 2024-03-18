import pickle
import pyaudio
import librosa
import wave

with open("model.pkl", "rb") as f:
     model3 = pickle.load(f)

def test():
  p = pyaudio.PyAudio()
  stream = p.open(format=pyaudio.paInt32, channels=1, rate=44100, input=True, start=False)
  input("Naciśnij Enter, aby zacząć nagrywać przez 2 sekundy...")
  recorded_data = []
  stream.start_stream()
  for _ in range(int(2 * 44100 / 1024)):
    data = stream.read(1024)
    recorded_data.append(data)
  stream.stop_stream()
  stream.close()
  audio_data = b"".join(recorded_data)
  wf = wave.open("nagranie.wav", "wb")
  wf.setnchannels(1)
  wf.setsampwidth(p.get_sample_size(pyaudio.paInt32))
  wf.setframerate(44100)
  wf.writeframes(audio_data)
  wf.close()
  y, sr = librosa.load("nagranie.wav")
  mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13).tolist()
  ddd = []
  for i in mfcc:
    for p in i:
      ddd.append(p)
  prediction = model3.predict([ddd])
  print(f"Predykcja: {prediction}")

if __name__ == "__main__":
     test()