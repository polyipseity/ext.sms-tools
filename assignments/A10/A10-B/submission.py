from glob import iglob
from json import dump, loads
from os import makedirs, path
from pathlib import Path
from subprocess import check_output
from sys import stderr
from typing import Sequence
from soundAnalysis import clusterSounds
from soundDownload import downloadSoundsFreesound

import numpy as np
import soundAnalysis


def main() -> None:
    api_key = None

    # part 1
    queries = (
        "violin",
        "guitar",
        "bassoon",
        "trumpet",
        "clarinet",
        "cello",
        # "naobo",
        "snare drum",
        "flute",
        # "mridangam",
        "electric guitar",
        "dizi",
    )
    makedirs("sounds/", exist_ok=True)
    for query in queries:
        if not path.exists(f"sounds/{query}"):
            if api_key is None:
                api_key = input("API key: ")
            downloadSoundsFreesound(
                queryText=query,
                API_Key=api_key,
                outputDir="sounds/",
                topNResults=20,
                duration=(0, 8.5),
                tag="single-note" if query not in {"electric guitar", "dizi"} else None,
            )

    # part 2
    """
    0. lowlevel.spectral_centroid.mean
    1. lowlevel.dissonance.mean
    2. lowlevel.hfc.mean
    3. sfx.logattacktime.mean
    4. sfx.inharmonicity.mean
    5. lowlevel.spectral_contrast.mean.0
    6. lowlevel.spectral_contrast.mean.1
    7. lowlevel.spectral_contrast.mean.2
    8. lowlevel.spectral_contrast.mean.3
    9. lowlevel.spectral_contrast.mean.4
    10. lowlevel.spectral_contrast.mean.5
    11. lowlevel.mfcc.mean.0
    12. lowlevel.mfcc.mean.1
    13. lowlevel.mfcc.mean.2
    14. lowlevel.mfcc.mean.3
    15. lowlevel.mfcc.mean.4
    16. lowlevel.mfcc.mean.5
    """
    clusterSounds("./sounds/", nCluster=len(queries), descInput=[0, 1, 2, 3, 7, 13])

    # part 3

    # Download Essentia extractors (for Windows): <https://essentia.upf.edu/extractors/essentia-extractors-v2.1_beta2-win-i686.tar.gz>
    # Use `streaming_extractor_music(.exe)`
    """`streaming_extractor_music profile.yml`
# See <https://essentia.upf.edu/streaming_extractor_music.html#configuration>
outputFrames: 1
outputFormat: json
requireMbid: false
indent: 4
    """
    for filepath in iglob("**/*.mp3", root_dir="./sounds/", recursive=True):
        input_path = Path("./sounds/") / filepath
        output_path = (Path("./intermediate/") / filepath).with_suffix(".json")
        if output_path.exists():
            continue
        output_path.parent.mkdir(parents=True, exist_ok=True)
        check_output(
            (
                "./streaming_extractor_music.exe",
                input_path,
                output_path,
                "./streaming_extractor_music profile.yml",
            ),
            stdin=None,
            # stdout=stdout,
            stderr=stderr,
        )

    for filepath in iglob(
        "**/*.json_frames", root_dir="./intermediate/", recursive=True
    ):
        input_path = Path("./intermediate/") / filepath
        output_path = (Path("./descriptors/") / filepath).with_suffix(".json")
        if output_path.exists():
            continue
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(input_path, "rb") as input_file:
            input_file_bytes = input_file.read()
        input_json = loads(input_file_bytes.replace(b".#IND", b""))
        del input_file_bytes

        filter = ~np.array(input_json["lowlevel"]["silence_rate_60dB"], dtype=bool)
        output = dict[str, Sequence[float]]()

        output["lowlevel.dissonance.mean"] = [
            np.mean(input_json["lowlevel"]["dissonance"], where=filter)
        ]
        output["lowlevel.gfcc.mean"] = [
            np.mean(
                input_json["lowlevel"]["gfcc"],
                where=filter[..., np.newaxis],
                axis=-2,
            ).tolist()
        ]
        output["lowlevel.hfc.mean"] = [
            np.mean(input_json["lowlevel"]["hfc"], where=filter)
        ]
        output["lowlevel.mfcc.mean"] = [
            np.mean(
                input_json["lowlevel"]["mfcc"],
                where=filter[..., np.newaxis],
                axis=-2,
            ).tolist()
        ]
        output["lowlevel.spectral_complexity.mean"] = [
            np.mean(input_json["lowlevel"]["spectral_complexity"], where=filter)
        ]
        output["lowlevel.spectral_entropy.mean"] = [
            np.mean(input_json["lowlevel"]["spectral_entropy"], where=filter)
        ]
        output["lowlevel.spectral_flux.mean"] = [
            np.mean(input_json["lowlevel"]["spectral_flux"], where=filter)
        ]
        output["lowlevel.spectral_spread.mean"] = [
            np.mean(input_json["lowlevel"]["spectral_spread"], where=filter)
        ]
        output["lowlevel.spectral_strongpeak.mean"] = [
            np.mean(input_json["lowlevel"]["spectral_strongpeak"], where=filter)
        ]
        output["lowlevel.spectral_contrast_coeffs.mean"] = [
            np.mean(
                input_json["lowlevel"]["spectral_contrast_coeffs"],
                where=filter[..., np.newaxis],
                axis=-2,
            ).tolist()
        ]
        output["lowlevel.spectral_contrast_valleys.mean"] = [
            np.mean(
                input_json["lowlevel"]["spectral_contrast_valleys"],
                where=filter[..., np.newaxis],
                axis=-2,
            ).tolist()
        ]
        output["tonal.hpcp_entropy.mean"] = [
            np.mean(input_json["tonal"]["hpcp_entropy"])
        ]  # Cannot use `filter`, since the size differs.

        with open(output_path, "wt", encoding="utf-8") as output_file:
            dump(output, output_file)

    soundAnalysis.descriptorMapping = dict(
        enumerate(
            (
                "lowlevel.dissonance.mean",
                "lowlevel.gfcc.mean.2",
                "lowlevel.hfc.mean",
                "lowlevel.mfcc.mean.3",
                "lowlevel.spectral_complexity.mean",
                "lowlevel.spectral_contrast_coeffs.mean.2",
                "lowlevel.spectral_contrast_valleys.mean.3",
                "lowlevel.spectral_entropy.mean",
                "lowlevel.spectral_flux.mean",
                "lowlevel.spectral_spread.mean",
                "lowlevel.spectral_strongpeak.mean",
                "tonal.hpcp_entropy.mean",
            )
        )
    )
    clusterSounds(
        "./descriptors/",
        nCluster=len(queries),
        descInput=list(soundAnalysis.descriptorMapping.keys()),
    )


if __name__ == "__main__":
    main()
