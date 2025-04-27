import hashlib
import os
import time

def calculate_file_hash(filepath):
    try:
        with open(filepath, "rb") as f:
            file_hash = hashlib.sha256()
            while chunk := f.read(8192):
                file_hash.update(chunk)
        return file_hash.hexdigest()
    except FileNotFoundError:
        return None

def store_initial_hashes(file_list):
    initial_hashes = {}
    for filepath in file_list:
        file_hash = calculate_file_hash(filepath)
        if file_hash:
            initial_hashes[filepath] = file_hash
        else:
            print(f"Warning: Could not calculate hash for {filepath}")
    return initial_hashes

def check_for_changes(file_list, initial_hashes):
    changed_files = []
    for filepath in file_list:
        current_hash = calculate_file_hash(filepath)
        if filepath in initial_hashes and current_hash != initial_hashes[filepath]:
            changed_files.append(filepath)
    return changed_files

def main():
    file_list = ["testfile1.txt", "testfile2.txt"] #replace with your files
    initial_hashes = store_initial_hashes(file_list)

    if not initial_hashes:
        print("No files to monitor.")
        return

    while True:
        changed_files = check_for_changes(file_list, initial_hashes)
        if changed_files:
            print("Changes detected in:")
            for filepath in changed_files:
                print(f"- {filepath}")
            initial_hashes = store_initial_hashes(file_list)
        else:
            print("No changes detected.")

        time.sleep(5)

if __name__ == "__main__":
    main()