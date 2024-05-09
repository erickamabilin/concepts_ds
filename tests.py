# Unit tests for the Bloom filter

    # Add check for false positive rate against size
    # Add check false positive rate if size was exceeded
    # Add check for compression rate (false positive rate vs expected false positive rate)


import unittest
from bloom_filter import BloomFilter


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
