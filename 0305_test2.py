import psutil
import random
import os
import  time

process = psutil.Process(os.getpid())
befo_mem = process.memory_info().rss / 1024 / 1024

name = ['은기', '상현', '해란', '기백', '호근', '관택', '락근']
grade = ['A', 'B', 'c', 'd', 'e', 'f']

def perf_list(nums):
    rst = []
    for x in range(nums):
        emp = {
            'id' : x,
            'name' : random.choice(name),
            'grade' : random.choice(grade)
        }
        rst.append(emp)
        print('>> list')
    return rst

def perf_gene(nums):
    for x in range(nums):
        emp = {
            'id' : x,
            'name' : random.choice(name),
            'grade' : random.choice(grade)
        }
        yield  emp
        print('>> gene')

t1 = time.time()
#test = perf_gene(50000)
test = perf_list(50000)

for v in test:
    print(v)

after_mem = process.memory_info().rss / 1024 / 1024
t2 = time.time()
tot_time = t2 - t1
print('시작 전 메모리 사용량 : {} MB'.format(befo_mem))
print('수행 후 메모리 사용량 : {} MB'.format(after_mem))
print('총 수행 시간 : {:.6f}'.format(tot_time))
