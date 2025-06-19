# A7 submission

- title: A7 submission

## question 1

Part 1.1

The fundamental frequency is about 100 to 240 Hz. There are about 40 harmonics, up to about 6000 Hz.

---

Part 1.2

- window type: Blackman \(balance between main lobe width and noise\)
- window size: 5292 samples \(6\*44100/50\)
- FFT size: 8192 samples \(larger than _M_\)
- magnitude threshold: −50 dB \(above the noise of the window function\)
- minimum duration of sinusoidal tracks: 0.1 s \(use the default\)
- maximum number of harmonics: 40 \(about 40 visible harmonics\)
- minimum fundamental frequency: 100 Hz \(by part 1.1\)
- maximum fundamental frequency: 240 Hz \(by part 1.1\)
- maximum error in f0 detection algorithm: 50 Hz \(by window size\)
- maximum frequency deviation in harmonic tracks: 0.01 Hz \(use the default\)
- stochastic approximation factor: 1 \(to reduce stochastic noise\)

---

Part 1.3

- file: [part 1.3.zip](part%201.3.zip)
  - source: [part 1.3/](part%201.3/)
    - original: [speech.wav](part%201.3/speech.wav)
    - harmonic: [speech-harmonic.wav](part%201.3/speech-harmonic.wav)
    - stochastic: [speech-reconstructed.wav](part%201.3/speech-reconstructed.wav)
    - reconstructed: [speech-reconstructed.wav](part%201.3/speech-reconstructed.wav)

## question 2

Part 2.1

Cello Section - spiccato - D5 \(spic_D4_v2_RR2.wav\) by sgossner -- <https://freesound.org/s/372807/> -- License: Creative Commons 0

---

Part 2.2

The fundamental frequency is about 550 to 650 Hz. There are about 40 visible harmonics, up to about 12000 Hz.

---

Part 2.3

- window type: Blackman \(balance between main lobe width and noise\)
- window size: 5292 samples \(6\*44100/50\)
- FFT size: 8192 samples \(larger than _M_\)
- magnitude threshold: −50 dB \(above the noise of the window function\)
- minimum duration of sinusoidal tracks: 0.1 s \(use the default\)
- maximum number of harmonics: 40 \(about 40 visible harmonics\)
- minimum fundamental frequency: 550 Hz \(by part 2.2\)
- maximum fundamental frequency: 650 Hz \(by part 2.2\)
- maximum error in f0 detection algorithm: 50 Hz \(by window size\)
- maximum frequency deviation in harmonic tracks: 0.01 Hz \(use the default\)
- stochastic approximation factor: 1 \(to reduce stochastic noise\)

---

Part 2.4

- file: [part 2.4.zip](part%202.4.zip)
  - source: [part 2.4/](part%202.4/)
    - unconverted: [a7p2-unconverted.wav](part%202.4/a7p2-unconverted.wav)
    - original: [a7p2.wav](part%202.4/a7p2.wav)
    - harmonic: [a7p2-harmonic.wav](part%202.4/a7p2-harmonic.wav)
    - stochastic: [a7p2-reconstructed.wav](part%202.4/a7p2-reconstructed.wav)
    - reconstructed: [a7p2-reconstructed.wav](part%202.4/a7p2-reconstructed.wav)
