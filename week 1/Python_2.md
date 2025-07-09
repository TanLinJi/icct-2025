> 接续 Python.md 文件的第二部分

# 字典

### 字典的基本操作

- 字典是一系列 键—值 对，每一个键都与一个值关联，值可以是数字，字符串，甚至是列表或字典，可以把任何python对象都作为字典中的值

    ```Python
    alien = {'color':'green','points':5}
    ```

    键和值之间用 ：分隔，而不同的键值对之间用 ，分隔 ，字典中可以包含任意数量的键值对

- 访问字典中的值

    ```Python
    alien = {'color':'green'}
    print(alien['color'])   #  green
    ```

    ```Python
    alien = {'color':'green','points':5}
    
    new_points = alien['points']
    print("You just earned " + str(new_points) + "points!")
    ```

- 添加 键—值 对

    ```Python
    alien = {'color':'green','points':5}
    
    alien['x_position'] = 0  # 添加新的键值对  x_position:0
    alien['y_position'] = 25 # 添加新的键值对  y_position:25
    print(alien)  # {'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
    ```

- python 不关心键值对的添加顺序，只关心键和值之间的练习，因此同一个字典中的键值对之间不存在先后顺序之说

- 创建一个空字典，并添加键值对

    ```Python
    alien = {}
    alien['color'] = 'green'
    alien['points'] = 5
    ```

- 修改字典中的值

    ```Python
    alien = {'color':'green','points':5}
    alien['color'] = 'blue'
    print(alien['color'])
    
    alien = {'x_position':0, 'y_position':25, 'speed':'medium'}
    if alien['speed'] == 'slow':
        x_increment = 1
    elif alien['speed'] == 'medium':
        x_increment = 2
    else:
        x_increment = 3
    alien['x_position'] = alien['x_position'] + x_increment
    print("New x_position: " + str(alien['x_position']))  # New x_position: 2
    ```

- 使用 del 语句删除键值对

    ```Python
    alien = {'color':'green','points':5}
    del alien['points']
    print(alien) # {'color': 'green'}
    ```

- 由类似对象组成的字典

    ```Python
    favorite_languages = {
    	'jen':'python',
        'sara':'C',
        'wdwa':'java',
        'alice':'python',  # 最后一个键值对后边的逗号可以有也可以没有
    }
    ```


### 字典的遍历

- 遍历字典的键和值

    ```Python
    favorite_nums = {
        'Bob': 5,
        'Alan':32,
        'kasy':56,
    }
    
    for name,num in favorite_nums.items():
        print(name + "'s favorite num is " + str(num))
        
    Bob's favorite num is 5
    Alan's favorite num is 32
    kasy's favorite num is 56
    ```

- 遍历字典的所有键

    ```Python
    favorite_languages = {
    	'jen':'python',
        'sara':'C',
        'wdwa':'java',
        'alice':'python',  
    }
    
    for name in favorite_languages.keys():   #  因为遍历字典会默认比哪里其所有的键，因此，使用for name in favorite_languages: 也可以
        print(name.title())
    ```

- 按顺序遍历字典中的所有键(对键进行排序)

    ```Python
    favorite_languages = {
        'jen': 'python',
        'bon': 'C',
        'kasy': 'pyhton',
        'sda': 'C++',
    }
    
    for name in sorted(favorite_languages.keys()):
        print(name.title() + ", thank you for taking the poll.")
    ```

- 遍历字典的所有值

    ```Python
    favorite_languages = {
        'jen': 'python',
        'bon': 'C',
        'kasy': 'java',
        'sda': 'C++',
    }
    
    for language in favorite_languages.values():
        print(language.title())
    ```

- 为了避免出现重复的值，可以用 集合，集合中的每个元素都是独一无二的

    ```Python
    favorite_languages = {
        'jen': 'Python',
        'bon': 'C',
        'kasy': 'Python',
        'sda': 'C++',
    }
    
    for language in set(favorite_languages.values()):  # 通过对包含重复元素的列表带调用set(),可以让python找出其中独一无二的元素
        print(language.title())
    ```

    



# 嵌套

###  字典列表

