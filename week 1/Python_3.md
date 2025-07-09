> 接续 Python.md 文件的第三部分

## 类

### 类的创建的基本使用

- 创建一个类

    ```Python
    class Dog():
        ''' 文档字符串：这是一次模拟小狗的简单尝试 '''
        def __init__(self,name,age):
            self.name = name
            self.age = age
        
        def sit(self):
            print(self.name.title() + " is now sitting.")
        
        def rollover(self):
            print(self.name.title() + " is now rolling over!")
    ```

    Dog()类中包含两个属性：name 和 age ，以及两个方法 sit() 和 rollover()。类中的函数称为方法，可以通过实例访问到的变量称为属性

    - `__init__()`方法，前后各有两个下划线，这是一个特殊的方法，在根据Dog()类创建实例时，python都会自动运行这个方法。
        - 这个方法中，形参 self 必须有，而且必须位于其他所有参数的前边，因为python在调用`__init__()`创建实例时，将自动传入实参 self
        - 每个与类相关联的方法调用都自动传入实参 self ，它是只想实例本身的引用，让实例能够访问到类中的属性和方法
        - 通过实参向 Dog() 传递 name 和 age 时，self会自动传递，因此不用自己传递它，只用给出后边两个实参
    - 以 self 为前缀的变量可以供类中的所有方法使用，而且还可以通过类的任何实例来访问这些变量
    - `self.name = name` 获取存储在形参 name 中的值，并将其存储在 name 变量中，然后将该变量关联到当前创建的实例
    - sit() 和 rollover() 方法不需要其他信息，因此只有一个形参 self
    - 类名通常是首字母大写，实例是小写

-  创建类的实例，根据类来创建对象称为实例化

    ```Python
    class Dog():
        ''' 文档字符串：这是一次模拟小狗的简单尝试 '''
        def __init__(self,name,age):
            self.name = name
            self.age = age
        
        def sit(self):
            print(self.name.title() + " is now sitting.")
        
        def rollover(self):
            print(self.name.title() + " is now rolling over!")
    
    my_dog = Dog('whill', 6)
    print("My dog's name is " + my_dog.name.title())   # 访问属性通过 句点表示法
    print("My dog's age is " , my_dog.age)
    
    my_dog.sit()
    my_dog.rollover()  # 访问方法通过 句点表示法
    ```



###     使用类和实例

- Car类

    ```Python
    class Car():
        '''一次模拟汽车的简单尝试'''
        
        def __init__(self,make,model,year):
            '''初始化描述汽车的属性'''
            self.make = make
            self.model = model
            self.year = year
        
        def get_descriptive_name(self):
            long_name = str(self.year) + " " + self.make + " " + self.model
            return long_name
        
    my_new_car = Car("Audi", 'a6', 2016)
    print(my_new_car.get_descriptive_name())
    ```

- 给属性指定默认值

    类的每个属性都必须有初始值，可以在`__init__()`方法内指定属性的初始值，此时无需包含为它提供初始值的形参

    ```Python
    class Car():
        '''一次模拟汽车的简单尝试'''
        
        def __init__(self,make,model,year):
            '''初始化描述汽车的属性'''
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0   # 为odometer_reading属性设置的初始值，不用再在形参中给出
        
        def get_descriptive_name(self):
            long_name = str(self.year) + " " + self.make + " " + self.model
            return long_name
        
        def read_odometer(self):
            '''打印汽车总里程'''
            print("Total odometer: " + str(self.odometer_reading) + " miles. ")
    
    my_new_car = Car("Audi", 'a6', 2016)
    print(my_new_car.get_descriptive_name())
    my_new_car.read_odometer()
    ```

- 修改属性的值

    ```Python
    # 法一 通过实例直接访问它(不安全)
    my_new_car = Car("Audi", 'a6', 2016)
    my_new_car.odometer_reading = 23
    my_new_car.read_odometer()
    ```

    ```Python
    class Car():
        '''一次模拟汽车的简单尝试'''
        --snip--
        
    	def update_odometer(self,mileage):
            '''
            将里程表修改为指定的值
            静止将里程表读数往回调
            '''
            if mileage > self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("不允许作弊.")
    my_new_car = Car("Audi", 'a6', 2016)
    my_new_car.update_odometer(23)
    my_new_car.read_odometer()
    ```

