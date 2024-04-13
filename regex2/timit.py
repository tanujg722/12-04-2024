def func_one(n):
    return[str(num) for num in range(n)]
print(func_one(10))

def func_two(n):
    return list(map(str,range(n)))
print(func_two(10))

import time
# Current time before
start_time = time.time()
# run code
result = func_one(100000)
# Current time after running code
end_time = time.time()
# elapsed time
elapsed_time = end_time - start_time
print(elapsed_time)

# Current time before
start_time = time.time()
# run code
result = func_two(100000)
# Current time after running code
end_time = time.time()
# elapsed time
elapsed_time = end_time - start_time
print(elapsed_time)


import timeit

stmt = '''
func_one(100)
'''
setup = '''
def func_one(n):
    return[str(num) for num in range(n)]
'''
print(timeit.timeit(stmt,setup,number=1000000))

stmt2 = '''
func_two(100)
'''
setup2 = '''
def func_two(n):
    return list(map(str,range(n)))
'''
print(timeit.timeit(stmt,setup,number=1000000))

%%timeit
func_one(100)