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
  class Animal:
      def speak(self):
         print("Animal makes a sound")

##### Child Class (inherits from Animal)
  class Dog(Animal):
      def speak(self):  # Overriding the parent class method
          print("Dog barks")

##### Creating objects
 a = Animal()
 d = Dog()

 a.speak()  
 d.speak()  
 
 - What is the difference between `@staticmethod`, `@classmethod`, and instance methods? 

3. Data Structures & Algorithms 
 - How would you implement a stack and a queue in Python? 
 - What is the time complexity of dictionary operations? 
 - Explain sorting algorithms like QuickSort and MergeSort. 

4. Python Libraries & Modules 
 - What are NumPy and Pandas used for? 
 - How do you handle missing values in Pandas? 
 - How does Python handle file I/O operations? 

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

9. Data Science & Machine Learning (if applicable) 
 - What are the key differences between supervised and unsupervised learning? 
 - How do you handle imbalanced datasets? 
 - Explain feature selection and feature engineering. 

10. Git & Version Control 
 - What is the difference between `git pull` and `git fetch`? 
 - How do you resolve a merge conflict in Git? 


