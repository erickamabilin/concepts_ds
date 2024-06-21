import unittest
import random
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
        print(f"False positive over actual size beyond capacity: {false_positives/bloom_filter.counter:.2%}")
    else:
        print(f"Capacity not yet reached")

    print(f"Compression rate: {(false_positives/bloom_filter.counter)/bloom_filter.error_rate:.2%}")


class TestBloomFilter(unittest.TestCase):
    # Example 1
    def test_basic_false_positives(self):
        bloom = BloomFilter(1000, 0.01)  # 1000 is the expected number of elements, 0.01 is the false positive rate
        existing_items = ["apple", "banana", "orange"]
        test_items = ["grape", "mango", "lemon"]  # Test items, expected to be False (if True, then False Positive)

        print("Basic False Positives Test")
        test_false_positives(bloom, existing_items, test_items)

    # Example 2 - Testing Different Data Type
    def test_dna_sequences_false_positives(self):
        bloom = BloomFilter(1000, 0.1)

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

        random.seed(42)
        test_dna = dna(10, 1000)
        add_items = test_dna[1:500] 
        test_items = test_dna[501:] # test_dna[501:1000]

        print("DNA Sequences False Positives Test")
        test_false_positives(bloom, add_items, test_items)


    # Example 3 - Test Random Words - slow in producing words will find list
    def test_random_words_false_positives(self):
        bloom = BloomFilter(1000, 0.01)

        def load_english_words(file_path):
            with open(file_path, 'r') as file:
                return [line.strip() for line in file]

        def generate_random_words(sequences, word_list):
            unique_seqs = set()
            while len(unique_seqs) < sequences:
                unique_seqs.add(random.choice(word_list))
            return list(unique_seqs)

        random.seed(42)
        english_words = load_english_words('words.txt')
        test_words = generate_random_words(1000,english_words)
        add_items = test_words[:500] #[1:50]
        test_items = test_words[501:] #[501:1000]

        print("Random Words False Positives Test")
        test_false_positives(bloom, add_items, test_items)


if __name__ == "__main__":
    unittest.main()
