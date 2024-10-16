'''
6 (12 14 17 27 33)
7 (5  7)
'''
#6-12
def combine(t1,t2):
    return t1+t2
#6-14
def add_n(lst,n=0):
    new_lst = []
    for num in lst :
        new_lst.append(num+n)
    return new_lst
#6-17
def make_dict(keys,values=None):
    if values is None:
        values = [0] * len(keys)
    return dict(zip(keys, values))
#6-27
def lambda_new(lst):
    new_lst = []
    for num in lst:
        if 0 < num < 255:
            new_lst.append(num)
    return new_lst
 #6-33
def gen(n):
    new_list= []
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 != 0:
            new_list.append(num)    
    return new_list
#7-5
import math
class Sphere:
    def __init__(self, radius):
        self.radius = radius
    def volume(self):
        return (4/3) * math.pi * self.radius**3
    def surface_area(self):
        return 4 * math.pi * self.radius**2
    def __repr__(self):
        return f"Sphere(radius={self.radius})"
    def __str__(self):
        return f"Sphere object, rad={self.radius}, volume={self.volume():.2f}, surface_area={self.surface_area():.2f}"


#7-7
class Employee:
    payRate = [1, 1.2, 1.5]  # 給付的比率
    def __init__(self, base):
        self.baseSalary = base

    def salary(self, hr, bonus):
        hourly_rate = self.baseSalary * self.payRate[bonus]
        total_salary= hourly_rate * hr
        return int(total_salary)

    @classmethod
    def set_payRate(cls, new_payRate):
        cls.payRate = new_payRate

    @staticmethod
    def estimate(bs, hr, rate):
        return int(bs * hr * rate)




#test   
print("-Q.12---------------------")
print(combine((1,3),(2,5,6)))
print("-Q.14---------------------")
print(add_n((1,2,3,4),))# n不給值
print(add_n((1,2,3,4),2))
print("-Q.17---------------------")
print(make_dict([0,1,2,3])) #values 不給值
print(make_dict([0,1,2],[12,32,3]))
print("-Q.27---------------------")
print(lambda_new([-3,6,100,300]))
print("-Q.33---------------------")
print(gen(20))
print("-Q.5---------------------")
sphere = Sphere(5)
print(sphere)
print(repr(sphere))
print("-Q.7---------------------")
# 創建一個員工實例
tom = Employee(160)
# 計算工作 8 小時，獎金等級為 1 的員工薪資
print(tom.salary(10, 1))  # 輸出: 1920.0
# 更新所有員工的薪資倍率
Employee.set_payRate([1, 1.3, 1.5])
# 再次計算薪資，可以看到薪資倍率已經更新
print(tom.salary(10, 1))  # 輸出: 2080.0
# 使用靜態方法估算薪資
print(Employee.estimate(160, 10, 1.25))  # 輸出: 2000