# The main module with the Bloom filter implementation
import hashlib

class BloomFilter:
    def __init__(self, size, num_hashes):
        self.size = size
        self.num_hashes = num_hashes
        self.bit_array = [0] * size
        self.counter = 0

    def add(self, item):
        indices = self.hash_functions(item)
        for index in indices:
            	self.bit_array[index] = 1
        self.counter += 1

    def check(self, item):
        indices = self.hash_functions(item)
        return all(self.bit_array[index] for index in indices)
    
    def hash_functions(self, item):
        result = []
        for i in range(self.num_hashes):
            hash_obj = hashlib.sha256()  # cryptographic hash functions SHA-256 
            hash_obj.update(item.encode('utf-8') + str(i).encode('utf-8'))
            result.append(int(hash_obj.hexdigest(), 16) % self.size)
        return result