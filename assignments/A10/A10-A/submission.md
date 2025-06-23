# A10-A submission

- title: A10-A submission

## question 1

Having seen that the below sound is transformed into something like airplane in assignment A8:

- Cello Section - spiccato - D5 \(spic_D4_v2_RR2.wav\) by sgossner -- <https://freesound.org/s/372807/> -- License: Creative Commons 0

I want to try to make as many variants of the below sound and join them together randomly to make airplane sounds.

---

Variation 1: Seems like a plane crashing?

- model: harmonic plus stochastic
- window type: Blackman
- window size: 5292 samples
- FFT size: 8192 samples
- magnitude threshold: −70 dB
- minimum duration of sinusoidal tracks: 0.1 s
- maximum number of harmonics: 40
- minimum fundamental frequency: 550 Hz
- maximum fundamental frequency: 650 Hz
- maximum error in f0 detection algorithm: 7 Hz
- maximum frequency deviation in harmonic tracks: 0.01 Hz
- stochastic approximation factor: 1
- frequency scaling factors
  - 0 s: 4
  - 5 s: 1
- frequency stretching factors
  - 0 s: 1
  - 5 s: 4
- timbre preservation: 1
- time scaling factors
  - 0 s: 0 s
  - 1 s: 4 s

---

Variation 2: Interesting ascending sound...

- model: harmonic plus stochastic
- window type: Blackman
- window size: 5292 samples
- FFT size: 8192 samples
- magnitude threshold: −70 dB
- minimum duration of sinusoidal tracks: 0.1 s
- maximum number of harmonics: 40
- minimum fundamental frequency: 550 Hz
- maximum fundamental frequency: 650 Hz
- maximum error in f0 detection algorithm: 7 Hz
- maximum frequency deviation in harmonic tracks: 0.01 Hz
- stochastic approximation factor: 1
- frequency scaling factors
  - 0 s: 1
  - 5 s: 4
- frequency stretching factors
  - 0 s: 4
  - 5 s: 1
- timbre preservation: 1
- time scaling factors
  - 0 s: 0 s
  - 1 s: 4 s

---

Variation 3: Generic airplane noise.

- model: harmonic plus stochastic
- window type: Blackman
- window size: 5292 samples
- FFT size: 8192 samples
- magnitude threshold: −40 dB
- minimum duration of sinusoidal tracks: 0.1 s
- maximum number of harmonics: 40
- minimum fundamental frequency: 550 Hz
- maximum fundamental frequency: 650 Hz
- maximum error in f0 detection algorithm: 7 Hz
- maximum frequency deviation in harmonic tracks: 0.01 Hz
- stochastic approximation factor: 1
- frequency scaling factors
  - 0 s: 1
  - 5 s: 4
- frequency stretching factors
  - 0 s: 4
  - 5 s: 1
- timbre preservation: 1
- time scaling factors
  - 0 s: 0 s
  - 1 s: 4 s

---

Variation 4: Ascend and then descend.

- model: harmonic plus stochastic
- window type: Blackman
- window size: 5292 samples
- FFT size: 8192 samples
- magnitude threshold: −70 dB
- minimum duration of sinusoidal tracks: 0.1 s
- maximum number of harmonics: 40
- minimum fundamental frequency: 550 Hz
- maximum fundamental frequency: 650 Hz
- maximum error in f0 detection algorithm: 7 Hz
- maximum frequency deviation in harmonic tracks: 0.01 Hz
- stochastic approximation factor: 1
- frequency scaling factors
  - 0 s: 1
  - 1 s: 4
  - 2 s: 1
  - 3 s: 4
  - 4 s: 1
  - 5 s: 4
- frequency stretching factors
  - 0 s: 4
  - 1 s: 1
  - 2 s: 4
  - 3 s: 1
  - 4 s: 4
  - 5 s: 1
- timbre preservation: 1
- time scaling factors
  - 0 s: 0 s
  - 1 s: 4 s

---

Variation 5: Seems similar to variation 4...

- model: harmonic plus stochastic
- window type: Blackman
- window size: 5292 samples
- FFT size: 8192 samples
- magnitude threshold: −70 dB
- minimum duration of sinusoidal tracks: 0.1 s
- maximum number of harmonics: 100
- minimum fundamental frequency: 550 Hz
- maximum fundamental frequency: 650 Hz
- maximum error in f0 detection algorithm: 100 Hz
- maximum frequency deviation in harmonic tracks: 0.01 Hz
- stochastic approximation factor: 1
- frequency scaling factors
  - 0 s: 1
  - 1 s: 4
  - 2 s: 1
  - 3 s: 4
  - 4 s: 1
  - 5 s: 4
- frequency stretching factors
  - 0 s: 4
  - 1 s: 1
  - 2 s: 4
  - 3 s: 1
  - 4 s: 4
  - 5 s: 1
- timbre preservation: 1
- time scaling factors
  - 0 s: 0 s
  - 1 s: 4 s

---

Finally, I use Audacity to compose the above into something seemingly meaningful. Each of the above variation appears for 4 times. It feels like there are many airplanes flying or fireworks ongoing very nearby.

## question 2

- file: [part 2/a10-a.wav](part%202/a10-a.wav)
