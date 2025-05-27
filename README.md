# mystt

**mystt** is a simple speech-to-text project that recognizes a single spoken word from the microphone and converts it to text using an XGBoost classifier.

## Features

- Records 2 seconds of audio from the user's microphone.
- Extracts MFCC (Mel Frequency Cepstral Coefficients) features from the recorded audio.
- Uses a pre-trained XGBoost classifier (`model.pkl`) to predict which word was spoken.
- Outputs the recognized word as text.

## Project Structure

```
mystt/
├── model.pkl          # Pre-trained XGBoost classifier (required for prediction)
├── main.py            # Main script: records audio, extracts features, runs prediction
├── requirements.txt   # Required Python packages
└── README.md          # This file
```

## How It Works

1. **Audio Recording:**  
   The program captures audio from the microphone for a fixed duration (e.g., 2 seconds).

2. **Feature Extraction:**  
   The recorded audio is saved as a WAV file. The MFCC features (typically 13 coefficients) are extracted using the `librosa` library.

3. **Classification:**  
   The MFCC features are flattened and passed to the XGBoost model loaded from `model.pkl`. The model predicts which word was spoken.

4. **Output:**  
   The predicted word is printed to the console.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Kitler174/mystt.git
   cd mystt
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Required packages include:
   - `pyaudio`
   - `librosa`
   - `xgboost`
   - `scikit-learn`
   - `numpy`

   > You may need to install system dependencies for `pyaudio` (e.g., `portaudio`).

3. **Download or train the XGBoost model:**
   Place the pre-trained `model.pkl` file in the root directory of the project.

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. When prompted, press Enter and say a single word clearly into your microphone.

3. The recognized word will be displayed as the prediction.

## Example

```
Press Enter to start recording for 2 seconds...
[say your word]
Prediction: ['cat']
```

## Notes

- The XGBoost model (`model.pkl`) must be trained in advance to recognize the specific set of words you want to detect.
- The program is designed to recognize only **one word at a time** per recording.
- Audio quality and environment will affect recognition accuracy.

## License

MIT License
