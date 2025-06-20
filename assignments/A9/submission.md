# A9 submission

- title: A9 submission

## question 1

These instruments are chosen for their similarity in their appearance. The queries do not need to be very complicated. The tag `single-note` already does most of the filtering.

- cello: `cello`; duration: 0 s to 8.5 s; tag: `single-note`
- guitar: `guitar`; duration: 0 s to 8.5 s; tag: `single-note`
- violin: `violin`; duration: 0 s to 8.5 s; tag: `single-note`

---

- file: [part 1.zip](part%201.zip)
  - source: [part 1/](part%201/)
    - [cello_SoundList.txt](part%201/cello_SoundList.txt)
    - [guitar_SoundList.txt](part%201/guitar_SoundList.txt)
    - [violin_SoundList.txt](part%201/violin_SoundList.txt)

## question 2

I try out all 136 possibilities and pick the best one.

- combination: `lowlevel.spectral_contrast.mean.2` \(7\), `lowlevel.mfcc.mean.3` \(14\)
  - They measure different audio features. Further, the timbre of the chosen instruments are slightly different, which are most likely in the middle. So our audio features consider mid-range frequencies.

---

- file: [part 2.zip](part%202.zip)
  - source: [part 2/](part%202/)
    - [7, 14.png](part%202/7,%2014.png)
    - [7, 14.svg](part%202/7,%2014.svg)

## question 3

Using the combination `lowlevel.dissonance.mean` \(1\), `lowlevel.spectral_contrast.mean.2` \(7\), `lowlevel.mfcc.mean.3` \(14\). The last 2 are chosen from part 2. The first 1 is added because it measures a different audio feature from the last 2. I obtain:

```text
(Cluster: 0) Using majority voting as a criterion this cluster belongs to class: cello
Number of sounds in this cluster are: 26
sound-id, sound-class, classification decision
[['248006' 'cello' '1']
 ['248007' 'cello' '1']
 ['248008' 'cello' '1']
 ['248009' 'cello' '1']
 ['372712' 'cello' '1']
 ['372722' 'cello' '1']
 ['372727' 'cello' '1']
 ['372775' 'cello' '1']
 ['372776' 'cello' '1']
 ['372780' 'cello' '1']
 ['372781' 'cello' '1']
 ['372782' 'cello' '1']
 ['372783' 'cello' '1']
 ['372785' 'cello' '1']
 ['372786' 'cello' '1']
 ['372787' 'cello' '1']
 ['372801' 'cello' '1']
 ['372802' 'cello' '1']
 ['372803' 'cello' '1']
 ['110455' 'guitar' '0']
 ['399490' 'guitar' '0']
 ['399504' 'guitar' '0']
 ['91199' 'guitar' '0']
 ['247880' 'violin' '0']
 ['247881' 'violin' '0']
 ['247882' 'violin' '0']]

(Cluster: 1) Using majority voting as a criterion this cluster belongs to class: guitar
Number of sounds in this cluster are: 12
sound-id, sound-class, classification decision
[['372726' 'cello' '0']
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
 ['399501' 'guitar' '1']]

(Cluster: 2) Using majority voting as a criterion this cluster belongs to class: violin
Number of sounds in this cluster are: 22
sound-id, sound-class, classification decision
[['399466' 'guitar' '0']
 ['399502' 'guitar' '0']
 ['399503' 'guitar' '0']
 ['399505' 'guitar' '0']
 ['84413' 'guitar' '0']
 ['247874' 'violin' '1']
 ['247875' 'violin' '1']
 ['247877' 'violin' '1']
 ['247878' 'violin' '1']
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
Out of 60 sounds, 13 sounds are incorrectly classified considering that one cluster should ideally contain sounds from only a single class
You obtain a classification (based on obtained clusters and majority voting) accuracy of 78.33 percentage
```

It seems like guitar is most easily misclassified. This is probably due to the guitar sounds not being similar enough to each other.

## question 4

Using the following query to find a new sound. The query does not need to be very complicated. The tag `single-note` already does most of the filtering.

- bassoon: `bassoon`; duration: 0 s to 8.5 s; tag: `single-note`

K is chosen to be 3 \(an odd number\). And using the same features as part 3 due to its high accuracy, I obtain `cello` as the output using the following sound:

- Bassoon - vibrato sustain - F#2 \(PSBassoon_G1_v2_1.wav\) by sgossner -- <https://freesound.org/s/372707/> -- License: Creative Commons 0