- 创建一个所有元素均为字典的列表

    ```Python
    alien_0 = {'color': 'green', 'points': 5}
    alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
    
    aliens = [alien_0, alien_1, alien_2]
    for alien in aliens:
        print(alien)
    ```
    
    ```Python
    # 创建一个用于存储外星人的空列表
    aliens = []
    
    # 创建30个绿色的外星人
    for alien_number in range(30):
        new_alien = {'color': 'green','points':5, 'speed':'slow'}
        aliens.append(new_alien)
        
    # 显示前五个外星人
    for alien in aliens[:5]:
        print(alien)
    
    # 显示创建了多少个外星人
    print("Total number: " + str(len(aliens)))
    ```
    
    ```Python
    # 创建一个用于存储外星人的空列表
    aliens = []
    
    # 创建30个绿色的外星人
    for alien_number in range(30):
        new_alien = {'color': 'green','points':5, 'speed':'slow'}
        aliens.append(new_alien)
    
    for alien in aliens[:3]:
        if alien['color'] == 'green':
            alien['color'] = 'red'
            alien['points'] = 10
            alien['speed'] = 'medium'
        
    # 显示前五个外星人
    for alien in aliens[:5]:
        print(alien)
    ```

### 列表字典

- 包含列表元素的字典

    ```Python
    # 存储点的pizza的信息
    pizza = {
        'crust':'thick',
        'toppings':['mushrooms','extra cheese'],
    }
    
    #  概述信息
    print("You ordeered  a" + pizza['crust'] + "-crust pizza"+
         " with the following topppings: ")
    for topping in pizza['toppings']:
        print('\t ' + topping)
    ```

    每当需要在字典中将一个键关联到多个值时，就可以在字典中嵌入一个列表

    ```Python
    favorite_languages = {
        'jen': ['python','ruby'],
        'sarah':['c'],
        'edward':['ruby','go'],
        'phil':['pyhotn','hashkell'],
    }
    
    for name,languages in favorite_languages.items():
        print("\n" + name.title() + "'s favorite languages are:")
        for language in languages:
            print("\t" + language.title())
    ```

### 存储字典的字典

- 在字典中存储字典，可以存储更复杂的信息

    ```Python
    users = {
        'endis': {
            'first': 'albert',
            'last': 'ensid',
            'location':'princeton'
        },
        'John':{
            'first':'marie',
            'last':'curie',
            'location':'Beijing'
        }
    }
    
    for username , user_info in users.items():
        print("UserName: " + username)
        fullName = user_info['first'] + " " + user_info['last']
        location = user_info['location']
        print('\t FullName: ' + fullName)
        print("\tLocation: " + location)
    ```

    尽量保证字典内每个字典的结构都相同，这样循环遍历起来更容易

# 输入

- input的工作原理：

    ```Python
    name = input("please input your name:")   # input里的参数是提示输入的内容
    print("Hello, " + name + "!")
    ```

- 如果提示内容太长，可以存在一个变量里：

    ```Python
    prompt = "If you tell us who you are, \  
    	\n I will tell you how to do!"
    name = input(prompt)
    print("Hello, " + name + "!")
    ```

    ```Python
    prompt = "If you tell us who you are"
    prompt += "\nTell me your name: "
    name = input(prompt)
    print("Hello, " + name + "!")
    ```

- 使用 int() 来获取数值型输入

    ```Python
    age = int(input("Please tell me your age: "))
    print(age >= 18)
    ```

# 输出

## 

```python
print(a + b, a, b)
print(chr(65), chr(97)) # 使用 chr 函数可以得到 对应的ASCII字符
print(ord('北'))  # 使用 ord 函数可以得到字符对应的ASCII值
print(ord('京'))
```

#### 完整格式

```python
print(*objects, sep=' ', end='\n', file=sys.stdout)
```

参数的具体含义如下：

objects --表示输出的对象。输出多个对象时，需要用 , （逗号）分隔。

sep -- 用来间隔多个对象，以sep指定的内容作为分隔符

end -- 用来设定以什么结尾。默认值是换行符 \n，我们可以换成其他字符。

file -- 要写入的文件对象。

#### 其他用法

