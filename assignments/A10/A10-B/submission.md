# A10-B submission

- title: A10-B submission

## question 1

These instruments are chosen so that they have at least 20 good search results. The queries do not need to be very complicated. The tag `single-note` already does most of the filtering for most queries. Some instruments do not have recordings having this tag, so the tag is omitted.

- violin: `violin`; duration: 0 s to 8.5 s; tag: `single-note`
- guitar: `guitar`; duration: 0 s to 8.5 s; tag: `single-note`
- bassoon: `bassoon`; duration: 0 s to 8.5 s; tag: `single-note`
- trumpet: `trumpet`; duration: 0 s to 8.5 s; tag: `single-note`
- clarinet: `clarinet`; duration: 0 s to 8.5 s; tag: `single-note`
- cello: `cello`; duration: 0 s to 8.5 s; tag: `single-note`
- snare drum: `snare drum`; duration: 0 s to 8.5 s; tag: `single-note`
- flute: `flute`; duration: 0 s to 8.5 s; tag: `single-note`
- guitar: `electric guitar`; duration: 0 s to 8.5 s
- flute: `dizi`; duration: 0 s to 8.5 s

## question 2

I use the combination indicated below to get a baseline accuracy of 55.5% \(n=200\). The reasons are:

- 0: `lowlevel.spectral_centroid.mean`: yes, very different from other features
- 1: `lowlevel.dissonance.mean`: yes, very different from other features apart from `sfx.inharmonicity.mean`
- 2: `lowlevel.hfc.mean`: yes, very different form other features
- 3: `sfx.logattacktime.mean`: yes, very different from other features
- 4: `sfx.inharmonicity.mean`: no, similar to `lowlevel.dissonance.mean`
- 5: `lowlevel.spectral_contrast.mean.0`: no, only use one to not repeat features
- 6: `lowlevel.spectral_contrast.mean.1`: no, only use one to not repeat features
- 7: `lowlevel.spectral_contrast.mean.2`: yes, only use one to not repeat features; the middle one is used for most generality
- 8: `lowlevel.spectral_contrast.mean.3`: no, only use one to not repeat features
- 9: `lowlevel.spectral_contrast.mean.4`: no, only use one to not repeat features
- 10: `lowlevel.spectral_contrast.mean.5`: no, only use one to not repeat features
- 11: `lowlevel.mfcc.mean.0`: no, only use one to not repeat features
- 12: `lowlevel.mfcc.mean.1`: no, only use one to not repeat features
- 13: `lowlevel.mfcc.mean.2`: yes, only use one to not repeat features; the middle one is used for most generality
- 14: `lowlevel.mfcc.mean.3`: no, only use one to not repeat features
- 15: `lowlevel.mfcc.mean.4`: no, only use one to not repeat features
- 16: `lowlevel.mfcc.mean.5`: no, only use one to not repeat features

Output for reference:

