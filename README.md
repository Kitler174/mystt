# mystt

**mystt** is an AI-based project that recognizes a single spoken word from the microphone and converts it to text using an XGBoost classifier. The project consists of three main Python scripts: `learn.py`, `model.py`, and `test.py`.

## Project Structure

```
.
├── learn.py           # Data acquisition: records audio, extracts MFCCs, saves to SQLite
├── model.py           # Model training: trains XGBoost classifier from SQLite data and saves model
├── test.py            # Model testing: records audio, extracts MFCCs, predicts using trained model
├── baza.sqlite3       # SQLite database with training data (created by learn.py)
├── model.pkl          # Trained XGBoost model (created by model.py)
├── nagranie.wav       # Temporary audio file for testing
├── output/            # Directory for training audio files
│   └── granie.wav     # Temporary audio file for training
├── README.md          # This file
```

## How It Works

### 1. Data Collection (`learn.py`)

- Records 2 seconds of audio from the microphone.
- Extracts MFCC (Mel Frequency Cepstral Coefficients) features using `librosa`.
- Stores the MFCC feature vector and a label (the word number) in a local SQLite database (`baza.sqlite3`).
- `insert_data(data_tuple)` inserts the features and label.
- `train_data(a)` handles recording, feature extraction, and storage.
- Usage:  
  ```
  python learn.py
  # Enter the label (number representing the word), then follow the prompts to record samples.
  ```

### 2. Model Training (`model.py`)

- Loads data from the SQLite database (`baza.sqlite3`).
- Trains an XGBoost classifier (`XGBClassifier`) using the MFCC features and their labels.
- Saves the trained model to `model.pkl` using `pickle`.
- Usage:
  ```
  python model.py
  # Trains and saves the model.
  ```

### 3. Model Testing (`test.py`)

- Loads the trained model from `model.pkl`.
- Records 2 seconds of audio from the microphone.
- Extracts MFCC features from the recording.
- Predicts the label (word number) using the trained model and prints the result.
- Usage:
  ```
  python test.py
  # Follow the prompt to record a word and see the predicted label.
  ```

## Required Libraries

- `librosa` (`pip install librosa`)
- `pyaudio` (`pip install pyaudio`)
- `wave` (standard with Python)
- `sqlite3` (standard with Python)
- `xgboost` (`pip install xgboost`)
- `scikit-learn` (`pip install scikit-learn`)
- `pickle` (standard with Python)

## Notes

- All scripts are run independently — there is no `main.py`.
- The workflow is:  
  1. Collect data with `learn.py`  
  2. Train the model with `model.py`  
  3. Test recognition with `test.py`
- The model only recognizes **single words** and expects the training and testing audio to be similar in format.
- Labels used during data collection should be consistent (e.g., 0 for "yes", 1 for "no", etc.).

## Additional Information

For more details or questions, contact the author via Discord: `. _.kitler._.`
