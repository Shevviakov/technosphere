import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', type=str, nargs='+', help='Input args', required=True, dest="input_args")

args = parser.parse_args()

arglist = map(lambda x: x.strip(), args.input_args)

if __name__ == '__main__':
    for arg in arglist:
        print arg