```text
(Cluster: 0) Using majority voting as a criterion this cluster belongs to class: cello
Number of sounds in this cluster are: 11
sound-id, sound-class, classification decision
[['372722' 'cello' '1']
 ['372727' 'cello' '1']
 ['372775' 'cello' '1']
 ['372776' 'cello' '1']
 ['372780' 'cello' '1']
 ['372782' 'cello' '1']
 ['372783' 'cello' '1']
 ['372786' 'cello' '1']
 ['372787' 'cello' '1']
 ['372801' 'cello' '1']
 ['372802' 'cello' '1']]

(Cluster: 1) Using majority voting as a criterion this cluster belongs to class: guitar
Number of sounds in this cluster are: 14
sound-id, sound-class, classification decision
[['372691' 'bassoon' '0']
 ['372726' 'cello' '0']
 ['13699' 'guitar' '1']
 ['13700' 'guitar' '1']
 ['13701' 'guitar' '1']
 ['13702' 'guitar' '1']
 ['13703' 'guitar' '1']
 ['13705' 'guitar' '1']
 ['13706' 'guitar' '1']
 ['13708' 'guitar' '1']
 ['13709' 'guitar' '1']
 ['13710' 'guitar' '1']
 ['399501' 'guitar' '1']
 ['84413' 'guitar' '1']]

(Cluster: 2) Using majority voting as a criterion this cluster belongs to class: violin
Number of sounds in this cluster are: 12
sound-id, sound-class, classification decision
[['130466' 'electric guitar' '0']
 ['130467' 'electric guitar' '0']
 ['399490' 'guitar' '0']
 ['399504' 'guitar' '0']
 ['399505' 'guitar' '0']
 ['269528' 'violin' '1']
 ['269531' 'violin' '1']
 ['269532' 'violin' '1']
 ['269533' 'violin' '1']
 ['269534' 'violin' '1']
 ['269537' 'violin' '1']
 ['269539' 'violin' '1']]

(Cluster: 3) Using majority voting as a criterion this cluster belongs to class: electric guitar
Number of sounds in this cluster are: 30
sound-id, sound-class, classification decision
[['372785' 'cello' '0']
 ['249138' 'clarinet' '0']
 ['249139' 'clarinet' '0']
 ['249140' 'clarinet' '0']
 ['249141' 'clarinet' '0']
 ['249142' 'clarinet' '0']
 ['249143' 'clarinet' '0']
 ['130471' 'electric guitar' '1']
 ['183552' 'electric guitar' '1']
 ['183553' 'electric guitar' '1']
 ['183554' 'electric guitar' '1']
 ['183555' 'electric guitar' '1']
 ['183557' 'electric guitar' '1']
 ['183558' 'electric guitar' '1']
 ['183559' 'electric guitar' '1']
 ['464989' 'electric guitar' '1']
 ['518300' 'electric guitar' '1']
 ['247041' 'flute' '0']
 ['247042' 'flute' '0']
 ['247043' 'flute' '0']
 ['247053' 'flute' '0']
 ['354450' 'flute' '0']
 ['354592' 'flute' '0']
 ['354625' 'flute' '0']
 ['247354' 'trumpet' '0']
 ['247355' 'trumpet' '0']
 ['247356' 'trumpet' '0']
 ['247357' 'trumpet' '0']
 ['247880' 'violin' '0']
 ['247882' 'violin' '0']]

(Cluster: 4) Using majority voting as a criterion this cluster belongs to class: bassoon
Number of sounds in this cluster are: 14
sound-id, sound-class, classification decision
[['372682' 'bassoon' '1']
 ['372684' 'bassoon' '1']
 ['372689' 'bassoon' '1']
 ['372692' 'bassoon' '1']
 ['372694' 'bassoon' '1']
 ['372698' 'bassoon' '1']
 ['372699' 'bassoon' '1']
 ['372701' 'bassoon' '1']
 ['372702' 'bassoon' '1']
 ['372703' 'bassoon' '1']
 ['372705' 'bassoon' '1']
 ['372706' 'bassoon' '1']
 ['255721' 'electric guitar' '0']
 ['399503' 'guitar' '0']]

(Cluster: 5) Using majority voting as a criterion this cluster belongs to class: snare drum
Number of sounds in this cluster are: 24
sound-id, sound-class, classification decision
[['372712' 'cello' '0']
 ['372781' 'cello' '0']
 ['183556' 'electric guitar' '0']
 ['375426' 'snare drum' '1']
 ['375427' 'snare drum' '1']
 ['375428' 'snare drum' '1']
 ['375429' 'snare drum' '1']
 ['375430' 'snare drum' '1']
 ['375431' 'snare drum' '1']
 ['375432' 'snare drum' '1']
 ['375433' 'snare drum' '1']
 ['375437' 'snare drum' '1']
 ['375438' 'snare drum' '1']
 ['375439' 'snare drum' '1']
 ['375441' 'snare drum' '1']
 ['375442' 'snare drum' '1']
 ['375443' 'snare drum' '1']
 ['375444' 'snare drum' '1']
 ['375445' 'snare drum' '1']
 ['375446' 'snare drum' '1']
 ['375447' 'snare drum' '1']
 ['375448' 'snare drum' '1']
 ['375449' 'snare drum' '1']
 ['247881' 'violin' '0']]

(Cluster: 6) Using majority voting as a criterion this cluster belongs to class: trumpet
Number of sounds in this cluster are: 47
sound-id, sound-class, classification decision
[['372693' 'bassoon' '0']
 ['249122' 'clarinet' '0']
 ['249124' 'clarinet' '0']
 ['249125' 'clarinet' '0']
 ['249126' 'clarinet' '0']
 ['249127' 'clarinet' '0']
 ['249130' 'clarinet' '0']
 ['249132' 'clarinet' '0']
 ['249134' 'clarinet' '0']
 ['249136' 'clarinet' '0']
 ['429860' 'dizi' '0']
 ['130468' 'electric guitar' '0']
 ['130469' 'electric guitar' '0']
 ['243424' 'electric guitar' '0']
 ['518301' 'electric guitar' '0']
 ['247036' 'flute' '0']
 ['247044' 'flute' '0']
 ['247045' 'flute' '0']
 ['247046' 'flute' '0']
 ['247047' 'flute' '0']
 ['354444' 'flute' '0']
 ['354534' 'flute' '0']
 ['247370' 'trumpet' '1']
 ['247372' 'trumpet' '1']
 ['247373' 'trumpet' '1']
 ['247375' 'trumpet' '1']
 ['247377' 'trumpet' '1']
 ['247378' 'trumpet' '1']
 ['247379' 'trumpet' '1']
 ['247380' 'trumpet' '1']
 ['247381' 'trumpet' '1']
 ['247382' 'trumpet' '1']
 ['247383' 'trumpet' '1']
 ['247384' 'trumpet' '1']
 ['247386' 'trumpet' '1']
 ['247387' 'trumpet' '1']
 ['247388' 'trumpet' '1']
 ['247874' 'violin' '0']
 ['247875' 'violin' '0']
 ['247877' 'violin' '0']
 ['247878' 'violin' '0']
 ['271048' 'violin' '0']
 ['271049' 'violin' '0']
 ['271051' 'violin' '0']
 ['271510' 'violin' '0']
 ['271511' 'violin' '0']
 ['271512' 'violin' '0']]

(Cluster: 7) Using majority voting as a criterion this cluster belongs to class: cello
Number of sounds in this cluster are: 13
sound-id, sound-class, classification decision
[['372686' 'bassoon' '0']
 ['372695' 'bassoon' '0']
 ['372707' 'bassoon' '0']
 ['248004' 'cello' '1']
 ['248006' 'cello' '1']
 ['248007' 'cello' '1']
 ['248008' 'cello' '1']
 ['248009' 'cello' '1']
 ['34327' 'electric guitar' '0']
 ['553950' 'electric guitar' '0']
 ['110455' 'guitar' '0']
 ['91199' 'guitar' '0']
 ['247371' 'trumpet' '0']]

(Cluster: 8) Using majority voting as a criterion this cluster belongs to class: dizi
Number of sounds in this cluster are: 11
sound-id, sound-class, classification decision
[['384937' 'dizi' '1']
 ['384939' 'dizi' '1']
 ['384940' 'dizi' '1']
 ['384949' 'dizi' '1']
 ['384953' 'dizi' '1']
 ['384954' 'dizi' '1']
 ['384956' 'dizi' '1']
 ['384958' 'dizi' '1']
 ['384959' 'dizi' '1']
 ['429859' 'dizi' '1']
 ['429861' 'dizi' '1']]

(Cluster: 9) Using majority voting as a criterion this cluster belongs to class: dizi
Number of sounds in this cluster are: 24
sound-id, sound-class, classification decision
[['372685' 'bassoon' '0']
 ['372687' 'bassoon' '0']
 ['372704' 'bassoon' '0']
 ['249128' 'clarinet' '0']
 ['249129' 'clarinet' '0']
 ['249131' 'clarinet' '0']
 ['249133' 'clarinet' '0']
 ['249137' 'clarinet' '0']
 ['384942' 'dizi' '1']
 ['384943' 'dizi' '1']
 ['384944' 'dizi' '1']
 ['384945' 'dizi' '1']
 ['384946' 'dizi' '1']
 ['429862' 'dizi' '1']
 ['429864' 'dizi' '1']
 ['429865' 'dizi' '1']
 ['247038' 'flute' '0']
 ['247040' 'flute' '0']
 ['247048' 'flute' '0']
 ['247049' 'flute' '0']
 ['247050' 'flute' '0']
 ['247051' 'flute' '0']
 ['399466' 'guitar' '0']
 ['399502' 'guitar' '0']]
Out of 200 sounds, 89 sounds are incorrectly classified considering that one cluster should ideally contain sounds from only a single class
You obtain a classification (based on obtained clusters and majority voting) accuracy of 55.50 percentage
```