- 通过方法对属性的值进行递增

    ```Python
    class Car():
        '''一次模拟汽车的简单尝试'''
        
        def __init__(self,make,model,year):
            '''初始化描述汽车的属性'''
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0   # 为odometer_reading属性设置的初始值，不用再在形参中给出
        
        
        def get_descriptive_name(self):
            long_name = str(self.year) + " " + self.make + " " + self.model
            return long_name
        
        
        def read_odometer(self):
            '''打印汽车总里程'''
            print("Total odometer: " + str(self.odometer_reading) + " miles. ")
        
            
        def update_odometer(self,mileage):
            '''
            将里程表修改为指定的值
            静止将里程表读数往回调
            '''
            if mileage > self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("不允许作弊.")
        
        
        def increment_odometer(self,miles):
            if miles > 0:
            	self.odometer_reading += miles
            else:
            	print("不允许作弊.")
        
    used_car = Car("Audi",'a7',2019)
    print(used_car.get_descriptive_name())
    
    used_car.update_odometer(2650)
    used_car.read_odometer()
    
    used_car.increment_odometer(3000)
    used_car.read_odometer()
    ```


### 继承

- 一个类继承一个类时，它将自动获得被继承类的所有属性和方法，原有的类称为父类或超类，新类称为子类

    ```Python
    class Car():
        '''一次模拟汽车的简单尝试'''
        
        def __init__(self,make,model,year):
            '''初始化描述汽车的属性'''
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0   # 为odometer_reading属性设置的初始值，不用再在形参中给出
        
        
        def get_descriptive_name(self):
            long_name = str(self.year) + " " + self.make + " " + self.model
            return long_name
        
        
        def read_odometer(self):
            '''打印汽车总里程'''
            print("Total odometer: " + str(self.odometer_reading) + " miles. ")
        
            
        def update_odometer(self,mileage):
            '''
            将里程表修改为指定的值
            静止将里程表读数往回调
            '''
            if mileage > self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("不允许作弊.")
        
        
        def increment_odometer(self,miles):
            if miles > 0:
            	self.odometer_reading += miles
            else:
            	print("不允许作弊.")
                
    
    class ElectricCar(Car):
        '''继承了类 Car'''
        def __init__(self,make,model,year):
            '''初始化父类的属性'''
            super().__init__(make,model,year)
            
    my_tesla = ElectricCar("tesla",'model y', 2018)
    print(my_tesla.get_descriptive_name())
    ```

- 创建子类时，父类必须包含在当前文件中，而且必须子类的前边

- 定义子类时，在括号内指定父类的名称`class ElectricCar(Car):`

- `super()`是特殊的函数，使父类和子类关联起来

- 给子类定义自己的特有属性和方法：

    ```Python
    class Car():
    	---snip---
        
    class ElectricCar(Car):
        '''继承了类 Car'''
        def __init__(self,make,model,year):
            # 初始化父类的属性
            super().__init__(make,model,year) 
            # 初始化自己特有的属性
            self.batery_size = 70
            
        def describe_battery(self):
            print("This car has a " + str(self.batery_size) + '-kWh battery.')
    
    my_tesla = ElectricCar("tesla",'model y', 2018)
    print(my_tesla.get_descriptive_name())
    my_tesla.describe_battery()
    ```

- 重写父类的方法（定义一个和父类方法重名的方法）

    ```Python
    class Car():
        ---snip---
        def fill_gas_tank(self):
            '''加油的方法'''
            print("加油中...")
            print("加油完成！")
            
    class ElectricCar(Car):
        def __init__(self,make,model,year):
            super().__init__(make,model,year)
            
        def fill_gas_tank(self):
            '''重写父类方法，电动车没有油箱'''
            print("This car doesn't need a gas tank.")
    ```

    重写父类方法后，在创建子类的实例时，Python会忽略掉原来父类中的方法

