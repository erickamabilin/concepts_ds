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

performance_dna = dna(10,100000)

sizes = [100, 500, 1_000, 5_000, 10_000, 20_000, 30_000, 40_000, 50_000]

samples = [
    random.sample(performance_dna, k=size) for size in sizes
]

# Check bloom.add max capacity of BloomFilter 50000
nr_runs = 10
times = {}
insert_sample = random.sample(performance_dna, k=20)
for sample in samples:
    bloom = BloomFilter(50000,0.1)
    for dna in sample:
        bloom.add(dna)
    times[len(sample)] = 0.0
    for _ in range(nr_runs):
        start_time = time.time_ns()
        for dna in insert_sample:
            bloom.add(dna)
        end_time = time.time_ns()
        times[len(sample)] += end_time - start_time
    times[len(sample)] /= nr_runs*1_000_000.0
print(times)

plt.plot(times.keys(), times.values())

# Check bloom.check max capacity of BloomFilter 50000
nr_runs = 10
times = {}
insert_sample = random.sample(performance_dna, k=20)
for sample in samples:
    bloom = BloomFilter(50000,3)
    for dna in sample:
        bloom.add(dna)
    times[len(sample)] = 0.0
    for _ in range(nr_runs):
        start_time = time.time_ns()
        for dna in insert_sample:
            bloom.check(dna)
        end_time = time.time_ns()
        times[len(sample)] += end_time - start_time
    times[len(sample)] /= nr_runs*1_000_000.0
print(times)

plt.plot(times.keys(), times.values())

# Check bloom.add max capacity of BloomFilter 10000 (run of > 10000 will be beyond capacity)
nr_runs = 10
times = {}
insert_sample = random.sample(performance_dna, k=20)
for sample in samples:
    bloom = BloomFilter(50000,0.1)
    for dna in sample:
        bloom.add(dna)
    times[len(sample)] = 0.0
    for _ in range(nr_runs):
        start_time = time.time_ns()
        for dna in insert_sample:
            bloom.add(dna)
        end_time = time.time_ns()
        times[len(sample)] += end_time - start_time
    times[len(sample)] /= nr_runs*1_000_000.0
print(times)

plt.plot(times.keys(), times.values())

# Check bloom.check max capacity of BloomFilter 50000 (run of > 10000 will be beyond capacity)
nr_runs = 10
times = {}
insert_sample = random.sample(performance_dna, k=20)
for sample in samples:
    bloom = BloomFilter(50000,3)
    for dna in sample:
        bloom.add(dna)
    times[len(sample)] = 0.0
    for _ in range(nr_runs):
        start_time = time.time_ns()
        for dna in insert_sample:
            bloom.check(dna)
        end_time = time.time_ns()
        times[len(sample)] += end_time - start_time
    times[len(sample)] /= nr_runs*1_000_000.0
print(times)

plt.plot(times.keys(), times.values())