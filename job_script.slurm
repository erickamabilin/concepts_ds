#!/bin/bash -l
#SBATCH --account=lp_h_ds_2023_2024
#SBATCH --cluster=wice
#SBATCH --nodes=1
#SBATCH --time=01:00:00

# Load the Python module
module load Python/3.10.8-GCCcore-12.2.0

# Set PYTHONPATH to include user-installed packages and the script directory
export PYTHONPATH="${VSC_DATA}/python_lib/lib/python3.10/site-packages/:/vsc-hard-mounts/leuven-user/363/vsc36376:${PYTHONPATH}"


python performance_test.py