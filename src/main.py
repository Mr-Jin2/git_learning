import numpy
import os

if __name__ == '__main__':
    with open(os.getcwd()+"/logs/log",'w') as fp:
        fp.write('writting log')
    print('hello docker')



