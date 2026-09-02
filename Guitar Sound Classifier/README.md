# Guitar Sound Classifier

Binary classifier that distinguishes acoustic vs electric guitar sounds using audio spectrograms and a convolutional neural network.

## Overview

This project transforms guitar audio (.wav files) into 3-channel "images" by stacking:
1. **Spectrogram** (STFT magnitude)
2. **Mel Spectrogram** (mel-filtered frequency representation)
3. **MFCC** (Mel-Frequency Cepstral Coefficients)

These 3 features form an RGB-like image that is classified by a small CNN.

![Data representation](Data%20Image.png)

## Architecture

**CNN Model:**
- Conv2D layer: 3 → 64 channels (3×3 kernel)
- LeakyReLU + MaxPool2D (2×2)
- Conv2D layer: 64 → 128 channels (3×3 kernel)
- LeakyReLU + MaxPool2D (2×2)
- Fully connected: 128 nodes → 32 nodes
- Output layer: 2 classes (acoustic, electric)

**Training:**
- Framework: PyTorch
- Loss: CrossEntropyLoss
- Optimizer: Adam (lr=1e-3)
- 50 epochs

![Validation Accuracy](Validation%20Accuracy.png)

## Tech Stack

- **Python** with PyTorch
- **torchaudio** for audio processing
- **Feature extraction:** STFT, Mel Spectrogram, MFCC
- **Architecture:** 2 convolutional layers + fully connected layers
- **Dataset:** 12,600 guitar audio clips (~0.29 seconds each, standardized duration)

## Dataset Requirements

The code expects .wav files in the following structure:
```
Data/
├── acoustic_note_1.wav
├── acoustic_note_2.wav
├── ...
├── acoustic_note_6300.wav
├── note_1.wav (electric)
├── note_2.wav (electric)
├── ...
└── note_6300.wav (electric)
```

**Audio specifications:**
- Format: .wav
- Duration: ~0.29 seconds (shorter clips are looped/padded)
- Sample rate: any (automatically handled)
- Clips should contain single guitar notes or chords

## How to Run

### 1. Prepare Your Dataset
Create a `Data/` folder with your .wav files following the naming convention above, or modify the file paths in `main.py` (lines 86-87):
```python
acoustic_note_paths = ['path/to/your/acoustic_note_{}.wav'.format(n) for n in range(1, N)]
electric_note_paths = ['path/to/your/note_{}.wav'.format(n) for n in range(1, N)]
```

### 2. Install Dependencies
```bash
pip install torch torchaudio scikit-learn
```

### 3. Run Training
```bash
python main.py
```

The script will:
- Load and preprocess audio files
- Extract spectrograms, mel spectrograms, and MFCC features
- Train the CNN for 50 epochs
- Print training loss, validation loss, and validation accuracy per epoch

## Notes

- **First deep learning project:** Built in 24 hours with ChatGPT assistance as a first attempt with PyTorch
- **Binary classification:** Model architecture is suitable for any binary audio classification task
- **Improvements possible:** As noted in the original README, there's room for optimization (data augmentation, hyperparameter tuning, deeper architectures)
- **Dataset not included:** Large audio dataset is not in this repository due to size constraints

## Original Repository

Source: [MaximoAPS/guitar_sound_classifier](https://github.com/MaximoAPS/guitar_sound_classifier)
