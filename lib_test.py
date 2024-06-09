from random import randint


def save_result(func):
    func_results = dict()

    def wrapper(*args, **kwargs):
        nonlocal func_results
        try:
            print(f"try : {func_results[*args]}")
            return func_results
        except KeyError:
            func_results[*args] = func(*args)
            print(f"except : {func_results[*args]}")
            return func_results
    return wrapper


@save_result
def f(n):
    return n * 123456789


length_test = []

for _ in range(10):
    for i in range(100):
        f(randint(0, 140))

    list_result = f(0)
    list_result_updated = []

    for i in list_result:
        list_result_updated.append(*i)

    list_result_updated.sort()
    print(f"Length = {len(list_result_updated)}")
    print(f"Unique args = {list_result_updated}")
    print("===============")
    print("===============")
    for i in list_result_updated:
        print(f"{i} = {list_result[(i,)]}")


