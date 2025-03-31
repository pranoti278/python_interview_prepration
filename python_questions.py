All the best and do your best , you are strong ,confidant and will achive great offer soon .

### 1) Write a Python function to find all unique pairs of integers in a list that sum up to a given target value

Ans:
- def find_unique_pair(nums,target):
 - seen=set()
 - for i in range(len(nums)):
   - for j in range(i+1,len(nums)):
     - if nums[i]+nums[j] ==target:
       - seen.add((nums[i],nums[i]))
   - print(len(seen))
- nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
- target = 10
- find_unique_pair(print(nums,target))


️### 2) Given a string, write a function to check if it’s a palindrome, ignoring spaces, punctuation, and case sensitivity.
Ans: 
- import re
- s= "No lemon, no melon"
- cleaned_str= re.sub(r'[^a-zA-Z0-9]','',s).lower()
- res=cleaned_str[::-1]
- print(res==cleaned_str)

#### 2nd approch 
- s= "No lemon, no melon"
- l=[]
- for i in s:
    - if i.isalnum()==True:
        - l.append(i)
- clean_str="".join(l).lower()
- print(clean_str==clean_str[::-1])

### 3) Explain the difference between deep copy and shallow copy in Python. When would you use each?

- When to Use Each?
  When you need a new object, but modifying nested elements should reflect in both objects.	Shallow Copy (copy.copy())
  When you need a completely independent copy, especially if the object has nested lists/dictionaries.	Deep Copy (copy.deepcopy())

- Example 1
    - import copy
    - original = [[1, 2, 3], [4, 5, 6]]
    - shallow_copied = copy.copy(original)
    - shallow_copied[0][0] = 99  # Modifying a nested object
    - print(original)  # [[99, 2, 3], [4, 5, 6]]
    - print(shallow_copied)  # [[99, 2, 3], [4, 5, 6]]

- Example 2
  - deep_copied = copy.deepcopy(original)
  - deep_copied[0][0] = 42  # Modifying a nested object
  - print(original)  # [[99, 2, 3], [4, 5, 6]] (Remains unchanged)
  - print(deep_copied)  # [[42, 2, 3], [4, 5, 6]]
    
### 4) What are decorators in Python, and how do they work? Provide an example of a scenario where a decorator would be useful.

- A decorator in Python is a function that modifies the behavior of another function without changing its code. It allows for reusable and clean code.

#### 5) How Do Decorators Work?
- A decorator is applied using the @decorator_name syntax above a function.
- It wraps the original function, allowing additional functionality before and/or after calling it.

- Example: A Simple Decorator

  -def my_decorator(func):
     - def wrapper():
         - print("Before calling the function")
         - func()
         - print("After calling the function")
     - return wrapper
 - @my_decorator
 - def say_hello():
    - print("Hello!")
 - say_hello()

  
- 🔹 Output:
  - Before calling the function  
  - Hello!  
  - After calling the function  
  - ✅ Here, my_decorator adds extra behavior before and after say_hello(), without modifying say_hello() itself.

- Example: Logging Function Calls
    - Imagine you need to log when certain functions are called. Instead of adding logging manually to each function, use a decorator:
 

#### 6)Explain the difference between lists and tuples and set. 
- A list (list) is an ordered, mutable (changeable) collection that allows duplicate elements. Lists support various operations such as appending, modifying, and removing elements. Since they maintain the order of insertion, they are useful when you need a dynamic sequence of items that can be modified.
- A tuple (tuple) is an ordered, immutable (unchangeable) collection that also allows duplicate elements. Since tuples cannot be modified after creation, they are useful for storing fixed sets of values, such as coordinates or database records, where immutability ensures data integrity.
- A set (set) is an unordered, mutable collection that only contains unique elements. Unlike lists and tuples, sets do not support indexing or slicing since they are unordered. Sets are highly efficient for membership testing (O(1) average time complexity) and are used when storing distinct values is required, such as removing duplicates from a dataset.
  
#### 7)What are Python’s built-in data types? 
- Numeric Types
  - int (Integer) → Whole numbers, e.g., 10, -5, 1000
  - float (Floating-point) → Decimal numbers, e.g., 10.5, -3.14, 2.0
  - complex (Complex numbers) → Numbers with real and imaginary parts, e.g., 3 + 4j
- Sequence Types
  - list → Mutable (modifiable) ordered collection, e.g., [1, 2, 3]
  - tuple → Immutable (unchangeable) ordered collection, e.g., (4, 5, 6)
  - range → Sequence of numbers, e.g., range(1, 10)
 
