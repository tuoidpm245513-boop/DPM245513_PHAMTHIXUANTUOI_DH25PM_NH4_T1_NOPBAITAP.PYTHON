#Hãy cho biết kết quả của Boolean Expression
#Yêu cầu:
#Cho x, y, z = 3, 5, 7. Hãy cho biết kết quả của Boolean Expression
x, y, z = 3, 5, 7

a = (x == 3)
print("x == 3: ",a)
b = (x < y)
print("x < y: ",b)
c = (x >= y)
print("x >= y: ",c)
d = (x <= y)
print("x <= y: ",d)
e = (x != y - 2)
print("x != y - 2: ",e)
f = (x < 10)
print("x < 10: ",f)
g = (x >= 0 and x < 10)
print("x >= 0 and x < 10: ",g)
h = (x < 0 and x < 10)
print("x < 0 and x < 10:",h)
i = (x >= 0 and x < 2)
print("x >= 0 and x < 2: ",i)
j = (x < 0 or x < 10)
print("x < 0 or x < 10: ",j)
k = (x > 0 or x < 10)
print("x > 0 or x < 10: ",k)
l = (x < 0 or x > 10)
print("x < 0 or x > 10: ",l)