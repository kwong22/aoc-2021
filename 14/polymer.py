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

def add_to_dict(k, v, d):
    if k in d:
        d[k] += v
    else:
        d[k] = v

def polymerize(lines, num_steps):
    template = lines[0]
    
    rules = {}

    for i in range(2, len(lines)):
        rule = lines[i].split()
        rules[rule[0]] = rule[-1]

    for _ in range(num_steps):
        new_template = [template[0]]

        for i in range(1, len(template)):
            pattern = template[i - 1] + template[i]
            new_template.append(rules[pattern])
            new_template.append(template[i])

        template = new_template
    
    counts = {}
    for c in template:
        add_to_dict(c, 1, counts)

    counts_list = [(key, val) for key, val in counts.items()]
    counts_list = sorted(counts_list, key=lambda x: x[1])

    return counts_list[-1][1] - counts_list[0][1]

def polymerize2(lines, num_steps):
    # Load template
    template = lines[0]
    pairs = {}

    # Convert template to pairs
    for i in range(1, len(template)):
        pair = template[i - 1] + template[i]
        add_to_dict(pair, 1, pairs)
    
    # Load rules
    rules = {}

    for i in range(2, len(lines)):
        rule = lines[i].split()
        rules[rule[0]] = rule[-1]

    # Run pair insertion rules
    for _ in range(num_steps):
        new_pairs = {}
        for key in pairs.keys():
            if pairs[key] > 0:
                insertion = rules[key]
                key1 = key[0] + insertion
                key2 = insertion + key[1]
                
                add_to_dict(key1, pairs[key], new_pairs)
                add_to_dict(key2, pairs[key], new_pairs)
        pairs = new_pairs

    counts = {}
    for key in pairs.keys():
        c1 = key[0]
        c2 = key[1]
        add_to_dict(c1, pairs[key], counts)
        add_to_dict(c2, pairs[key], counts)

    # Double counted all but first and last characters
    add_to_dict(template[0], 1, counts)
    add_to_dict(template[-1], 1, counts)

    # Divide by 2 because double counted
    counts_list = [(key, val // 2) for key, val in counts.items()]
    counts_list = sorted(counts_list, key=lambda x: x[1])

    return counts_list[-1][1] - counts_list[0][1]

if __name__ == '__main__':
    lines = read_lines_from_file('input')
    print(polymerize(lines, 10))
    print(polymerize2(lines, 40))
