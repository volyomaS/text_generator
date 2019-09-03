import argparse
import sys
import fit
import generate

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', nargs='?', default='generate')
    parser.add_argument('filename', nargs='?', default='test.txt')
    args = parser.parse_args(sys.argv[1:])
    if args.mode == 'fit':
        curr = fit.Fit(args.filename)
        data = curr.action()
        curr.rewrite(data)
    elif args.mode == 'generate':
        curr = generate.Generate()
        curr.action()
