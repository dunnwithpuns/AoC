

def find_calib_val(doc):
    with open(doc) as f:
        text = f.read()

    lines = doc.split("\n")
    sums = []

    for line in lines:
        sums.append(find_line_val(line))

    return sums


def find_line_val(line):
    # split the line by character 
    split_line = list(line)
    nums = []
    
    # find and track each digit per line
    for i in split_line:
        if i.isdigit():
            nums.append(i)

    # store the first and last digits 
    final_digits = [nums[0], nums[-1]]
    
    # return the concatenated int
    return int("".join(final_digits))