- other
  - str
  - bool
  - set
  - frozenset
    
#### 8) How does memory management work in Python? 
- Python manages memory using reference counting, garbage collection, and memory pooling.
  - Reference Counting → Each object has a reference count; when it reaches zero, the memory is freed.
  - Garbage Collection (GC) → Handles circular references and unused objects automatically (can be triggered using gc.collect()).
  - Memory Pooling → Python optimizes memory allocation using techniques like pymalloc for small objects.
  - Stack vs Heap → Local variables are stored in the stack, while objects and data structures are stored in the heap.
  - del Statement → Removes object references but doesn’t immediately free memory.

#### 9) What is the difference between class and instance variables? 
- Class Variable :
   - Defined at the class level and shared by all instances.
   - Shared across all instances of the class.
   - Changing the value affects all instances (unless overridden).
   - Stored in the class’s namespace.
   - Used when a common value is needed for all instances.
- Instance Variable :
   - Defined inside methods using self and unique to each instance.
   - Specific to a particular instance (object).
   - Changing the value affects only that instance.
   - Stored in the object’s (instance’s) namespace.
   - Used for instance-specific data.
 

 #### 10) Explain inheritance and polymorphism with examples. 
 - Inheritance
   - Inheritance allows a child class to acquire the properties and methods of a parent class. This promotes code reusability and helps in 
    creating hierarchical relationships between classes.

 ##### Parent Class
  - class Animal:
      - def speak(self):
         - print("Animal makes a sound")

##### Child Class (inherits from Animal)
  - class Dog(Animal):
      - def speak(self):  # Overriding the parent class method
          - print("Dog barks")

##### Creating objects
 - a = Animal()
 - d = Dog()
 - a.speak()  
 - d.speak()  

### Polymorphism
- Polymorphism allows different classes to use the same method name but with different implementations. It enables method overriding and method overloading (though Python does not support true method overloading like Java).

- class Cat:
    - def speak(self):
        - print("Cat meows")

- class Dog:
    - def speak(self):
        - print("Dog barks")

##### Function demonstrating polymorphism
- def animal_sound(animal):
    - animal.speak()

##### Creating objects
- c = Cat()
- d = Dog()
- animal_sound(c)  # Output: Cat meows
- animal_sound(d)  # Output: Dog barks

  
#### 11) What is the difference between `@staticmethod`, `@classmethod`, and instance methods? 
- An instance method is the most common type of method and is defined without any decorator. It takes self as the first parameter, allowing it to access and modify instance attributes and other instance-specific behavior. Since it works with instance variables, it requires an instance of the class to be called.

- A class method, defined using the @classmethod decorator, takes cls as its first parameter instead of self. This means it operates on the class level rather than on individual instances. Class methods can modify class variables and are useful when the method logic is related to the class rather than any specific instance. They can be called using either an instance or the class itself.

- A static method, marked with the @staticmethod decorator, does not take self or cls as a parameter. It behaves just like a regular function but is defined inside a class for logical grouping. Static methods do not access instance or class variables and are typically used for utility functions that don’t need to modify instance or class attributes.

- class MyClass:
    - class_var = "Class Variable"

    - def __init__(self, value):
        - self.instance_var = value  # Instance variable

    - Instance Method
    - def instance_method(self):
        - return f"Instance Method: {self.instance_var}"

    - #Class Method
    - @classmethod
    - def class_method(cls):
        - return f"Class Method: {cls.class_var}"

    - #Static Method
    - @staticmethod
    - def static_method():
        - return "Static Method: No instance or class access"

-  Creating an instance
- obj = MyClass("Instance Variable")

- Calling methods
- print(obj.instance_method())  # ✅ Needs an instance
- print(MyClass.class_method())  # ✅ Can be called on class
- print(MyClass.static_method())  # ✅ Can be called on class

 
#### 12)How would you implement a stack and a queue in Python? 
-- Implementing a Stack (LIFO)
  - A stack allows elements to be added and removed from the same end (top). It supports two main operations:
  - Push → Add an element to the stack.
  - Pop → Remove the last added element.
  
  ###### Example :Implementation Using a List
- class Stack:
    - def __init__(self):
        - self.stack = []

    - def push(self, item):
        - self.stack.append(item)  # Add element

    - def pop(self):
        - if not self.is_empty():
            - return self.stack.pop()  # Remove last element
        - return "Stack is empty"

    - def peek(self):
        - return self.stack[-1] if self.stack else "Stack is empty"

    - def is_empty(self):
        - return len(self.stack) == 0

    - def size(self):
        - return len(self.stack)

