#!/usr/bin/env python3

import sys

separator = input('Write the separator you want to use: ')
print('\nPaste or write every line that you want to put together')
lines = sys.stdin.readlines()

output = []

[output.append(line.replace('\n', separator)) for line in lines]

print('\n')
print(''.join(output).strip(separator))




