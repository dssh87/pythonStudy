# List(리스트)
score = [80, 90, 100, 77, 85]
print(type(score))
print(score)
score[1] = 92
print(score)

# Tuple(튜플)
T = (1,3,5,7)
print(type(T))
# tuple은 mutable 하기 때문에 에러발생
T[1]=2
print(T)

# set(집합)
data = {1,2,3,4,5}
print(type(data))

# dict(사전)
school={1:200, 2:220, 3:170}
print(type(school))