- 将实例用作属性

    ```Python
    class Car():
        '''一次模拟汽车的简单尝试'''
        
        def __init__(self,make,model,year):
            '''初始化描述汽车的属性'''
            self.make = make
            self.model = model
            self.year = year
            self.odometer_reading = 0   # 为odometer_reading属性设置的初始值，不用再在形参中给出
        
        
        def get_descriptive_name(self):
            long_name = str(self.year) + " " + self.make + " " + self.model
            return long_name
        
        
        def read_odometer(self):
            '''打印汽车总里程'''
            print("Total odometer: " + str(self.odometer_reading) + " miles. ")
        
            
        def update_odometer(self,mileage):
            '''
            将里程表修改为指定的值
            静止将里程表读数往回调
            '''
            if mileage > self.odometer_reading:
                self.odometer_reading = mileage
            else:
                print("不允许作弊.")
        
        
        def increment_odometer(self,miles):
            if miles > 0:
            	self.odometer_reading += miles
            else:
            	print("不允许作弊.")
    
    class Battery():
        def __init__(self,battery_size=70):
            '''初始化电瓶的属性'''
            self.battery_size = battery_size
            
        def describe_battery(self):
            print("This car has a " + str(self.battery_size) + '-kWh battery.')
            
            
    class ElectricCar(Car):
        def __init__(self,make,model,year):
            super().__init__(make,model,year)
            self.battery = Battery()   # 创建了一个Battery()的实例作为ElectricCar类的属性
    
    my_tesla = ElectricCar("tesla",'model y', 2018)
    print(my_tesla.get_descriptive_name())
    my_tesla.battery.describe_battery()
    ```

    有时候自己的类非常庞大，有非常多的属性和方法，这是可以采用上述方法，将类的一部分作为一个独立的类单独提取出来

    上边新建了一个Battery类，以后想要再对电池做分析就更简洁了

    ```Python
    class Battery():
        def __init__(self,battery_size=70):
            '''初始化电瓶的属性'''
            self.battery_size = battery_size
            
        def describe_battery(self):
            print("This car has a " + str(self.battery_size) + '-kWh battery.')
            
        def get_range(self):
            if self.battery_size == 70:
                range = 240
            elif self.battey_size == 80:
                range = 270
            message = "This car can go approximately " + str(range)
            message += " miles on a full charge."
            print(message)
    ```

### 导入类

- 为了使文件更简洁，Python允许将类存储在模块中，然后在主程序中导入所需的模块

- 可以把多个类放在一个模块中

    ```Python
    # car.py
    class Car():
    	---snip---
        
    class Battery():
        ---snip---
        
    class ElectricCar(Car):
        ---snip---
    ```

- 导入单个类

    ```Python
    from car import Car  # 从 car.py 文件中导入单个类 Car
    ```

- 导入多个类

    ```Python
    from car import Car,ElectricCar  # 多个类之间用逗号分隔
    ```

- 导入整个模块

    ```Python
    import car
    
    my_tesla = car.ElectricCar("tesla",'model y', 2018)  # 需要用句点表达式的方式来访问需要的类
    ```

    使用`module_name.class_name`的方式访问需要的类

- 导入模块中的所有类

    ```Python
    from car import *
    ```

    不推荐使用这种方法，因为可能发生类名冲突

- 从一个模块中导入很多类时，最好是导入整个模块，然后在接下来的代码中使用`module_name.class_name`的方式访问需要的类

- 还可以从一个模块中导入另外一个模块

    ```Python
    # car.py 模块
    class Car():
    	---snip---
    ```

    ```Python
    # electric_car.py 模块
    from car import Car   # 从 car.py模块中导入Car类
    
    class Battery():
        ---snip---
        
    class ElectricCar(Car):
        ---snip---
    ```

    ```Python
    # my_cars.py
    from car import Car
    from electric_car import ElectricCar
    
    my_beetle = Car("volk", 'beetle', 2018)
    print(my_beetle.get_descriptive_name())
    
    my_tesla = ElectricCar("tesla",'model y', 2018)
    print(my_tesla.get_descriptive_name())
    ```

### 自定义工作流程

- 一开始应该尽可能的让结构简单，先尽可能的在一个文件中完成所有的工作，确定一切都能够正常运行后，再将类移到独立的模块中

# 文件

### 从文件中读取数据

```Python
with open('.//FileOP//pi_digits.txt') as file_object:
    contents = file_object.read()  
    print(contents)
    
-->
3.1415926535
  8979323846
  2643383279
			 # 多了一个空行
```

- 使用 **open()** 函数打开文件，并返回一个表示该文件的对象

- 关键字 **with** 在不再需要访问打开的文件后关闭该文件，就不用手动用 **close()** 函数关闭文件，但是不推荐这种做法，因为有的时候程序不能正常运行到 close() 这里导致文件不能够正确的关闭从而导致文件数据受损

