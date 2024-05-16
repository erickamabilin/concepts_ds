import math
import mmh3


class BloomFilter:
    """
    Bloom Filter implementation for probabilistic set membership testing.

    Attributes:
        size (int): Expected number of elements inserted in the Bloom filter.
        error_rate (float): Desired false positive rate.
        bit_array_size (int): Size of the bit array based on size and error_rate.
        bit_array (list): Bit array used for the Bloom filter.
        num_hashes (int): Number of hash functions used.
        counter (int): Number of elements added to the Bloom filter.
    """

    def __init__(self, size, error_rate):
        """
        Initializes the Bloom filter with the given size and error rate.

        Args:
            size (int): The expected number of elements to be inserted.
            error_rate (float): The desired false positive rate.
        """
        self.size = size
        self.error_rate = error_rate
        self.bit_array_size = self.calculate_bit_array_size(size, error_rate)
        self.bit_array = [0] * self.bit_array_size
        self.num_hashes = self.calculate_num_hashes(size, self.bit_array_size)
        self.counter = 0

    def add(self, item):
        """
        Adds an item to the Bloom filter.

        Args:
            item (str): The item to be added to the Bloom filter.
        """
        for i in range(self.num_hashes):
            hash_val = mmh3.hash(item, i) % self.bit_array_size
            self.bit_array[hash_val] = 1
        self.counter += 1

    def check(self, item):
        """
        Checks if an item is in the Bloom filter.

        Args:
            item (str): The item to be checked.

        Returns:
            bool: True if the item is probably in the Bloom filter,
            False if the item is not in the Bloom filter.
        """
        for i in range(self.num_hashes):
            hash_val = mmh3.hash(item, i) % self.bit_array_size
            if self.bit_array[hash_val] == 0:
                return False
        return True

    def calculate_bit_array_size(self, size, error_rate):
        """
        Calculates the size of the bit array.

        Args:
            size (int): The expected number of elements to be inserted.
            error_rate (float): The desired false positive rate.

        Returns:
            int: The size of the bit array.
        """
        return int(- (size * math.log(error_rate)) / (math.log(2) ** 2))

    def calculate_num_hashes(self, size, bit_array_size):
        """
        Calculates the number of hash functions to use.

        Args:
            size (int): The expected number of elements to be inserted.
            bit_array_size (int): The size of the bit array.

        Returns:
            int: The number of hash functions.
        """
        return int((bit_array_size / size) * math.log(2))
