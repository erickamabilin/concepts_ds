# Script for performance benchmarking on HPC
import random
import time
import matplotlib.pyplot as plt
from bloom_filter import BloomFilter

def load_english_words(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def words(sequences, word_list):
    unique_seqs = set()
    while len(unique_seqs) < sequences:
        unique_seqs.add(random.choice(word_list))
    return list(unique_seqs)

def performance_test(bloom_capacity, error_rate, samples, operation):
    nr_runs = 10
    times = {}

    for sample in samples:
        bloom = BloomFilter(bloom_capacity, error_rate)
        for word in sample:
            bloom.add(word)

        sample_size = len(sample)
        if sample_size < 20:
            insert_sample = sample  
        else:
            insert_sample = random.sample(sample, k=20)

        times[sample_size] = 0.0
        for _ in range(nr_runs):
            start_time = time.time_ns()
            for dna in insert_sample:
                if operation == 'add':
                    bloom.add(word)
                elif operation == 'check':
                    bloom.check(word)
            end_time = time.time_ns()
            times[sample_size] += end_time - start_time
        times[sample_size] /= nr_runs*1_000_000.0

    return times


def false_positive_rate_test(bloom_capacity, error_rate, samples):
    false_positives = {}
    for sample in samples:
        bloom = BloomFilter(bloom_capacity, error_rate)
        for word in sample:
            bloom.add(word)

        sample_size = len(sample)
        test_sample = random.sample(performance_word, k=sample_size)
        false_positive_count = sum(1 for item in test_sample if bloom.check(item) and item not in sample)
        false_positive_rate = false_positive_count / sample_size
        false_positives[sample_size] = false_positive_rate * 100  # in percentage
    
    return false_positives

def compression_rate_test(bloom_capacity, error_rate, samples):
    compression_rate = {}
    for sample in samples:
        bloom = BloomFilter(bloom_capacity, error_rate)
        for word in sample:
            bloom.add(word)

        sample_size = len(sample)
        test_sample = random.sample(performance_word, k=sample_size)
        false_positive_count = sum(1 for item in test_sample if bloom.check(item) and item not in sample)
        false_positive_rate = false_positive_count / sample_size
        compression_rate = false_positive_rate / error_rate
    
    return compression_rate

def plot_false_positive_rate(false_positives, title, filename):
    plt.clf()
    plt.plot(false_positives.keys(), false_positives.values())
    plt.xlabel('Number of Elements')
    plt.ylabel('False Positive Rate (%)')
    plt.title(title)
    plt.savefig(filename)
    plt.show()

def plot_times (times, title, filename):
    plt.clf()
    plt.plot(times.keys(), times.values())
    plt.xlabel('Number of Elements')
    plt.ylabel('Time (ms)')
    plt.title(title)
    plt.savefig(filename)
    plt.show()

def plot_compression_rate(compression_rate, title, filename):
    plt.clf()
    plt.plot(compression_rate.keys() , compression_rate.values())
    plt.xlabel('Number of Elements')
    plt.ylabel('Compression Rate (%)')
    plt.title(title)
    plt.savefig(filename)
    plt.show()

if __name__ == "__main__":
    english_words = load_english_words('words.txt')
    performance_word = words(100000, english_words)
    sizes = [100, 500, 1000, 5000, 20000, 40000, 60000, 80000, 100000]
    samples = [random.sample(performance_word, k=size) for size in sizes]

    # Test 1: Add operation with Bloom filter capacity of 100000 and error rate of 0.1
    times = performance_test(100000, 0.1, samples, 'add')
    print(times)
    plot_times(times, 'Bloom Filter Add Operation (Capacity 100000, Error Rate 0.1)', 'add_operation_100000_0.1_word.png')

     # Test 2: Check operation with Bloom filter capacity of 100000 and error rate of 3
    times = performance_test(100000, 3, samples, 'check')
    print(times)
    plot_times(times, 'Bloom Filter Check Operation (Capacity 100000, Error Rate 3)', 'check_operation_100000_3_word.png')

    # Test 3: Add operation with Bloom filter capacity of 10000 (beyond capacity test)
    times = performance_test(50000, 0.1, samples, 'add')
    print(times)
    plot_times(times, 'Bloom Filter Add Operation (Capacity 50000, Error Rate 0.1)', 'add_operation_50000_0.1_word.png')

    # Test 4: Check operation with Bloom filter capacity of 50000 (beyond capacity test)
    times = performance_test(50000, 3, samples, 'check')
    print(times)
    plot_times(times, 'Bloom Filter Check Operation (Capacity 50000, Error Rate 3) - Beyond Capacity', 'check_operation_50000_3_beyond_word.png')`

    # Test 5: False positive rate test
    false_positives = false_positive_rate_test(100000, 0.1, samples)
    print(false_positives)
    plot_false_positive_rate(false_positives, 'Bloom Filter False Positive Rate (Capacity 100000, Error Rate 0.1)', 'false_positive_rate_100000_0.1_word.png')

    # Test 6: False positive rate test - Beyond Capacity
    false_positives = false_positive_rate_test(50000, 0.1, samples)
    print(false_positives)
    plot_false_positive_rate(false_positives, 'Bloom Filter False Positive Rate (Capacity 50000, Error Rate 0.1)', 'false_positive_rate_beyond_50000_0.1_word.png')

    # Test 7: False positive rate test - Compression Rate
    compression_rate = compression_rate_test(50000, 0.1, samples)
    print(compression_rate)
    plot_compression_rate(compression_rate, 'Bloom Filter Compression Rate (Capacity 50000, Error Rate 0.1)', 'compression_rate_100000_0.1_word.png')

    # Test 8: False positive rate test
    false_positives = false_positive_rate_test(100000, 3, samples)
    print(false_positives)
    plot_false_positive_rate(false_positives, 'Bloom Filter False Positive Rate (Capacity 100000, Error Rate 3)', 'false_positive_rate_100000_3_word.png')
    
    # Test 9: False positive rate test - Beyond Capacity
    false_positives = false_positive_rate_test(50000, 3, samples)
    print(false_positives)
    plot_false_positive_rate(false_positives, 'Bloom Filter False Positive Rate (Capacity 50000, Error Rate 3)', 'false_positive_rate_beyond_50000_3_word.png')

    # Test 10: False positive rate test - Compression Rate
    compression_rate = compression_rate_test(100000, 3, samples)
    print(compression_rate)
    plot_compression_rate(compression_rate, 'Bloom Filter Compression Rate (Capacity 100000, Error Rate 3)', 'compression_rate_100000_3_word.png')

    # Test 11: False positive rate test
    false_positives = false_positive_rate_test(100000, 0.5, samples)
    print(false_positives)
    plot_false_positive_rate(false_positives, 'Bloom Filter False Positive Rate (Capacity 100000, Error Rate 0.5)', 'false_positive_rate_100000_0.5_word.png')
    
    # Test 12: False positive rate test - Beyond Capacity
    false_positives = false_positive_rate_test(50000, 0.5, samples)
    print(false_positives)
    plot_false_positive_rate(false_positives, 'Bloom Filter False Positive Rate (Capacity 50000, Error Rate 0.5)', 'false_positive_rate_beyond_50000_0.5_word.png')

    # Test 13: False positive rate test - Compression Rate
    compression_rate = compression_rate_test(100000, 0.5, samples)
    print(compression_rate)
    plot_compression_rate(compression_rate, 'Bloom Filter Compression Rate (Capacity 100000, Error Rate 0.5)', 'compression_rate_100000_0.5_word.png')

    # Test 14: False positive rate test
    false_positives = false_positive_rate_test(100000, 0.3, samples)
    print(false_positives)
    plot_false_positive_rate(false_positives, 'Bloom Filter False Positive Rate (Capacity 100000, Error Rate 0.3)', 'false_positive_rate_100000_0.3_word.png')
    
    # Test 15: False positive rate test - Beyond Capacity
    false_positives = false_positive_rate_test(50000, 0.3, samples)
    print(false_positives)
    plot_false_positive_rate(false_positives, 'Bloom Filter False Positive Rate (Capacity 50000, Error Rate 0.3)', 'false_positive_rate_beyond_50000_0.3_word.png')

    # Test 16: False positive rate test - Compression Rate
    compression_rate = compression_rate_test(100000, 0.3, samples)
    print(compression_rate)
    plot_compression_rate(compression_rate, 'Bloom Filter Compression Rate (Capacity 100000, Error Rate 0.3)', 'compression_rate_100000_0.3_word.png')

