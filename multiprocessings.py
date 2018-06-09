# from multiprocessing import Process
#
#
# def PrintSquare(x):
#     return x*x
#
#
# def CheckPrime(x):
#     for i in range(2, x):
#         if x % 2 == 0:
#             print("{} number not a prime number".format(x))
#             break
#     else:
#         print("{} is a prime number".format(x))
#
# if __name__ == "__main__":
#     from time import time
#     # t = time()
#     p1 = Process(target=PrintSquare,args=(1,))
#     p2 = Process(target=CheckPrime,args=(2,))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     # print('after joining the processes',time() - t)
#

from multiprocessing import Process, Queue


def is_even(numbers, q):
    for n in numbers:
        if n % 2 == 0:
            q.put(n)


if __name__ == "__main__":
    q = Queue()
    p = Process(target=is_even,args=(range(20),q))
    p.start()
    p.join()
    # print(q)
    while q:
        print(q.get())