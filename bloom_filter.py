# The main module with the Bloom filter implementation
import math
import mmh3

class BloomFilter:
    def __init__(self, size, error_rate):
        self.size = size
        self.error_rate = error_rate
        self.bit_array_size = self.calculate_bit_array_size(size, error_rate)
        self.bit_array = [0] * self.bit_array_size
        self.num_hashes = self.calculate_num_hashes(size, self.bit_array_size)
        self.counter = 0

    def add(self, item):
        for i in range(self.num_hashes):
            hash_val = mmh3.hash(item, i) % self.bit_array_size
            self.bit_array[hash_val] = 1
        self.counter += 1

    def check(self, item):
        for i in range(self.num_hashes):
            hash_val = mmh3.hash(item, i) % self.bit_array_size
            if self.bit_array[hash_val] == 0:
                return False
        return True

    def calculate_bit_array_size(self, size, error_rate):
        return int(- (size * math.log(error_rate)) / (math.log(2) ** 2))

    def calculate_num_hashes(self, size, bit_array_size):
        return int((bit_array_size / size) * math.log(2))