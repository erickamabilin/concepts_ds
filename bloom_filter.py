class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = [0] * size

    def add(self, item):
        index = hash(item) % self.size
        self.bit_array[index] = 1

    def check(self, item):
        index = hash(item) % self.size
        return self.bit_array[index] == 1

# Example 
bloom = BloomFilter(10)  # just for demostration

bloom.add("apple")
bloom.add("banana")

# Check for existing and non-existing items
print("apple", bloom.check("apple"))  # Should be True
print("banana", bloom.check("banana"))  # Should be True
print("cherry", bloom.check("cherry"))  # Should be False
