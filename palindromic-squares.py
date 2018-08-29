# palindromic-squares
# to find palindromic and square integers

def isPalNum(n): # 判断是否回文数
    s = str(n)
    flag = False
    if s == s[::-1]:
        flag = True
    return flag
 
 def isSquareNum(n): # 判断是否平方数
    flag = False
    import math
    if int(math.sqrt(n))**2 == n:
        flag = True
    return flag

#####找到10000以内回文数#####
palNumList = [] 
for i in range(10,100001):
    if isPalNum(i):
        palNumList.append(i)
print(palNumList)
print('回文数个数为：',len(palNumList))

####找到10000以内的平方数####
sqrNumList = []
for i in range(1,100001):
    if isSquareNum(i):
        sqrNumList.append(i)
print(sqrNumList)
print('平方数的个数为：',len(sqrNumList))

#####完全平方数########
result = []
for i in palNumList:
    if i in sqrNumList:
        result.append(i)
print('完全平方数为：',result)
