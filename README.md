# Bloom Filter Implementation and Analysis

## Introduction
This project demonstrates the implementation and analysis of a Bloom filter. A Bloom filter is a space-efficient probabilistic data structure used for testing with a possibility of false positives.

## Files
- `bloom_filter.py`: Contains the implementation of the Bloom filter.
- `test.py`: Contains unit tests for the Bloom filter.
- `performance_test.py`: Script for performance benchmarking using DNA sequences.
- `performance_test_words.py`: Script for performance benchmarking using English words.
- `demo.ipynb`: Jupyter notebook demonstrating the Bloom filter implementation and analysis.
- `job_script.slurm`: SLURM job script for running `performance_test.py` on HPC.
- `job_script_words.slurm`: SLURM job script for running `performance_test_words.py` on HPC.
- `words.txt`: A text file containing a list of English words for benchmarking.

## Requirements
- Python 3.10
- `mmh3` library
- `matplotlib` library

## Installation
1. Clone the repository.
2. Install the required libraries using pip:
   ```sh
   pip install mmh3 matplotlib