---

- file: [submission.pdf](submission.pdf)
  - source: [submission.md](submission.md)

## question 3

I used from `streaming_extractor_music` from <https://essentia.upf.edu/extractors`> to extract many audio features, and then selectively choose some of them. Then, `lowlevel.silence_rate_60dB` is used to detect silence and remove those frames from the audio. Finally, the mean of the selected audio features are computed, and then used for classification. The 60 dB threshold is determined by inspecting the output for some audio files. For the 20 dB and 30 dB thresholds, they are too high, so almost all frames are detected as silent.

I use the combination indicated below to get a new accuracy of 68.5% \(n=200\), which is much higher than the baseline accuracy, but still not as high when there are few instruments. The features are selected so they are independent of the instrument pitch, and do not overlap with other features excessively. This is why only 1 band is selected for `lowlevel.gfcc`, `lowlevel.mfcc`, `lowlevel.spectral_contrast_coeffs`, and `lowlevel.spectral_constrast_valleys`.

- `lowlevel.dissonance.mean`
- `lowlevel.gfcc.mean.2`
- `lowlevel.hfc.mean`
- `lowlevel.mfcc.mean.3`
- `lowlevel.spectral_complexity.mean`
- `lowlevel.spectral_contrast_coeffs.mean.2`
- `lowlevel.spectral_contrast_valleys.mean.3`
- `lowlevel.spectral_entropy.mean`
- `lowlevel.spectral_flux.mean`
- `lowlevel.spectral_spread.mean`
- `lowlevel.spectral_strongpeak.mean`
- `tonal.hpcp_entropy.mean`