- 使用连接符连接两个字符串(只能是字符串和字符串之间连接，整数和字符串不能做连接)

    ```python
    print('a'+'b')
    ```

- 如果想要同时输出字符串和整数，用逗号分隔即可

    ```python
    print('a',2)
    ```



# While循环

- 让用户选择何时退出

    ```Python
    prompt = "Tel me something, and I will repeat it back to you \n"
    prompt += "(Enter 'quit' to end the program.) : "
    message = ""
    while message != 'quit':
        message = input(prompt)
        if message != 'quit':
        	print(message)
    ```

- 使用标志：定义一个变量，判断整个程序是否处于活动状态，这个变量称为标志

    ```Python
    prompt = "Tel me something, and I will repeat it back to you \n"
    prompt += "(Enter 'quit' to end the program.) : "
    active = True  # active 就是程序状态的标志
    while active:
        message = input(prompt)
        if message == 'quit':
            active = False
        else:
            print(message)
    ```

- 使用break退出循环

    ```Python
    prompt = "Tel me something, and I will repeat it back to you \n"
    prompt += "(Enter 'quit' to end the program.) : "
    
    while True:
        message = input(prompt)
        if message == 'quit':
            break
        else:
            print(message)
    ```

    任何python的循环都可以使用break语句跳出循环。如：可以使用break语句跳出遍历列表或字典的for循环

- 在循环中使用continue

    ```Python
    # 实现打印 1-10内的奇数
    
    current_num = 0
    while current_num < 10:
        current_num += 1
        if current_num % 2 == 0:
            continue
        else:
            print(current_num)
    ```

- 使用 while 循环来处理列表和字典

    ```Python
    # 在列表之间移动元素
    unconfirmed_users = ['alice', 'brain', 'wow']
    confirmed_users = []
    
    while unconfirmed_users:
    	current_user = unconfirmed_users.pop()
        print("Verifying user: " + current_user.title())
        confirmed_users.append(current_user)
    print("\nThe following users are confirmed: ")
    for user in confirmed_users:
        print(user.title())
    ```

- 删除包含特定值的所有列表元素

    ```Python
    pets = ['cat','dog','goldfish','cat','dog','rabbit','cat']
    print(pets)
    
    while 'cat' in pets:
    	pets.remove('cat')
    
    print(pets)
    ```

- 使用用户输入来填充字典

    ```Python
    responses = {}
    
    active = True
    while active:
        name = input("please input your name: ")
        response = input("Please input your advice: ")
        responses[name] = response
        repeat = input("Would you like to let another person respond?(yes/no): ")
        if repeat == 'NO' or repeat == "no" or repeat == 'No':
            active = False

    print("Polling results: ")
    for name, response in responses.items():
        print(name + ": " + response + "\n")
    ```
    
    

# 函数

- 定义函数--> 原则：每个函数都应只负责一项具体的工作

    ```Python
    def greet_user(username):
        print("Hello, " + str(username).title())
    greet_user("John")
    ```

- 函数应该包含注释，其注释应该紧跟在函数定义后边，并使用文档字符串的形式注释

- 多个函数之间用两个空行分开

- 实参--位置实参（实参的顺序必须和形参的顺序完全相同）

    ```Python
    def describe_pet(animal_type, pet_name):
        print("I have a " + animal_type + ".")
        print("My " + animal_type + "'s name is " + pet_name.title() + '.' )
    
    describe_pet('dog', 'John')
    ```

- 实参--关键字实参(传递给函数的名称-值对)

    ```Python
    def describe_pet(animal_type, pet_name):
        print("I have a " + animal_type + ".")
        print("My " + animal_type + "'s name is " + pet_name.title() + '.' )
    
    describe_pet(animal_type = 'dog', pet_name =  'John')
    describe_pet(pet_name =  'John', animal_type = 'dog')   # 两种方式输出一样
    ```

    此时不用考虑参数的顺序，但是必须准确的指定函数定义中形参的名字

