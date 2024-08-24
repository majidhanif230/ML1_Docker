# file_processor.py
with open("input.txt", 'r') as infile:
    lines = infile.readlines()

line_count = len(lines)

with open('output.txt', 'w') as outfile:
    outfile.write(f'Number of lines: {line_count}')
