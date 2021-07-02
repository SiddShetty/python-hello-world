import random

def test_rand():
    random.seed(100)
    a = random.randint(1,10)
    print(a)
    random.seed(100)
    b = random.randint(1, 10)
    print(b)
    assert a==b

# if __name__ == '__main__':
#     rand_test()