- 所以使用 with 结构来让 Python 自己决定在合适的时候关闭文件
- 使用 read() 方法读取目标文件的全部内容，并将其作为一个字符串
- read() 方法到达文件末尾时返回一个空字符串，因此打印出来时会多一个空行，可以使用**rstrip()**去除字符串末尾的空白

### 文件路径

- 使用这种方法时，Python会在当前执行的文件所在的目录中查找文件

    ```Python
    with open('pi_digits.txt') as file_object:
        ---snip---
    ```

- 使用相对路径，这是Python会在当前执行的文件所在的目录中的FileOP文件夹中去找目标文件

    ```Python
    with open('FileOP\pi_digits.txt') as file_object:
        ---snip---
    ```

    windows系统中，使用反斜杠(/)而不是斜杠(\\)，或者使用双斜杠`\\`，这样就可以防止被转义

- 使用绝对路径，因为绝对路径通常比较长，所以经常把它放在一个变量中

    ```Python
    file_path = 'D:\GiteeRepository\python-project\jupyter\FileOP\pi_digits.txt'
    with open(file_path) as file_object:
        ---snip---
    ```

### 逐行读取

- 对文件对象使用for循环，以每次一行的方式检查文件：

    ```Python
    file_path = "FileOP/pi_digits.txt"
    with open(file_path) as file_object:
        for line in file_object:
            print("- " + line)
    
    --->
    - 3.1415926535
    
    -   8979323846
    
    -   2643383279
    
    ```

    每行的末尾都有一个空白行，这是因为在文件中，每行的末尾都有一个换行符，而print语句也会自己加上一个换行符，所以答应出来有一个空行

    可以使用**rstrip()**去除字符串末尾的空白

    ```Python
    file_path = "FileOP/pi_digits.txt"
    with open(file_path) as file_object:
        for line in file_object:
            print("- " + line.rstrip())
    ```

- 创建一个包含文件多行的列表

    ```Python
    file_path = "FileOP/pi_digits.txt"
    with open(file_path) as file_object:
        lines = file_object.readlines()
        
    print(lines)  #  ['3.1415926535\n', '  8979323846\n', '  2643383279\n']
    ```

    readlines()方法从文件中读取每一行以列表的形式存储到lines中

- Python读取我呢本文件时，对于所有的文本都解读为字符串，可以使用 int() 或 float() 函数转化成数字

### 写入文件

- 写入空文件，调用 open() 时，多提供一个参数 ‘w’ ，这个参数称为模式参数，告诉Python要写入文件

    ```Python
    file_path = 'FileOP/programming.txt'
    
    with open(file_path, 'w') as file_obj:  # 如果目标文件不存在，函数 open() 就新建一个文件
        file_obj.write('I love programming.')
    ```

- 打开文件时，可以指定写入模式：`读取模式（’r’）`、`写入模式（‘w’）`、`附加模式（‘a’）`、`读取和写入模式（‘r+’）`

- 以`写入模式（‘w’）`打开文件时，如果目标文件中存在内容，Python在返回该文件对象时会清空该文件里的内容

- python只能将字符串写入到文本文件，如果是数值型数据，必须要用 str() 转换成字符串格式

- 写入多行，write函数不会自动添加换行符，需要自己手动加上

    ```Python
    file_path = 'FileOP/programming.txt'
    
    with open(file_path, 'w') as file_obj:
        file_obj.write('I love programming.\n')
        file_obj.write('I love creating new games.\n')
    ```

- 附加到文件，使用 **附加模式**

    ```Python
    file_path = 'FileOP/programming.txt'
    
    with open(file_path, 'a') as file_obj:
        file_obj.write('I also love finding meaning in large datasets.\n')
        file_obj.write('I love creating apps that can run in a browser.\n')
    ```


# 异常

- Python使用被称为**异常**的特殊**对象**来管理程序执行期间发生的错误

- 如果代码中没有处理异常的代码块，程序会显示一个traceback

- 异常是使用`try-except`代码块处理的

    ```Python
    # 处理 ZeroDivisionError:
    try:
        print(5/0)
    except ZeroDivisionError:
        print("You can't divide by zero.")
    ```

    这样就可以处理特定的异常，在上面代码中，可以处理`ZeroDivisionError`异常

    如果 try 代码块中的代码没有问题，Python将跳过except代码块，否则，将查找这样的except代码块：except 指定的错误与引发的错误相同，并运行其中的代码