- s = Stack()
- s.push(1)
- s.push(2)
- s.push(3)
- print(s.pop())  # Output: 3 (Last in, first out)


-- Implementing a Queue (FIFO)
- A queue allows elements to be added at one end (rear) and removed from the other end (front). It supports:
- Enqueue → Add an element to the queue.
- Dequeue → Remove the first added element.
---- Implementation Using collections.deque (Efficient)

- from collections import deque
- class Queue:
    - def __init__(self):
        - self.queue = deque()  # Double-ended queue for O(1) operations

    - def enqueue(self, item):
        - self.queue.append(item)  # Add element at rear

    - def dequeue(self):
        - if not self.is_empty():
            - return self.queue.popleft()  # Remove element from front
        - return "Queue is empty"

    - def peek(self):
        - return self.queue[0] if self.queue else "Queue is empty"

    - def is_empty(self):
        - return len(self.queue) == 0

    - def size(self):
        - return len(self.queue)
- q = Queue()
- q.enqueue(1)
- q.enqueue(2)
- q.enqueue(3)
 -print(q.dequeue())  # Output: 1 (First in, first out)
  
#### 13 What is the time complexity of dictionary operations? 
- The average time complexity is O(1) for lookup, insertion, and deletion because dictionaries use a hash table.
- In worst cases (due to hash collisions), these operations can degrade to O(n) when multiple keys map to the same hash bucket.

#### 14) Largest time complexity element ?
- O(1) (Constant Time) – Fastest, does not depend on n.
- O(logn) (Logarithmic Time) – Grows very slowly (e.g., binary search).
- O(nlogn) (Linearithmic Time) – Slightly worse than linear (e.g., Merge Sort).
- O(n2) (Quadratic Time) – Common in nested loops (e.g., Bubble Sort).
- O(n 3) (Cubic Time) – Even worse (e.g., some matrix operations).
- O(2 **n) (Exponential Time) – Very slow (e.g., recursive Fibonacci).


#### 15) What are NumPy and Pandas used for?
- NumPy (Numerical Python)
  - Purpose: Used for numerical computations, handling large multi-dimensional arrays, and performing mathematical operations efficiently.
- Key Features:
  - Supports N-dimensional arrays (ndarray).
  - Provides mathematical functions for linear algebra, Fourier transform, and random number generation.
  - Optimized for performance using C and Fortran under the hood.
  - Used in scientific computing, data analysis, and machine learning.
 
- Pandas
  - Purpose: Used for data manipulation and analysis, providing flexible and powerful data structures.
- Key Features:
  - Series (1D) and DataFrame (2D) structures for tabular data.
  - Supports data cleaning, transformation, and analysis.
  - Built on top of NumPy, allowing fast computations.
  - Used in data science, financial analysis, and real-world data processing.


#### 16 How do you handle missing values in Pandas? 
- To check for missing values in a DataFrame:
  - import pandas as pd
  - df = pd.DataFrame({
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4]
})

  - print(df.isnull())  # Returns True for missing values
  - print(df.isnull().sum())  # Count of missing values per column

-- Remove Missing Values
 a) Drop Rows with Missing Values
   -- df.dropna(inplace=True)  # Removes rows with NaN values
b) Drop Columns with Missing Values
-- df.dropna(axis=1, inplace=True)  # Removes columns with NaN values

-- Fill Missing Values
a) Fill with a Specific Value
df.fillna(0, inplace=True)  # Replaces NaN with 0
b) Fill with Column Mean/Median/Mode
df['A'].fillna(df['A'].mean(), inplace=True)  # Fill with mean
df['A'].fillna(df['A'].median(), inplace=True)  # Fill with median
df['A'].fillna(df['A'].mode()[0], inplace=True)  # Fill with mode
 

5. Database & SQL 
 - Write an SQL query to find the second highest salary from an employee table. 
 - Explain the difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL JOIN. 
 - What are indexes in SQL, and how do they improve performance? 

6. Error Handling & Debugging 
 - What is the difference between `try-except` and `try-finally` in Python? 
 - How do you debug a Python program? 

7. Multithreading & Concurrency 
 - What is the Global Interpreter Lock (GIL) in Python? 
 - How do you implement multithreading in Python? 

8. REST APIs & Web Development 
 - What is REST, and how does it differ from SOAP? 
 - How do you create a REST API using Flask or Django? 
 - Explain the role of middleware in Django. 


10. Git & Version Control 
 - What is the difference between `git pull` and `git fetch`? 
 - How do you resolve a merge conflict in Git? 


