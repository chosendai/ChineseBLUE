import random
import sys

def train_test_split(infile, test_rate=0.9):
    with open(sys.argv[2], 'w') as f_train, \
            open(sys.argv[3], 'w') as f_test:
        for line in open(infile):
            if random.random() > test_rate:
                f_train.write(line)
            else:
                f_test.write(line)

if __name__ == '__main__':
    train_test_split(sys.argv[1])
