"""Download the Traffic dataset for the minimal iTransformer example."""
import zipfile
import shutil
from pathlib import Path
import gdown

# Google Drive file ID for iTransformer_datasets.zip
FILE_ID = "1l51QsKvQPcqILT3DwfjCgx8Dsg2rpjot"
URL = f"https://drive.google.com/uc?id={FILE_ID}"


def download_and_prepare(dest_dir: Path = Path("dataset")) -> None:
    dest_dir.mkdir(exist_ok=True)
    zip_path = dest_dir / "iTransformer_datasets.zip"
    if not zip_path.exists():
        print("Downloading dataset...")
        gdown.download(URL, str(zip_path), quiet=False)
    else:
        print("Zip file already exists. Skipping download.")

    print("Extracting dataset...")
    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(dest_dir)

    source = dest_dir / "iTransformer_datasets" / "traffic"
    target = dest_dir / "traffic"
    if target.exists():
        print(f"{target} already exists. Skipping move.")
    else:
        shutil.move(str(source), str(target))
    print(f"Dataset prepared at {target}")


if __name__ == "__main__":
    download_and_prepare()
