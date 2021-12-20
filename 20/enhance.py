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

def read_input(lines):
    algo = lines[0]
    image = lines[2:]
    return algo, image

def print_image(image):
    for line in image:
        print(''.join(line))

def compute_output_pixel(i, j, image, algo, step_num):
    window = []
    for n in range(i - 1, i + 2):
        for m in range(j - 1, j + 2):
            if n < 0 or n >= len(image) or m < 0 or m >= len(image[0]):
                window.append(int(step_num % 2 == 1)) # 0 if even, 1 if odd
            else:
                window.append(int(image[n][m] == '#'))

    num = 0
    for b in window:
        num = num * 2 + b

    return algo[num]

def enhance_image(image, algo, step_num):
    out = []

    for i in range(-1, len(image) + 1):
        row = []
        for j in range(-1, len(image[0]) + 1):
            row.append(compute_output_pixel(i, j, image, algo, step_num))
        out.append(row)

    return out

def count_pixels(lines):
    num_pixels = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if lines[i][j] == '#':
                num_pixels += 1

    return num_pixels

if __name__ == '__main__':
    lines = read_lines_from_file('input')
    algo, image = read_input(lines)
    for i in range(50):
        image = enhance_image(image, algo, i)
    print(count_pixels(image))
