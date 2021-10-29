"""
抽象出一个基类，知道要有哪些方法，但只是抽象方法，并不实现功能，只能被继承，而不能被实例化，
但继承的子类必须要实现该方法。这时就需要用到抽象基类，在很多时候用得到。
抽象基类会用到abc模块
"""
from abc import ABC, abstractmethod

# 抽象基类不能实例化
class Foo(ABC):
    @abstractmethod
    def fun(self):
        print("this is an abstract method.")

# 子类必须重写fun 方法，不然实例化子类SubFoo同样报错
class SubFoo(Foo):
    # 抽象方法可以有实现代码。即便实现了，子类也必须覆盖抽象方法，
    # 但是在子类中可以使用 super() 函数调用抽象方法，为它添加功能，而不是从头开始实现。
    def fun(self):
        return super().fun()
    def f(self):
        print("this is a f method of SubFoo.")

# 抽象基类只能继承而不能实例化，子类要实例化，必须先实现抽象基类中的抽象方法。

a = SubFoo()
a.fun()
a.f()