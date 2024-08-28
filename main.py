import argparse
import os
from src.function import print_values

parser = argparse.ArgumentParser(description="Just an example",
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-a", "--num_a", help="value of num_a")
parser.add_argument("-b", "--num_b", help="value of num_b")
args = vars(parser.parse_args())

try:
    num_a = int(args['num_a'])
    num_b = int(args['num_b'])
    print_values(num_a, num_b)
except (TypeError, ValueError):
    print("Error: You must supply integer values for num_a and num_b.")
    print("See example below:")
    print("    python main.py --num_a 1 --num_b 2")