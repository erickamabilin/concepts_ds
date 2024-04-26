class SimpleBloomFilter:
    def __init__(self, size):
        self.bit_array = [0] * size

    def add(self, item):
        index = hash(item) % len(self.bit_array)
        self.bit_array[index] = 1

    def check(self, item):
        index = hash(item) % len(self.bit_array)
        return self.bit_array[index] == 1

# Example 
bloom = SimpleBloomFilter(10)  # just for demostration

bloom.add("apple")
bloom.add("banana")

# Check for existing and non-existing items
print("apple" in bloom)  # Should be True
print("banana" in bloom)  # Should be True
print("cherry" in bloom)  # Should be False
