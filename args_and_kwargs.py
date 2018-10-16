#
# No.1 - The using of args and kwargs 
#
# args - 用于在不确定传入多少个参数的情况下
# kwargs - 用于在不确定传入多少个关键字参数的情况下
def func_args(*args,**kwargs):
    print ('args = ', args)
    print ('kwargs = ',kwargs)

# calling functions
print("1-----")
func_args(1,2,3,4,'a')

print('2-----')
func_args(kwwords1 = 1, kwords2 = 2, kwords3 = 3, kwords = 4)  # 返回一个字典

print('3-----')
func_args(10,20,30,'ACB++==', ky1 = 'a', ky2 = 'b',ky3 = 'c')

# No.2 - 可Hash: 通过key来计算values的存储位置,通过key计算位置的算法叫做Hash算法
# dict = {keys:values} - key要求是不可变的类型才可以作为key, 字符串和整数是不可变的，list是可变的不能作为key
# 
# 
# No.3 - set和dict的原理类似,set中存放的是key,但是没有value,同时key要求是不能可变的对象
# 同时set要求里面的数据没有顺序且没有重复的key

# N.4 - Class 的简单实现
print('---------------------Divided Line ------------------')
class Person:
    def __init__(self,name,age,location):
        self.name = name
        self.age  = age
        self.location = location
    
    def DetailInfor(self):
        print('Your name is:',self.name)
        print('And age is :',self.age)
        print('Location is :',self.location)


Peter =  Person('Peter','192','American')
Peter.DetailInfor()

### No.5 --- 
print("No.5 : Set add and remove:")
alist = [1,3,3,3,4,3,2,2,2,12,32,33]
s = set(alist)
# add or remove key 
s1 = s.add(12)
s2 = s.add(123)
s3 = s.remove(3)
