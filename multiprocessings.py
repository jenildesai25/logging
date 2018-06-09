import multiprocessing

def count(num):
    num = num + 1
    return subtract(num)

def subtract(num):
    num = num - 1
    return count(num)

if __name__ == "__main__":
    print(multiprocessing.cpu_count())