- 默认值（可以在编写函数时，给每个参数一个默认值，）

    ```Python
    def describe_pet(pet_name, animal_type='dog'):  # 注意参数的顺序发生了改变，pet_name位置处传入的参数时位置参数
        print("I have a " + animal_type + ".")
        print("My " + animal_type + "'s name is " + pet_name.title() + '.' )
    describe_pet("john")
    ```

    使用默认值时，把给定了默认值的参数放在后边，把那些没有给默认值的形参放在前边：

    ```Python
    def describe_pet(animal_type='dog',pet_name):   # 会报错 SyntaxError: non-default argument follows default argument
        print("I have a " + animal_type + ".")
        print("My " + animal_type + "'s name is " + pet_name.title() + '.' )
    describe_pet("john")
    ```

- 等效的函数调用

    ```Python
    def describe_pet(pet_name, animal_type='dog'):
        print("I have a " + animal_type + ".")
        print("My " + animal_type + "'s name is " + pet_name.title() + '.' )
    
    # 一只名为wille的小狗
    describe_pet('wille')
    describe_pet(pet_name = 'wille')
    
    # 一只名为harry的仓鼠
    describe_pet('harry','hamster')
    describe_pet(pet_name = 'harry', animal_type = 'hamster')
    describe_pet(animal_type = 'hamster', pet_name = 'harry')
    describe_pet(pet_name = 'harry', 'hamster') # 不能这样写，要么全部写成位置参数，要么全部写成关键词参数
    ```

- 返回值（使用return语句）

    ```Python
    def get_fullname(first_name, last_name):
        fullname = first_name.title() + " " + last_name.title()
        return fullname
    musician = get_fullname("john",'Alan')
    print(musician)
    ```

- 让实参变成可选的

    ```Python
    def get_fullname(first_name, last_name, middle_name=''):  # 中间名是可选的，应该在最后列出该形参，并将其值设置为空字符串
        if middle_name:   
            fullname = first_name + ' ' + middle_name + ' ' + last_name  # 这样没有中间名字时，也能合理的显示
        else:
            fullname = first_name + ' '  + last_name
        return fullname.title()
    
    musician = get_fullname('jimi','hendrix')
    print(musician)
    musician = get_fullname('jimi','hendrix','Lee')
    print(musician)
    ```

- 返回字典

    ```Python
    def build_person(first_name,last_name,age=''):
        person = {'first_name':first_name, 'last_name':last_name}
        if age:
            person['age'] = age
        return person
    
    musician = build_person('jimi', 'hendrix',age=27)
    print(musician)
    ```

- 综合训练

    ```Python
    def get_fullname(first_name, last_name):
        fullname = first_name + " " + last_name
        return fullname.title()
    
    while True:
        print("\nTell me your name（input 'q' to edn program.）: ")
        f_name = input("\tfirst name:")
        if f_name == 'q' or f_name == 'Q':
            break
        l_name = input("\tlast name: ")
        if l_name == 'q' or l_name == 'Q':
            break
        full_name = get_fullname(f_name,l_name)
        print("Hello, " + full_name)
    ```

- 传递列表

    ```Python
    def greet_users(names):
        for name in names:
            print("hello, " + name.title() + '.')
    usernames = ['John','ALan','Alice']
    greet_users(usernames)
    ```

- 在函数中修改传递的列表

    ```Python
    def print_models(unprinted_designs, completed_designs):
        while unprinted_designs:
            current_design = unprinted_designs.pop()
            print("Printing model: " + current_design + " ...")
            completed_designs.append(current_design)
    
    def show_completed_models(completed_designs):
        print("\nThe following modesl have benn printed:")
        for design in completed_designs:
            print(design)
            
    unprint_designs = ['iphone case', 'robot pendant', 'dodecahdrom']
    completed_models = []
    print_models(unprint_designs,completed_models)
    show_completed_models(completed_models)
    ```

- 静止函数修改列表-->向函数传递列表的副本而不是原件

    ```Python
    function_name(list_name[:]) # 使用切片表示法[:]创建列表的副本
    ```

    ```Python
    def print_models(unprinted_designs, completed_designs):
        while unprinted_designs:
            current_design = unprinted_designs.pop()
            print("Printing model: " + current_design + " ...")
            completed_designs.append(current_design)
    
    def show_completed_models(completed_designs):
        print("\nThe following modesl have benn printed:")
        for design in completed_designs:
            print(design)
            
    unprint_designs = ['iphone case', 'robot pendant', 'dodecahdrom']
    completed_models = []
    print_models(unprint_designs[:],completed_models)  # 使用切片表示法创建副本，原来的列表能够继续存在
    show_completed_models(completed_models)
    print("======")
    show_completed_models(unprint_designs)
    ```