- else 代码块：

    ```Python
    print("Give me two numbers, and I'll diveide them.")
    print("Enter 'q' to quit.")
    
    while True:
        first_num = input('first_num: ')
        if first_num == 'q':
            break
        second_num = input('second_num: ')
        if second_num == 'q':
            break
        try:
            answer = int(first_num) / int(second_num)
        except ZeroDivisionError:
        	print("You can't divide by zero.")
        else:
            print("Answer: ", answer)
    ```

    在上述代码中，`try` 代码块中只包含可能导致错误的代码，如果发生错误将试图和`except`代码块中的错误匹配，如果没有错误就执行`else`代码块中的内容

    excpet代码块的作用是告诉Python，在遇到了指定的异常应该怎么办

- 处理 `FileNotFoundError` 异常

    ```Python
    file_name = 'alice.txt'
    
    with open(file_name) as f_obj:
        contents = f_obj.read()   # FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
    ```

    这个异常是 `open` 函数导致的，可以把 `open` 函数包含在 `try` 代码块中：

    ```Python
    file_name = 'alice.txt'
    
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()   
    except:
        msg = "Sorry, the file '" + file_name + "' does not exist."
        print(msg)
    ```

- 分析文本

    ```Python
    title = 'Alice in Wonderland.'
    
    title.split()   # ['Alice', 'in', 'Wonderland.']
    ```

    `split()` 方法以空格为分隔符将字符串分拆成多个部份，并将这些部份都存储到一个列表中

    ```Python
    file_name = 'Alice in Wonderland.txt'
    
    try:
        with open(file_name) as f_obj:
            contents = f_obj.read()   
    except:
        msg = "Sorry, the file '" + file_name + "' does not exist."
        print(msg)
    else:
        words = contents.split()
        num_words = len(words)
        print("Total words nums: " + str(num_words))
    ```

- 使用多个文件（包装成一个函数）

    ```Python
    def count_words(file_path):
        """计算一个文件大致包含多少个单词"""
        try:
            with open(file_path) as f_obj:
                contents = f_obj.read()   
        except:
            msg = "Sorry, the file '" + file_name + "' does not exist."
            print(msg)
        else:
            words = contents.split()
            num_words = len(words)
            print("Total words nums: " + str(num_words))
            
    file_path = "./FileOP/alice.txt"
    count_words(file_path)
    ```

- 使用 `pass`语句跳过对捕捉异常的处理部份

    ```Python
    def count_words(file_path):
        try:
            with open(file_path) as f_obj:
                contents = f_obj.read() 
        except FileNotFoundError:
            pass
        else:
            words = contents.split()
            num_words = len(words)
            print("Total words nums: " + str(num_words))
            
            
    file_path = "./FileOP/alice.txt"
    count_words(file_path)        
    ```

    `pass` 语句充当了占位符，提醒自己在某个地方什么都没做

# 存储数据

- 使用 `json` 格式存储数据

- 使用 `json.jump()` 存储数据

    ```Python
    import json
    
    numbers = [1, 2, 3, 4, 5]
    file_path = "./FileOP/numbers.json"
    with open(file_path, 'w') as file_obj:
        json.dump(numbers, file_obj)
    ```

- 使用 `json.load()` 读取数据

    ```Python
    import json 
    
    file_path = "./FileOP/numbers.json"
    with open(file_path) as file_obj:
        numbers = json.load(file_obj)
    
    print(numbers)
    ```

- 一次实例：

    ```Python
    # rember_me.py
    import json
    file_path = "./FileOP/username.json"
    try:
        with open(file_path) as f_obj:
            user_name = json.load(f_obj)
    except FileNotFoundError:
        username = input("Tell me your name: ")
        with open(file_path, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We will rember you, Dear  " + username)
    else:
        print("Welcome back, " + username)
    ```


# 测试

- Python标准库中的模块`unittest`提供了代码测试工具
- **单元测试**用于核实函数的某个方面没有问题
- **测试用例**是一组单元测试，这些单元测试一起核实函数在各种情况下都符合要求
- **全覆盖式测试**用例包含一整套单元测试，涵盖了各种可能的函数使用方式

### 测试函数

