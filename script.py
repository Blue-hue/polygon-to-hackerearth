import os
import zipfile
import shutil
from pathlib import Path
import sys

def zero_pad(index):
    return f"{index:02d}"

def extract_zip(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def polygon_to_he(zip_file, output_folder):
    zip_file = Path(zip_file)
    if zip_file.suffix != ".zip" or not zip_file.exists():
    # if not zip_file.endswith(".zip") or not os.path.exists(zip_file):
        print("Please provide a valid .zip file exported from Polygon.")
        return

    base_name = Path(zip_file).stem
    target_folder = Path(output_folder) / f"{base_name}_tcs"
    target_folder.mkdir(parents=True, exist_ok=True)
    work_dir = target_folder / "extracted"
    tests_dir = work_dir / "tests"

    mytests_dir = target_folder / "mytests"
    if mytests_dir.exists():
        shutil.rmtree(mytests_dir)
    mytests_dir.mkdir(parents=True, exist_ok=True)

    print(f"[+] Extracting Polygon package: {zip_file}")
    extract_zip(zip_file, work_dir)

    # Gather test input and output files
    print("[+] Collecting and renaming testcases...")

    test_files = sorted([f for f in tests_dir.iterdir() if f.suffix == ".a" or f.suffix == ""])
    test_ids = sorted(set(f.stem for f in test_files))

    for idx, test_id in enumerate(test_ids):
        index = zero_pad(idx)
        input_file = tests_dir / test_id
        output_file = tests_dir / f"{test_id}.a"

        input_target = mytests_dir / f"in{index}.txt"
        output_target = mytests_dir / f"out{index}.txt"

        if input_file.exists() and input_file.is_file():
            shutil.copyfile(input_file, input_target)
        else:
            print(f"[!] Missing input file for {test_id}")

        if output_file.exists():
            shutil.copyfile(output_file, output_target)
        else:
            print(f"[!] Missing output (.a) file for {test_id}")

    # Create final testcases.zip with highest compression
    final_zip_path = target_folder / "testcases.zip"
    print(f"[+] Creating zip: {final_zip_path}")

    with zipfile.ZipFile(final_zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
        for file in sorted(mytests_dir.glob("*.txt")):
            zipf.write(file, arcname=file.name)
        # for file in sorted(output_dir.glob("*.txt")):
        #     zipf.write(file, arcname=file.name)

    print("[✓] Done! `testcases.zip` is ready to upload to HackerEarth.")

    shutil.rmtree(work_dir)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <polygon_package.zip>")
    else:
        zip_file = sys.argv[1]
        output_dir = Path.cwd()
        polygon_to_he(zip_file, output_dir)