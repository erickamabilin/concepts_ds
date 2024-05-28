# Bloom Filter Implementation and Analysis

## Project Description
This project implements a Bloom filter, a probabilistic data structure for efficient membership testing with a trade-off of false positives. The project includes performance analysis using different datasets, specifically DNA sequences and English words.


## Installation Instructions
1. Clone the repository from GitHub.
2. Python 3.10 installed.
3. Install the required Python packages

## Usage Instructions
1. To run the performance tests on DNA sequences:
    ```bash
    python performance_test.py
    ```
2. To run the performance tests on English words:
    ```bash
    python performance_test_words.py
    ```


## Files
- `bloom_filter.py`: Contains the implementation of the Bloom filter.
- `test.py`: Contains unit tests for the Bloom filter.
- `performance_test.py`: Script for performance benchmarking using DNA sequences.
- `performance_test_words.py`: Script for performance benchmarking using English words.
- `demo.ipynb`: Jupyter notebook demonstrating the Bloom filter implementation and analysis.
- `job_script.slurm`: SLURM job script for running `performance_test.py` on HPC.
- `job_script_words.slurm`: SLURM job script for running `performance_test_words.py` on HPC.
- `words.txt`: A text file containing a list of English words for benchmarking.

## Contributors
- Andrea Maza León (2365080)
- Ericka Mae Mabilin ()

## Conclusion
The Bloom filter provides an efficient means of membership testing, with performance and false positive rates analyzed using both DNA sequences and English words. The performance tests highlight the efficiency and trade-offs of using Bloom filters in different scenarios.