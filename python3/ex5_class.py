
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


class task_queue:
    queue = []

    def append(self, obj):
        self.queue.append(obj)

    def print_queue(self):
        print(self.queue)

def test_task():
    a = task_queue()
    b = task_queue()
    c = task_queue()

    a.append('tc_1')

    a.print_queue()
    b.print_queue()
    c.print_queue()

    task_queue.queue.append('t2')
    a.print_queue()
    b.print_queue()
    c.print_queue()


class T:
    num = 0
    # def __init__(self):
    #     self.num = 0

def test_t():
    a = T()
    b = T()
    print(a.num, b.num)


if __name__ == "__main__":
    test_task()
    test_t()


