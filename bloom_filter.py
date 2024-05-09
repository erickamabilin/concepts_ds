# The main module with the Bloom filter implementation
import hashlib

def hash_functions(item, num_hashes, size):
    result = []
    for i in range(num_hashes):
        hash_obj = hashlib.sha256()  # cryptographic hash functions SHA-256 
        hash_obj.update(item.encode('utf-8') + str(i).encode('utf-8'))
        result.append(int(hash_obj.hexdigest(), 16) % size)
    return result

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size

    def add(self, item):
        indices = hash_functions(item, self.num_hashes, self.size)
        for index in indices:
            	self.bit_array[index] = 1

    def check(self, item):
        indices = hash_functions(item, self.num_hashes, self.size)
        return all(self.bit_array[index] for index in indices)