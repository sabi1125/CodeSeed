import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-l", "--language", help="Specifies the programming language")

args = parser.parse_args()
if args.language:
    print("Creating folders for " + args.language)
