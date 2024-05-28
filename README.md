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
- Ericka Mae Mabilin (2261307)

## Conclusion
The Bloom filter provides an efficient means of membership testing, with performance and false positive rates analyzed using both DNA sequences and English words. The implementation follows an object-oriented approach, ensuring modularity and readability.

### Performance Analysis on HPC
The performance analysis was conducted on the HPC infrastructure provided by the Vlaams Supercomputer Centrum (VSC). The tests included:

1. **Add Operation (Capacity 100000, Error Rate 0.1):**
    - The time taken to add elements remained relatively constant, indicating efficient performance even as the number of elements increased.

2. **Add Operation (Capacity 50000, Error Rate 0.1):**
    - The results showed similar efficiency with slight variations due to reduced capacity.

3. **Check Operation (Capacity 100000, Error Rate 3):**
    - The check operation was highly efficient, with minimal time required even with a high number of elements.

4. **False Positive Rate (Capacity 100000, Error Rate 0.1):**
    - The false positive rate increased with the number of elements, reaching a peak and then declining. This behavior requires further investigation but indicates that the Bloom filter might not function optimally under certain conditions.

5. **False Positive Rate (Capacity 50000, Error Rate 0.1):**
    - The false positive rate started low and gradually increased, reaching a higher peak compared to the larger capacity filter. This is expected as the smaller Bloom filter reaches its capacity faster, resulting in more collisions and higher chances of false positives.

The Bloom filter works best when the number of elements is significantly lower than its capacity. As the number of elements approaches the capacity, the false positive rate increases, showing the limitations of the filter.

The decline in the false positive rate after the peak needs further investigation. It may be due to specific implementation details or characteristics of the dataset used.

Overall, the Bloom filter demonstrates its effectiveness for space-efficient membership testing, with clear trade-offs in terms of false positives and performance as the capacity is approached. The detailed results and analyses are available in the `demo.ipynb` file.
