import logging


logging.basicConfig(filename='logging.log',level=logging.INFO)

def fun(fn):
    print("This is fun!")
    logging.info("fun is running\n")
    def infun(*args):
        print("This is infun!")
        logging.info("infun is running")
    return infun

@fun
def decroate_func(a, b):
    print(a + b)

if __name__ == '__main__':
    decroate_func(1, 2)
