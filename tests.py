# Unit tests for the Bloom filter

    # Add check for false positive rate against size
    # Add check false positive rate if size was exceeded
    # Add check for compression rate (false positive rate vs expected false positive rate)


from bloom_filter import BloomFilter


def test_false_positives(bloom_filter, items, test_items):
    for item in items:
        bloom_filter.add(item)
    false_positives = 0
    for t_item in test_items:
        print(t_item, bloom_filter.check(t_item))
        if bloom_filter.check(t_item):
            false_positives += 1
    print(f"False positive rate: {false_positives/len(test_items):.2%}")
    print(f"False positives over capacity: {false_positives/bloom_filter.size:.2%}")
    if bloom_filter.counter > bloom_filter.size:
    if bloom_filter.counter > bloom_filter.size:
        print(f"False positive over actual size beyond capacity: {false_positives/bloom_filter.counter:.2%}")
    else: print(f"False positive over actual size beyond capacity: Capacity not yet reached")
    print(f"Compression rate: {(false_positives/bloom_filter.counter)/bloom_filter.error_rate:.2%}") 

# Example 
bloom = BloomFilter(1000, 4)  # just for demostration

existing_items = ["apple", "banana", "orange"]
test_items = ["grape", "mango", "lemon"] #test item all False - if True then False Positive

test_false_positives(bloom, existing_items, test_items)


# Example 2 - Testing Different Data Type
import random

def dna_seq(length):
    dna = ["A", "T", "C", "G"]
    seq = []
    while len(seq) < length:
        d = random.choice(dna)
        seq.append(d)
    return ''.join(seq)

def dna(length, sequences):
    unique_seqs = set()
    while len(unique_seqs) < sequences:
        unique_seqs.add(dna_seq(length))
    return list(unique_seqs)

test_dna = dna(10,100)

bloom = BloomFilter(1000, 0.1)

add_items = test_dna[1:50]
test_items = test_dna[51:100]

test_false_positives(bloom, add_items, test_items)

#Test Random Words - slow in producing words will find list
from random_word import RandomWords

def words(sequences):
    unique_seqs = set()
    while len(unique_seqs) < sequences:
        r = RandomWords()
        unique_seqs.add(r.get_random_word())
    return list(unique_seqs)

test_word = words(100)
bloom = BloomFilter(1000, 0.1)

add_items = test_word[1:50]
test_items = test_word[51:100]

test_false_positives(bloom, add_items, test_items)
