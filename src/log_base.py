import logging

# formatter = logging.Formatter("%(asctime)s - %(message)s")
# handler = logging.FileHandler('../logs/log',encoding='utf-8')

logging.basicConfig(
    level=logging.INFO,
    format = '[%(levelname)s] %(asctime)s-%(filename)s-%(lineno)d : %(message)s',
    filename='../logs/mylog',
    filemode='a'
)


d = {'a':'jyz','b':'jyw'}
for i in d:
    print(i)