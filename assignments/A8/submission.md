# A9 submission

- title: A8 submission

## question 1

I want to increase the speech pitch naturally.

- model: harmonic plus stochastic
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
- frequency scaling factors
  - 0 s: 2
  - 5 s: 2
- frequency stretching factors
  - 0 s: 1
  - 5 s: 1
- timbre preservation: 1
- time scaling factors
  - 0 s: 0 s
  - 5 s: 5 s

---

- file: [part 1.zip](part%201.zip)
  - source: [part 1/](part%201/)
    - original: [speech.wav](part%201/speech.wav)
    - transformed: [speech-transformed-1.wav](part%201/speech-transformed-1.wav)

## question 2

Cello Section - spiccato - D5 \(spic_D4_v2_RR2.wav\) by sgossner -- <https://freesound.org/s/372807/> -- License: Creative Commons 0

I want to make some strange sound that is very different from the original.

- model: harmonic plus stochastic
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
- frequency scaling factors
  - 0 s: 4
  - 5 s: 1
- frequency stretching factors
  - 0 s: 1
  - 5 s: 4
- timbre preservation: 1
- time scaling factors
  - 0 s: 0 s
  - 5 s: 20 s

---

- file: [part 2.zip](part%202.zip)
  - source: [part 2/](part%202/)
    - unconverted: [a8p2-unconverted.wav](part%202/a8p2-unconverted.wav)
    - original: [a8p2.wav](part%202/a8p2.wav)
    - transformed: [a8p2-transformed-1.wav](part%202/a8p2-transformed-1.wav)
