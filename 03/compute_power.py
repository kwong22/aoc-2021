#!/usr/bin/python

def read_lines_from_file(fname):
    """Builds list of strings line-by-line from a file.

    Args:
        fname: name of file to read from
    Returns:
        List of strings
    """
    output = []
    with open(fname, 'r') as lines:
        for line in lines:
            line = line.strip()
            output.append(line)
    return output

def read_ints_from_file(fname):
    lines = read_lines_from_file(fname)
    return [int(line) for line in lines]

def count_increases(depths):
    """Counts number of increases between consecutive integers.

    Args:
        depths: list of integers representing depths
    Returns:
        Number of increases between consecutive integers
    """
    if len(depths) < 2:
        return 0

    num_increases = 0

    for i in range(1, len(depths)):
        if depths[i] > depths[i - 1]:
            num_increases += 1

    return num_increases

def convert_binary_to_decimal(list_bits):
    """Converts list of binary digits to decimal integer.

    Args:
        list_bits: list of binary digits
    Returns:
        Decimal integer
    """
    out = 0
    for x in list_bits:
        out = out * 2 + x

    return out

def compute_power(numbers):
    """Computes power consumption from list of binary numbers.

    Gamma rate = most common bit in each position
    Epsilon rate = least common bit in each position
    Power conspmution = gamma rate * epsilon rate

    Args:
        numbers: list of strings representing binary numbers
    Returns:
        Power consumption
    """
    gamma_bits = []
    eps_bits = []

    # number of bits in each number
    num_bits = len(numbers[0])

    # number of numbers
    num_nums = len(numbers)

    for i in range(num_bits):
        col_count = 0
        for j in range(num_nums):
            col_count += int(numbers[j][i])

        if col_count > num_nums / 2:
            gamma_bits.append(1)
            eps_bits.append(0)
        else:
            gamma_bits.append(0)
            eps_bits.append(1)

    gamma = convert_binary_to_decimal(gamma_bits)
    eps = convert_binary_to_decimal(eps_bits)

    return gamma * eps

def compute_rating(numbers, o2=True):
    ids = list(range(len(numbers)))
    
    # number of bits in each number
    num_bits = len(numbers[0])

    curr_bit = 0

    # Assume one number remains before all digits have been seen
    while len(ids) > 1: 
        # Determine most (or least) common value in current bit position
        col_count = 0
        for j in range(len(ids)):
            col_count += int(numbers[ids[j]][curr_bit])

        common = int(o2) # 1 for O2 if equal, otherwise 0
        if o2:
            # Select most common bit for O2 rating
            if col_count < len(ids) / 2:
                common = 0
        else:
            # Select least common bit for CO2 rating
            if col_count < len(ids) / 2:
                common = 1

        # Remove ids of numbers that do not match
        ids = [num_id for num_id in ids if int(numbers[num_id][curr_bit]) ==
                common]

        curr_bit += 1

    return convert_binary_to_decimal([int(x) for x in numbers[ids[0]]])

def compute_life_support(numbers):
    """Compute life support rating.

    Args:
        numbers: list of strings representing binary numbers
    Returns:
        Life support rating
    """
    o2 = compute_rating(numbers, o2=True)
    co2 = compute_rating(numbers, o2=False)
    print(o2, co2)
    return o2 * co2

if __name__ == '__main__':
    print('Power: {}'.format(compute_power(read_lines_from_file('input'))))
    print('Rating: {}'.format(compute_life_support(read_lines_from_file('input'))))
