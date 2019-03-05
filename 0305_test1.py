#리스트
#제너레이터
import  sys

def test_list(nums):
    result = []
    for x in nums:
        result.append(x * x)
    return result

def test_gene(nums):
    for x in nums:
        yield  x * x

a= test_list([1,2,3,4,5])
print(a)
print(sys.getsizeof(a))

print(test_list([1,2,3,4,5]))
print(type(test_list([1,2,3,4,5])))

b = test_gene([1,2,3,4,5])
print(test_gene([1,2,3,4,5]))
print(type(test_gene([1,2,3,4,5])))

print(next(b))