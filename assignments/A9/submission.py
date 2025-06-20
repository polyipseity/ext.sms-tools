from glob import glob
from os import makedirs, path
from soundAnalysis import classifySoundkNN, clusterSounds, descriptorPairScatterPlot
from soundDownload import downloadSoundsFreesound


def main() -> None:
    api_key = None

    # part 1
    makedirs("sounds/", exist_ok=True)
    for query in ("violin", "guitar", "cello"):
        if not path.exists(f"sounds/{query}"):
            if api_key is None:
                api_key = input("API key: ")
            downloadSoundsFreesound(
                queryText=query,
                API_Key=api_key,
                outputDir="sounds/",
                topNResults=20,
                duration=(0, 8.5),
                tag="single-note",
            )

    # part 2
    makedirs("plots/", exist_ok=True)
    if not path.exists("plots/"):
        for a in range(17):
            for b in range(a + 1, 17):
                descriptorPairScatterPlot("sounds/", (a, b), 1, f"plots/{a}, {b}.svg")

    # part 3
    clusterSounds("sounds/", nCluster=3, descInput=[1, 7, 14])

    # part 4
    makedirs("queries/", exist_ok=True)
    for query in ("bassoon",):
        if not path.exists(f"queries/{query}"):
            if api_key is None:
                api_key = input("API key: ")
            downloadSoundsFreesound(
                queryText=query,
                API_Key=api_key,
                outputDir="queries/",
                topNResults=1,
                duration=(0, 8.5),
                tag="single-note",
            )
    classifySoundkNN(
        glob("queries/**/*.json", recursive=True)[0],
        "sounds/",
        K=3,
        descInput=[1, 7, 14],
    )


if __name__ == "__main__":
    main()
