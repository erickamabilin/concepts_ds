## bloom_filter.py      # The main module with the Bloom filter implementation
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
    # Add check for false positive rate against size
    # Add check false positive rate if size was exceeded
    # Add check for compression rate (false positive rate vs expected false positive rate)

def test_false_positives(bloom_filter, items, test_items):
    for item in items:
        bloom_filter.add(item)
           
    false_positives = sum(1 for item in test_items if bloom_filter.check(item))
    print(f"False positive rate: {false_positives / len(test_items):.2%}")

# Example 
bloom = BloomFilter(1000, 4)  # just for demostration

existing_items = ["apple", "banana", "orange"]
test_items = ["grape", "mango", "lemon"] + existing_items

test_false_positives(bloom, existing_items, test_items)


# Example 2 - Testing Different Data Type
bloom = BloomFilter(1000, 4)

bloom.add("TTAATTA")
bloom.add("ATTACTC")

# Check for existing and non-existing items
print("TTAATTA", bloom.check("TTAATTA"))  # Should be True
print("ATTACTC", bloom.check("ATTACTC"))  # Should be True
print("ACTCAC", bloom.check("ACTCAC"))  # Should be False