- 要为函数编写测试用例，需要先导入模块`unittest`以及要测试的函数，在创建一个继承`unitest.TestCase`的类

    ```Python
    # name_function.py
    
    def get_fullname(first,last):
        fullname = first + " " + last
        return fullname.title()
    ```

    ```Python
    # test_name_function.py
    import unittest
    from name_function import get_fullname
    
    class NamesTestCase(unittest.TestCase):  # 类名可以自定义，但是应尽量包含Test，而且必须继承 unittest.TestCase 类
        """ 测试name_function.py """
        def test_first_last_name(self):
            fullname = get_fullname('jains', 'joplin')
            self.assertEqual(fullname, 'Jains Joplin')
    
    unittest.main()
    ```

- 一个新的案例：

    ```Python
    # name_function.py
    
    def get_fullname(first, last, middle=''):
        if middle:
            fullname = first + " " + middle + " " + last
        else:
            fullname = first + " " + last
        return fullname.title()
    ```

    ```Python
    # test_name_function.py
    import unittest
    from name_function import get_fullname
    
    
    class NamesTestCase(unittest.TestCase):
        """ 测试name_function.py """
    
        def test_first_last_name(self):
            fullname = get_fullname('jan', 'joplin')
            self.assertEqual(fullname, 'Jan Joplin')
    
        def test_first_last_middle_name(self):
            fullname = get_fullname('wolf', 'dog', 'amazes')
            self.assertEqual(fullname, 'Wolf Dog Amazes')
    
    unittest.main()
    ```

- 一个新的案例

    ```Python
    # city_functions.py
    
    def get_formatted_city(city, country, population=''):
        if population:
            res = city + ', ' + country + '-' + str(population)
        else:
            res = city + ', ' + country
        return res.title()
    
    ```

    ```Python
    # test_cities.py
    
    import unittest
    from city_functions import get_formatted_city as gfc
    
    
    class CitiesTestCase(unittest.TestCase):
        """ 测试city_functions.py """
    
        def test_city_country(self):
            res = gfc('xian', 'china')
            self.assertEqual(res, 'Xian, China')
    
        def test_city_country_population(self):
            res = gfc('santiago', 'chile', 25000)
            self.assertEqual(res, 'Santiago, Chile-25000')
    
    # unittest.main()
    ```

### 测试类

- `unittest.TestCase`中常用的断言方法

    | 方法                                   | 用途                                                         |
    | -------------------------------------- | ------------------------------------------------------------ |
    | `assertEqual(a, b)`                    | 验证 `a == b`                                                |
    | `assertNotEqual(a, b)`                 | 验证 `a != b`                                                |
    | `assertTrue(x)`                        | 验证 `x` 为 `True`                                           |
    | `assertFalse(x)`                       | 验证 `x` 为 `False`                                          |
    | `assertIs(a, b)`                       | 验证 `a is b`（对象身份相同）                                |
    | `assertIn(item,list)`                  | 验证 `item` 在 `list` 中                                     |
    | `assertNotIn(item,list)`               | 验证 `item` 不在 `list` 中                                   |
    | `assertIsNot(a, b)`                    | 验证 `a is not b`                                            |
    | `assertIsNone(x)`                      | 验证 `x` 是 `None`                                           |
    | `assertIsNotNone(x)`                   | 验证 `x` 不是 `None`                                         |
    | `assertIn(a, b)`                       | 验证 `a` 包含在 `b` 中（`a in b`）                           |
    | `assertNotIn(a, b)`                    | 验证 `a` 不包含在 `b` 中（`a not in b`）                     |
    | `assertIsInstance(obj, cls)`           | 验证 `obj` 是 `cls` 的实例                                   |
    | `assertNotIsInstance(obj, cls)`        | 验证 `obj` 不是 `cls` 的实例                                 |
    | `assertAlmostEqual(a, b, places=7)`    | 验证浮点数 `a` 和 `b` 近似相等（精度为小数点后 `places` 位） |
    | `assertNotAlmostEqual(a, b, places=7)` | 验证浮点数 `a` 和 `b` 不近似相等                             |
    | `assertGreater(a, b)`                  | 验证 `a > b`                                                 |
    | `assertGreaterEqual(a, b)`             | 验证 `a >= b`                                                |
    | `assertLess(a, b)`                     | 验证 `a < b`                                                 |
    | `assertLessEqual(a, b)`                | 验证 `a <= b`                                                |
    | `assertListEqual(a, b)`                | 验证列表 `a` 和 `b` 内容及顺序一致                           |
    | `assertDictEqual(a, b)`                | 验证字典 `a` 和 `b` 键值对完全一致                           |
    | `assertTupleEqual(a, b)`               | 验证元组 `a` 和 `b` 内容及顺序一致                           |
    | `assertSetEqual(a, b)`                 | 验证集合 `a` 和 `b` 内容相同（忽略顺序）                     |
    | `assertMultiLineEqual(a, b)`           | 验证多行字符串 `a` 和 `b` 完全一致                           |

