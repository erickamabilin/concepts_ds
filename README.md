# Bloom Filter Implementation and Analysis

## Project Description
This project implements a Bloom filter, a probabilistic data structure for efficient membership testing with a trade-off of false positives. The project includes performance analysis using different datasets, specifically DNA sequences and English words.

The complete report of this work, including implementation details, test results, and performance analysis, is presented in the `demo.ipynb` file. This is the most important file where our results are documented.



## Installation Instructions
1. Clone the repository from GitHub.
2. Python 3.10 installed.
3. Install the required Python packages

## Usage Instructions

### Bloom Filter Implementation and Testing
1. To test the the Bloom filter, run:
    ```bash
    python test.py
    ```

### Performance Analysis (HPC)
To run the performance tests on the HPC, use the provided SLURM job scripts.

1. For performance tests on DNA sequences:
    ```bash
    sbatch job_script.slurm
    ```
2. For performance tests on English words:
    ```bash
    sbatch job_script_words.slurm
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