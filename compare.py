import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--model", type=str, prompt="explain recursion simply")
args = parser.parse_args()