- 类的测试大部分工作是测试类中方法的行为：

    ```Python
    # suvery.py
    class AnonymousSurvey():
        """ 收集匿名调查问卷的答案 """
    
        def __init__(self, question):
            """存储一个问题，并为存储答案做准备"""
            self.question = question
            self.responses = []
    
        def show_question(self):
            """显示调查问卷"""
            print(self.question)
    
        def store_responses(self, new_response):
            """存储单份调查问卷"""
            self.responses.append(new_response)
    
        def show_results(self):
            """显示收集到的所有答案"""
            print("Survey results: ")
            for res in self.responses:
                print('-' + res)
    ```

    ```Python
    # language_survey.py
    from survey import AnonymousSurvey as AS
    
    # 定义一个问题，并创建一个表示调查的AnonymousSurvey对象
    question = "What's your favorite language?"
    my_survey = AS(question)
    
    # 显示问题并存储答案
    my_survey.show_question()
    print("Enter 'q' to quit. ")
    while True:
        response = input("Please tell me your answer: ")
        if response == 'q':
            break
        else:
            my_survey.store_responses(response)
    
    # 显示调查结果
    print("\n Thank you: ")
    my_survey.show_results()
    ```

- 开始测试`AnonymousSurvey`类

    - 验证：如果用户面对调查问题时，只提供了一个答案，是否能够准确地存储

        ```Python
        # test_survey.py
        import unittest
        from survey import AnonymousSurvey
        
        
        class TestAnonymousSurvey(unittest.TestCase):
            """测试AnonymousSurvey类"""
            def test_store_single_response(self):
                question = "What your favorite language?"
                my_survey = AnonymousSurvey(question)
                my_survey.store_responses('English')
        
                self.assertIn('English', my_survey.responses)
        ```

    - 验证：如果用户提供了多个答案时，是否能够准确的存储：

        ```Python
        # test_survey.py
        import unittest
        from survey import AnonymousSurvey
        
        
        class TestAnonymousSurvey(unittest.TestCase):
            """测试AnonymousSurvey类"""
            def test_store_single_response(self):
                question = "What your favorite language?"
                my_survey = AnonymousSurvey(question)
                my_survey.store_responses('English')
                self.assertIn('English', my_survey.responses)
        
            def test_store_three_responses(self):
                question = "What your favorite language?"
                my_survey = AnonymousSurvey(question)
                responses = ['C++', 'C', 'Java']
                for res in responses:
                    my_survey.store_responses(res)
        
                for res in responses:
                    self.assertIn(res, my_survey.responses)
        ```

- 使用方法 `setUp()`，在上边的`TestAnonymousSurvey`类中，每个测试方法都创建了一次`AnonymousSurvey`的实例，使用`setUp()`方法可以让我们只需创建一次实例对象，然后在每个测试方法中使用它：

    ```Python
    import unittest
    from survey import AnonymousSurvey
    
    
    class TestAnonymousSurvey(unittest.TestCase):
        """测试AnonymousSurvey类"""
    
        def setUp(self) -> None:
            """创建一个调查对象和一组答案，供使用的测试方法使用"""
            question = "What your favorite language?"
            self.my_survey = AnonymousSurvey(question)  
            self.responses = ['C++', 'C', 'Java']
    
        def test_store_single_response(self):
            """测试单个答案会被妥善的存储"""
            self.my_survey.store_responses(self.responses[0])
            self.assertIn(self.responses[0], self.my_survey.responses)
    
        def test_store_three_responses(self):
            """测试多个答案会被妥善的存储"""
            for res in self.responses:
                self.my_survey.store_responses(res)
    
            for res in self.responses:
                self.assertIn(res, self.my_survey.responses)
    ```

    在方法`setUp`中创建了一个调查对象 `my_survey` 和一个答案列表 `responses` , 并且都添加了前缀`self`(即存储在属性中)，因此可在这个类的任何地方使用

    

    

    

    

