import pyaudio
import sqlite3
import librosa
import wave

conn = sqlite3.connect('baza.sqlite3')
cursor = conn.cursor()
def insert_data(data_tuple):
    cursor.execute("INSERT INTO dane (data3, key) VALUES (?, ?)",
                   data_tuple)
    conn.commit()

def train_data(a):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt32, channels=1, rate=44100, input=True, start=False)
    input("Naciśnij aby zacząć nagrywać przez 2 sekundy")
    recorded_data = []
    stream.start_stream()
    for i in range(int(44100 / 1024 * 2)):
        print(i)
        data = stream.read(1024)
        recorded_data.append(data)
    stream.stop_stream()
    stream.close()
    p.terminate()
    audio_data = b"".join(recorded_data)
    wf = wave.open("output/granie.wav", "wb")
    wf.setnchannels(1)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt32))
    wf.setframerate(44100)
    wf.writeframes(audio_data)
    wf.close()
    y, sr = librosa.load("output/granie.wav")
    mfccc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13).tolist()
    dddd=[]
    for i in mfccc:
        for p in i:
            dddd.append(p)
    dataa = (str(dddd), a)
    insert_data(dataa)
if __name__ == "__main__":
    a = input("key>")
    while True:
        train_data(a)