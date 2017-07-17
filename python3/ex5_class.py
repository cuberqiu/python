
class A(object):
    def __init__(self):
        print("A INIT")


class B(A):
    def __init__(self):
        super(B, self).__init__()
        super().__init__()
        print("B INIT")


class C(B, A):
    def __init__(self):
        super(C, self).__init__()
        super().__init__()
        print("C INIT")

if __name__ == '__main__':
    # a = A()
    b = B()
    c = C()

