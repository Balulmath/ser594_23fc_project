import hashlib
import os

def generate_md5(filename):
    md5_hash = hashlib.md5()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    return md5_hash.hexdigest()

def compute_hashes(directory):
    file_hashes = {}
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_hashes[file] = generate_md5(file_path)
    return file_hashes

def save_hashes_to_file(file_hashes):
    with open('hashes.txt', 'w') as f:
        for file, hash in file_hashes.items():
            f.write(f'{file}: {hash}\n')

directory = 'data_original'
file_hashes = compute_hashes(directory)
save_hashes_to_file(file_hashes)
