from hashlib import sha1


def sha1_hash(file_path: str) -> str:
    block_size: int = 128
    h = sha1()
    with open(file_path, "rb") as file:
        while chunk := file.read(block_size * h.block_size):
            h.update(chunk)
    return h.hexdigest()
