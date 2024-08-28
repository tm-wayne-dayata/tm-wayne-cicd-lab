import argparse
import os
from src.function import print_values

parser = argparse.ArgumentParser(description="Just an example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-a", "--num_a", help="value of num_a")
parser.add_argument("-b", "--num_b", help="value of num_b")
args = vars(parser.parse_args())

num_a = int(args['num_a'])
num_b = int(args['num_b'])

print_values(num_a, num_b)