- 传递任意数量的实参（使用 * 创建空元组）

    ```Python
    def make_pizza(*toppings):  # 创建了一个名为toppings的空元组
        print(toppings)
make_pizza('pepper')   # ('pepper',)
    make_pizza('pepper','green pepp','dogds')  # ('pepper', 'green pepp', 'dogds')   
    ```
    
    使用这种方法，无论传入多少个实参，都是按照元组对待，可以使用遍历的方法：
    
    ```Python
    def make_pizza(*toppings):  # 创建了一个名为toppings的空元组
        print("The toppings are following: ")
        for topping in toppings:
            print(topping)
    make_pizza('pepper','green pepp','dogds')
    ```
    
- 结合使用位置实参和任意数量实参

    如果同时有位置实参和任意数量参数，必须把任意数量实参的形参放在最后，Python会先匹配位置实参和关键字实参，再将剩下的实参都放在最后一个形参中

    ```Python
    def make_pizza(size,*toppings):
        print("Making a "+ str(size) + "-size pizza.")
        print("The toppings are following: ")
        for topping in toppings:
            print("\t-"+ topping)
    make_pizza(12,'pieer')
    make_pizza(16,'asds','sada','pospdo')
    ```

- 使用任意数量的关键字实参（使用 ** 创建空字典）

    ```Python
    def build_person(first,last, **user_info):  # 告诉Python创建一个名为  user_info的空字典
        person = {}
        person['first_name']= first
        person['last_name'] = last
        for key,value in user_info.items():
            person[key] = value
        return person
    
    user_profile = build_person('alberit','ensten',
                               location='princeton',   # 注意写法，这里的 键 不用加引号
                               field='Computer Science')
    print(user_profile) # {'first_name': 'alberit', 'last_name': 'ensten', 'location': 'princeton', 'field': 'Computer Science'}
    ```

- 将函数存储在模块中

    模块是一个单独存放函数的文件，可以隐藏程序代码的细节，模块的扩展名为.py。使用import语句将模块导入主程序中

    ```Python
    # pizza.py
    def make_pizza(size,*toppings):
        print("Making a "+ str(size) + "-size pizza.")
        print("The toppings are following: ")
        for topping in toppings:
            print("\t-"+ topping)
    ```

    ```Python
    import pizza   # 导入后，可以使用pizza.py中的所有函数
    
    pizza.make_pizza(12,'pieer')  # 使用 模块名.函数名()的方法调用模块中的任意一个函数
    pizza.make_pizza(16,'asds','sada','pospdo')
    ```

    python导入模块时，是将模块中的代码整个的复制到当前的程序中

- 导入特定的函数，使用逗号分隔函数名

    ```Python
    from moudle_name import function_name
    from moudle_name import function1_name,function2_name,function3_name
    ```

    ```Python
    from pizza import make_pizza
    make_pizza(12,'pieer')  # 使用导入特定函数的方法，就不用再使用句点的方式，因为显示的导入了make_pizza函数，所以可以直接使用其名称
    make_pizza(16,'asds','sada','pospdo')
    ```

- 使用 as 给函数起别名

    ```Python
    from pizza import make_pizza as mp
    
    mp(12,'pieer')
    mp(16,'asds','sada','pospdo')
    ```

- 使用 as 给模块起别名

    ```Python
    import pizza as p
    
    p.make_pizza(12,'pieer')  
    p.make_pizza(16,'asds','sada','pospdo')
    ```

- 使用 * 导入模块中的所有函数（尽量少用，因为可能不同的模块中有名字相同的函数）

    ```Python
    from pizza import *
    make_pizza(12,'pieer')  # 由于导入了所有函数，也不用再使用句点的方式，可以直接使用其名称
    make_pizza(16,'asds','sada','pospdo')
    ```

    python在遇到多个名字相同的变量或函数时，会覆盖，而不是分别导入不同的函数