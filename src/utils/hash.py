from hashlib import md5
from hashlib import sha1
from hashlib import sha256


class Hash:
    __slots__ = ("block_size", "file_path")

    def __init__(self, file_path: str, block_size: int = 128):
        self.file_path: str = file_path
        self.block_size: int = block_size

    def __hash(self, hash_type) -> str:
        h = hash_type()
        with open(self.file_path, "rb") as file:
            while chunk := file.read(self.block_size * h.block_size):
                h.update(chunk)
        return h.hexdigest()

    def sha1_hash(self) -> str:
        return self.__hash(sha1)

    def md5_hash(self) -> str:
        return self.__hash(md5)

    def sha256_hash(self) -> str:
        return self.__hash(sha256)
