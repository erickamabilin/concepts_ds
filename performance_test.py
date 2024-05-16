# Script for performance benchmarking on HPC
import random
import time
import matplotlib.pyplot as plt
from bloom_filter import BloomFilter

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

def performance_test (bloom_capacity, error_rate, samples, operation):
    nr_runs = 10
    times = {}

    for sample in samples:
        bloom = BloomFilter(bloom_capacity, error_rate)
        for dna in sample:
            bloom.add(dna)

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
                    bloom.add(dna)
                elif operation == 'check':
                    bloom.check(dna)
            end_time = time.time_ns()
            times[sample_size] += end_time - start_time
        times[sample_size] /= nr_runs*1_000_000.0
    
    return times

def plot_times (times, title, filename):
    plt.plot(times.keys(), times.values())
    plt.xlabel('Number of Elements')
    plt.ylabel('Time (ms)')
    plt.title(title)
    plt.savefig(filename)
    plt.show()

if __name__ == "__main__":
    performance_dna = dna(10, 100000)
    sizes = [100, 500, 1000, 5000, 10000, 20000, 30000, 40000, 50000]
    samples = [random.sample(performance_dna, k=size) for size in sizes]

    times = performance_test(50000, 0.1, samples, 'add')
    print(times)
    plot_times(times, 'Bloom Filter Add Operation (Capacity 50000, Error Rate 0.1)', 'add_operation_50000_0.1.png')

    times = performance_test(50000, 3, samples, 'check')
    print(times)
    plot_times(times, 'Bloom Filter Check Operation (Capacity 50000, Error Rate 3)', 'check_operation_50000_3.png')