I observed that as the number of instruments increase, the harder it gets to achieve a high accuracy, even with many descriptors. This may be a limitation of the KNN model, and we may use other more advanced models \(not taught in this course\) to achieve a higher accuracy.

Output for reference:

```text
(Cluster: 0) Using majority voting as a criterion this cluster belongs to class: guitar
Number of sounds in this cluster are: 18
sound-id, sound-class, classification decision
[['372712' 'cello' '0']
 ['372722' 'cello' '0']
 ['372726' 'cello' '0']
 ['372780' 'cello' '0']
 ['372802' 'cello' '0']
 ['553950' 'electric guitar' '0']
 ['110455' 'guitar' '1']
 ['13699' 'guitar' '1']
 ['13700' 'guitar' '1']
 ['13701' 'guitar' '1']
 ['13702' 'guitar' '1']
 ['13703' 'guitar' '1']
 ['13705' 'guitar' '1']
 ['13706' 'guitar' '1']
 ['13708' 'guitar' '1']
 ['13709' 'guitar' '1']
 ['13710' 'guitar' '1']
 ['91199' 'guitar' '1']]

(Cluster: 1) Using majority voting as a criterion this cluster belongs to class: dizi
Number of sounds in this cluster are: 20
sound-id, sound-class, classification decision
[['384942' 'dizi' '1']
 ['384943' 'dizi' '1']
 ['384945' 'dizi' '1']
 ['384946' 'dizi' '1']
 ['384953' 'dizi' '1']
 ['384954' 'dizi' '1']
 ['384956' 'dizi' '1']
 ['384958' 'dizi' '1']
 ['384959' 'dizi' '1']
 ['429859' 'dizi' '1']
 ['429860' 'dizi' '1']
 ['429861' 'dizi' '1']
 ['429862' 'dizi' '1']
 ['429864' 'dizi' '1']
 ['429865' 'dizi' '1']
 ['399505' 'guitar' '0']
 ['247874' 'violin' '0']
 ['247875' 'violin' '0']
 ['247877' 'violin' '0']
 ['247878' 'violin' '0']]

(Cluster: 2) Using majority voting as a criterion this cluster belongs to class: snare drum
Number of sounds in this cluster are: 21
sound-id, sound-class, classification decision
[['130466' 'electric guitar' '0']
 ['375426' 'snare drum' '1']
 ['375427' 'snare drum' '1']
 ['375428' 'snare drum' '1']
 ['375429' 'snare drum' '1']
 ['375430' 'snare drum' '1']
 ['375431' 'snare drum' '1']
 ['375432' 'snare drum' '1']
 ['375433' 'snare drum' '1']
 ['375437' 'snare drum' '1']
 ['375438' 'snare drum' '1']
 ['375439' 'snare drum' '1']
 ['375441' 'snare drum' '1']
 ['375442' 'snare drum' '1']
 ['375443' 'snare drum' '1']
 ['375444' 'snare drum' '1']
 ['375445' 'snare drum' '1']
 ['375446' 'snare drum' '1']
 ['375447' 'snare drum' '1']
 ['375448' 'snare drum' '1']
 ['375449' 'snare drum' '1']]

(Cluster: 3) Using majority voting as a criterion this cluster belongs to class: clarinet
Number of sounds in this cluster are: 25
sound-id, sound-class, classification decision
[['372685' 'bassoon' '0']
 ['372693' 'bassoon' '0']
 ['372704' 'bassoon' '0']
 ['249122' 'clarinet' '1']
 ['249124' 'clarinet' '1']
 ['249125' 'clarinet' '1']
 ['249126' 'clarinet' '1']
 ['249127' 'clarinet' '1']
 ['249128' 'clarinet' '1']
 ['249129' 'clarinet' '1']
 ['249130' 'clarinet' '1']
 ['249131' 'clarinet' '1']
 ['249132' 'clarinet' '1']
 ['249133' 'clarinet' '1']
 ['249134' 'clarinet' '1']
 ['249136' 'clarinet' '1']
 ['249137' 'clarinet' '1']
 ['247038' 'flute' '0']
 ['247040' 'flute' '0']
 ['247048' 'flute' '0']
 ['247049' 'flute' '0']
 ['247050' 'flute' '0']
 ['247051' 'flute' '0']
 ['354444' 'flute' '0']
 ['247388' 'trumpet' '0']]

(Cluster: 4) Using majority voting as a criterion this cluster belongs to class: violin
Number of sounds in this cluster are: 24
sound-id, sound-class, classification decision
[['372775' 'cello' '0']
 ['372783' 'cello' '0']
 ['372787' 'cello' '0']
 ['372801' 'cello' '0']
 ['384937' 'dizi' '0']
 ['384939' 'dizi' '0']
 ['384940' 'dizi' '0']
 ['384944' 'dizi' '0']
 ['399466' 'guitar' '0']
 ['399502' 'guitar' '0']
 ['399503' 'guitar' '0']
 ['269528' 'violin' '1']
 ['269531' 'violin' '1']
 ['269532' 'violin' '1']
 ['269533' 'violin' '1']
 ['269534' 'violin' '1']
 ['269537' 'violin' '1']
 ['269539' 'violin' '1']
 ['271048' 'violin' '1']
 ['271049' 'violin' '1']
 ['271051' 'violin' '1']
 ['271510' 'violin' '1']
 ['271511' 'violin' '1']
 ['271512' 'violin' '1']]

(Cluster: 5) Using majority voting as a criterion this cluster belongs to class: clarinet
Number of sounds in this cluster are: 18
sound-id, sound-class, classification decision
[['249138' 'clarinet' '1']
 ['249139' 'clarinet' '1']
 ['249140' 'clarinet' '1']
 ['249141' 'clarinet' '1']
 ['249142' 'clarinet' '1']
 ['249143' 'clarinet' '1']
 ['384949' 'dizi' '0']
 ['247041' 'flute' '0']
 ['247042' 'flute' '0']
 ['247043' 'flute' '0']
 ['247053' 'flute' '0']
 ['354450' 'flute' '0']
 ['354625' 'flute' '0']
 ['399490' 'guitar' '0']
 ['399504' 'guitar' '0']
 ['247880' 'violin' '0']
 ['247881' 'violin' '0']
 ['247882' 'violin' '0']]

(Cluster: 6) Using majority voting as a criterion this cluster belongs to class: cello
Number of sounds in this cluster are: 15
sound-id, sound-class, classification decision
[['372686' 'bassoon' '0']
 ['372695' 'bassoon' '0']
 ['372707' 'bassoon' '0']
 ['248004' 'cello' '1']
 ['248006' 'cello' '1']
 ['248007' 'cello' '1']
 ['248008' 'cello' '1']
 ['248009' 'cello' '1']
 ['372727' 'cello' '1']
 ['372776' 'cello' '1']
 ['372782' 'cello' '1']
 ['372786' 'cello' '1']
 ['255721' 'electric guitar' '0']
 ['34327' 'electric guitar' '0']
 ['399501' 'guitar' '0']]

(Cluster: 7) Using majority voting as a criterion this cluster belongs to class: trumpet
Number of sounds in this cluster are: 26
sound-id, sound-class, classification decision
[['243424' 'electric guitar' '0']
 ['247044' 'flute' '0']
 ['247045' 'flute' '0']
 ['247046' 'flute' '0']
 ['247047' 'flute' '0']
 ['354534' 'flute' '0']
 ['354592' 'flute' '0']
 ['247354' 'trumpet' '1']
 ['247355' 'trumpet' '1']
 ['247356' 'trumpet' '1']
 ['247357' 'trumpet' '1']
 ['247370' 'trumpet' '1']
 ['247371' 'trumpet' '1']
 ['247372' 'trumpet' '1']
 ['247373' 'trumpet' '1']
 ['247375' 'trumpet' '1']
 ['247377' 'trumpet' '1']
 ['247378' 'trumpet' '1']
 ['247379' 'trumpet' '1']
 ['247380' 'trumpet' '1']
 ['247381' 'trumpet' '1']
 ['247382' 'trumpet' '1']
 ['247383' 'trumpet' '1']
 ['247384' 'trumpet' '1']
 ['247386' 'trumpet' '1']
 ['247387' 'trumpet' '1']]

(Cluster: 8) Using majority voting as a criterion this cluster belongs to class: electric guitar
Number of sounds in this cluster are: 17
sound-id, sound-class, classification decision
[['372781' 'cello' '0']
 ['372785' 'cello' '0']
 ['130467' 'electric guitar' '1']
 ['130468' 'electric guitar' '1']
 ['130469' 'electric guitar' '1']
 ['130471' 'electric guitar' '1']
 ['183552' 'electric guitar' '1']
 ['183553' 'electric guitar' '1']
 ['183554' 'electric guitar' '1']
 ['183555' 'electric guitar' '1']
 ['183556' 'electric guitar' '1']
 ['183557' 'electric guitar' '1']
 ['183558' 'electric guitar' '1']
 ['183559' 'electric guitar' '1']
 ['464989' 'electric guitar' '1']
 ['518300' 'electric guitar' '1']
 ['518301' 'electric guitar' '1']]

(Cluster: 9) Using majority voting as a criterion this cluster belongs to class: bassoon
Number of sounds in this cluster are: 16
sound-id, sound-class, classification decision
[['372682' 'bassoon' '1']
 ['372684' 'bassoon' '1']
 ['372687' 'bassoon' '1']
 ['372689' 'bassoon' '1']
 ['372691' 'bassoon' '1']
 ['372692' 'bassoon' '1']
 ['372694' 'bassoon' '1']
 ['372698' 'bassoon' '1']
 ['372699' 'bassoon' '1']
 ['372701' 'bassoon' '1']
 ['372702' 'bassoon' '1']
 ['372703' 'bassoon' '1']
 ['372705' 'bassoon' '1']
 ['372706' 'bassoon' '1']
 ['247036' 'flute' '0']
 ['84413' 'guitar' '0']]
Out of 200 sounds, 63 sounds are incorrectly classified considering that one cluster should ideally contain sounds from only a single class
You obtain a classification (based on obtained clusters and majority voting) accuracy of 68.50 percentage
```

---

- file: [submission.py](submission.py)
