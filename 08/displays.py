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

def read_display_from_line(line):
    return [x.split() for x in line.split('|')]

def read_displays_from_lines(lines):
    inputs = []
    outputs = []

    for line in lines:
        inp, out = read_display_from_line(line)
        inputs.append(inp)
        outputs.append(out)

    return inputs, outputs

def count_obvious(outputs):
    res = 0

    for o in outputs:
        for x in o:
            if len(x) == 2 or len(x) == 4 or len(x) == 3 or len(x) == 7:
                res += 1

    return res

def chars_to_bits(chars):
    bits = [0] * 7 # Total of 7 segments

    for c in chars:
        bits[ord(c) - ord('a')] = 1

    return ''.join([str(x) for x in bits])

def count_segments(bits):
    return sum([int(x) for x in bits])

def count_differences(b1, b2):
    num_diffs = 0
    for i in range(len(b1)):
        if b1[i] != b2[i]:
            num_diffs += 1

    return num_diffs

def contains_all_bits(b1, b2):
    """Returns True if all bits in b1 are also in b2."""
    for i in range(len(b1)):
        if b1[i] == '1' and b2[i] != '1':
            return False

    return True

def decode_line(inp, out):
    inp = [chars_to_bits(x) for x in inp]
    out = [chars_to_bits(x) for x in out]

    bits_to_idx = {}
    idx_to_bits = [''] * 10 # Total of 10 digits

    five_segs = []
    six_segs = []

    # Determine obvious digits
    for x in inp:
        if count_segments(x) == 2:
            bits_to_idx[x] = 1
            idx_to_bits[1] = x
        elif count_segments(x) == 4:
            bits_to_idx[x] = 4
            idx_to_bits[4] = x
        elif count_segments(x) == 3:
            bits_to_idx[x] = 7
            idx_to_bits[7] = x
        elif count_segments(x) == 7:
            bits_to_idx[x] = 8
            idx_to_bits[8] = x
        elif count_segments(x) == 5:
            five_segs.append(x)
        elif count_segments(x) == 6:
            six_segs.append(x)

    # Determine 5-segment digits
    if count_differences(five_segs[0], five_segs[1]) == 4:
        three = 2
    elif count_differences(five_segs[0], five_segs[2]) == 4:
        three = 1
    else:
        three = 0
    bits_to_idx[five_segs[three]] = 3
    idx_to_bits[3] = five_segs[three]
    five_segs.pop(three)

    if count_differences(five_segs[0], idx_to_bits[4]) == 3:
        five = 0
        two = 1
    else:
        five = 1
        two = 0
    bits_to_idx[five_segs[five]] = 5
    idx_to_bits[5] = five_segs[five]
    bits_to_idx[five_segs[two]] = 2
    idx_to_bits[2] = five_segs[two]

    # Determine 6-segment digits
    if not contains_all_bits(idx_to_bits[5], six_segs[0]):
        zero = 0
    elif not contains_all_bits(idx_to_bits[5], six_segs[1]):
        zero = 1
    else:
        zero = 2
    bits_to_idx[six_segs[zero]] = 0
    idx_to_bits[0] = six_segs[zero]
    six_segs.pop(zero)

    if count_differences(six_segs[0], idx_to_bits[3]) == 1:
        nine = 0
        six = 1
    else:
        nine = 1
        six = 0
    bits_to_idx[six_segs[nine]] = 9
    idx_to_bits[9] = six_segs[nine]
    bits_to_idx[six_segs[six]] = 6
    idx_to_bits[6] = six_segs[six]

    result = 0
    for x in out:
        result = result * 10 + bits_to_idx[x]
    return result

def decode_lines(inputs, outputs):
    result = 0
    for inp, out in zip(inputs, outputs):
        result += decode_line(inp, out)

    return result

if __name__ == '__main__':
    inputs, outputs = read_displays_from_lines(read_lines_from_file('input'))
    print(count_obvious(outputs))
    print(decode_lines(inputs, outputs))

