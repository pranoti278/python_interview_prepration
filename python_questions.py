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


#### 16) How do you handle missing values in Pandas? 
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
 


#### 17 What is the difference between `try-except` and `try-finally` in Python? 
The try-except-finally block is used when:
- try → Contains code that may raise an exception.
- except → Handles specific exceptions.
- finally → Executes cleanup code, whether an exception occurs or not.
✅ Example 2: Handling Division by Zero
try:
    num = int(input("Enter a number: "))
    result = 100 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Invalid input! Please enter a number.")
finally:
    print("Execution completed.")
Output:
Enter a number: 0
Error: Cannot divide by zero!
Execution completed.

Custom Error--
In Python, you can create custom exceptions to handle specific error scenarios in a more meaningful way. 
This is done by defining a new exception class that inherits from Exception.

1️⃣ Why Use Custom Exceptions?
✅ Makes error messages more descriptive.
✅ Helps in debugging and logging specific issues.
✅ Can enforce custom validation rules in programs.
Use the raise keyword to trigger the exception.


#### 18) How do you debug a Python program? 

🔹 Best Practices for Debugging
✔ Start with print/logging for small bugs.
✔ Use assertions to validate conditions.
✔ For complex issues, use pdb or an IDE debugger.
✔ Log errors properly with logging.
✔ Optimize performance with cProfile.


#### 19) What is the Global Interpreter Lock (GIL) in Python? 
The Global Interpreter Lock (GIL) is a mutex (lock) that allows only one thread to execute Python bytecode 
at a time, even on multi-core processors.

2️⃣ How Does GIL Affect Multithreading?
Threads take turns executing (even on multi-core CPUs).
Only one thread runs at a time, causing performance issues for CPU-intensive tasks.
🔹 Even though two threads are created, due to GIL, Python executes them one at a time, instead of in parallel.
🔹 So multithreading doesn’t speed up CPU-bound tasks.

✅ 2. Use JIT Compilers (e.g., PyPy)
PyPy (an alternative Python implementation) reduces GIL impact by optimizing execution.
✅ 3. Use C Extensions (NumPy, Cython)
Libraries like NumPy and Cython use C code under the hood, bypassing the GIL for computations.

 #### How do you implement multithreading in Python? 

 #### 20) Difference Between threading and multiprocessing
 Multithreading:
 > Runs multiple threads within the same process                                                                           
 > ❌ No true parallelism (due to GIL)
 > I/O-bound tasks (file I/O, web scraping, database queries)
 > Shared memory between threads and Low (threads are lightweight)
 > ❌ Slower due to GIL
 > Web scraping, network calls, GUI applications

Multiprocessing:
> Runs multiple processes, each with its own memory
> ✅ True parallel execution on multiple CPU cores
> CPU-bound tasks (heavy computations, data processing)
> Each process has its own memory
>✅ Faster because processes run independently
> Data processing, machine learning, image processing



#### 21) What is REST, and how does it differ from SOAP? 
1) Diff between REST and SOAP
REST : 
>REST (Representational State Transfer) 
>An architectural style for designing networked applications
>Uses HTTP, HTTPS (lightweight)
>JSON, XML, Plain Text (human-readable)
>✅ Faster and more efficient (less overhead)
>✅ Simple, easy to integrate with web apps
>Stateless (each request is independent) and Web services, APIs (e.g., RESTful APIs in FastAPI, Flask, Django)
>Working with mobile, web applications, or microservices.
SOAP:
 > SOAP (Simple Object Access Protocol) 
 > A protocol that defines rules for structuring messages
 > Can use HTTP, SMTP, TCP (heavy)
 > XML (strict, bulky)
 > ❌ Strict XML format, less flexible
 > ❌ Complex, requires more setup
 > Stateful or Stateless
 > Financial transactions, banking services

 1️⃣ What is REST? 🌍
REST (Representational State Transfer) is a web service architecture that follows six constraints, including statelessness and resource-based communication.
Uses HTTP methods: GET- Retrieve data from a server
   POST-Add new data to the server
   PUT- Add new data to the server
   DELETE-,Remove data from the server
Returns JSON or XML (lightweight, human-readable).
Ideal for modern web and mobile applications.
 
 

 - How do you create a REST API using Flask or Django? 
 - Explain the role of middleware in Django. 



#### 24)  What is the difference between `git pull` and `git fetch`? 
Git ftech : 
> Downloads latest changes from the remote repository without merging
> No changes to your working directory
> ✅ Yes (safe, does not overwrite local work)	❌ Risky (may cause merge 

 Git Pull  – Fetch + Merge
 > Downloads and automatically merges changes into your local branch
 > Updates your local branch immediately
 > ❌ Risky (may cause merge conflicts)
                                                       
#### 25) What is the difference between Git and GitHub?
 >A version control system
                                                      



#### 26) How do you resolve a merge conflict in Git? 
When we Try to Merge the Branch,Git detects conflicts, it will show an error like:
CONFLICT (content): Merge conflict in file.py
Automatic merge failed; fix conflicts and then commit the result.
2️⃣ Identify the Conflicted Files
Run:
git status
You'll see output like:
both modified:   file.py
                                                       
3️⃣ Open the Conflicted File
The file will have conflict markers (<<<<<<<, =======, >>>>>>>), like this:
<<<<<<< HEAD
print("Hello from main branch")
=======
print("Hello from feature branch")
>>>>>>> feature-branch
HEAD represents your current branch (e.g., main).

The other section is from the branch you are merging.

4️⃣ Manually Fix the Conflict
Edit the file to keep the desired version:
print("Hello from feature branch - fixed version")
Then save the file.

5️⃣ Mark the Conflict as Resolved
After fixing all conflicts, stage the file:
git add file.py
6️⃣ Complete the Merge
git commit -m "Resolved merge conflict in file.py"
7️⃣ Push the Changes (If Needed)
git push origin main


#### 27) Which oops concepts you have implemented & How have you implemented abstraction and encapsulation 
As a Python developer with 3.5 years of experience, I have implemented various Object-Oriented Programming (OOP) concepts, 
including Abstraction, Encapsulation, Inheritance, and Polymorphism.
1. Abstraction
Definition: Abstraction hides the implementation details and only exposes the necessary functionalities.
Implementation:
> I have used abstract classes and methods in Python using the abc module.
Example: In one of my projects, I created an abstract base class for database connections, allowing different database implementations 
(SQL Server, Snowflake) to follow the same interface.
> This ensures that all database classes follow the same structure without exposing internal implementations.

2. Encapsulation
Definition: Encapsulation restricts direct access to certain object attributes and methods, ensuring controlled access.
Implementation:
> I have used private (__var) and protected (_var) variables to prevent direct modification.
> Example: I implemented encapsulation in a user authentication system where sensitive user data like passwords were stored securely.
Here, the password is encapsulated and cannot be accessed directly, ensuring data security.

#### 29) How have you handled null pointer exception 
Handling Null Pointer Exception in Python
Python does not have a direct Null Pointer Exception like Java or C++, but it has a similar concept—NoneType errors. 
These occur when you try to access attributes or call methods on a None object.
> Common Causes of Null Pointer (NoneType) Errors
> Accessing an attribute of a None object.
> Calling a method on None.
> Using None in operations where a valid object is expected.

#### 30) What is compile time and run time polymorphism? How have you implemented them?
1️⃣ Compile-Time Polymorphism (Method Overloading)
Definition:
> In Compile-Time Polymorphism, the method that will be executed is determined at compile time.
> Python does not support method overloading like Java or C++ (because Python allows dynamic typing), 
> but we can achieve similar behavior using default arguments or *args.

Implementation in Python
Using Default Arguments
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

calc = Calculator()
print(calc.add(5))         # Output: 5
print(calc.add(5, 10))     # Output: 15
print(calc.add(5, 10, 15)) # Output: 30

> Using *args for Variable-Length Arguments
class Calculator:
    def add(self, *args):
        return sum(args)

calc = Calculator()
print(calc.add(5))         # Output: 5
print(calc.add(5, 10))     # Output: 15
print(calc.add(5, 10, 15)) # Output: 30
Here, even though Python does not allow multiple methods with the same name, we achieve method overloading behavior by using *args or default values.

2️⃣ Run-Time Polymorphism (Method Overriding)
Definition:
In Run-Time Polymorphism, the method that will be executed is determined at runtime.
Achieved through method overriding in inheritance.

Implementation in Python
class Animal:
    def speak(self):
        return "Animal makes a sound"

class Dog(Animal):
    def speak(self):  # Overriding the parent class method
        return "Dog barks"

class Cat(Animal):
    def speak(self):  # Overriding the parent class method
        return "Cat meows"

# Run-time polymorphism
animals = [Dog(), Cat(), Animal()]
for animal in animals:
    print(animal.speak())  # Calls the overridden method based on the object type
Output:
Dog barks
Cat meows
Animal makes a sound
The method to be executed is determined at runtime, making it run-time polymorphism.


####31) Can you create an object of an interface?
> No, you cannot create an object of an interface because an interface is meant to be a blueprint for classes. In Python,
interfaces can be implemented using abstract base classes (ABCs) from the abc module.

from abc import ABC, abstractmethod
# Interface (Abstract Base Class)
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass  # No implementation

# Trying to create an object of the interface
animal = Animal()  # ❌ This will raise a TypeError

#### 32) What is the difference between array list and Linked list
An ArrayList and a LinkedList are both data structures used to store elements, but they differ in how they manage memory and perform operations. 
An ArrayList is backed by a dynamic array, meaning it provides fast random access (O(1)) since elements are stored in contiguous memory locations.
However, inserting or deleting elements in the middle requires shifting elements, making these operations O(n) in the worst case. On the other
hand, a LinkedList consists of nodes that store data along with pointers to the next (and sometimes previous) node. This makes insertion and 
deletion in the middle O(1) when a reference to the node is available, but random access is slow (O(n)) since traversal is required. 
ArrayLists are more memory efficient due to lower overhead, whereas LinkedLists use extra memory for pointers. 
If frequent modifications are needed, a LinkedList is preferable, but if fast access is required, an ArrayList is a better choice.

#### 33) What is map
map() Function in Python
> The map() function in Python is used to apply a function to each element in an iterable (list, tuple, etc.) and returns a map object 
(which is an iterator).

Syntax:
map(function, iterable)

Example:
numbers = [1, 2, 3, 4, 5]
doubled = map(lambda x: x * 2, numbers)
print(list(doubled))  # Output: [2, 4, 6, 8, 10]




>>𝗔𝗣𝗜𝘀:
34) What are RESTful APIs? How do they work?
--- Ans :1️⃣ Client Sends a Request
The client (browser, mobile app, or another service) sends an HTTP request to the server.
The request includes:
HTTP Method (e.g., GET, POST, PUT, DELETE).
URL (Endpoint) (e.g., /users, /products/123).
Headers (e.g., Authorization, Content-Type).
Body (for POST or PUT requests).

2️⃣ Server Processes the Request
The API receives the request and processes it using business logic.
It may query a database, perform calculations, or modify data.

3️⃣ Server Sends a Response
The API responds with:
HTTP Status Code (e.g., 200 OK, 404 Not Found).
Response Body (e.g., JSON data).
Headers (e.g., Content-Type: application/json).
                                                                                                
35)  What is the difference between PUT and POST methods in REST?
PUT:
> 	Used to update or create a resource at a specific location
> Idempotent (Sending the same request multiple times won’t change the result)
> The client specifies the resource URL (/users/123)
> Replaces an existing resource or creates a new one if it doesn’t exist
> Updating user details, replacing an existing file

 POST:
 > Used to create a new resource
 > Not idempotent (Repeated requests may create duplicate resources)
 > The server decides the resource URL (/users → Server assigns ID)
 > Contains data to create a resource
 > Submitting a form, adding a new user

36) How do you handle authentication and authorization in a REST API?
---> In a REST API, security is crucial to prevent unauthorized access. Authentication verifies who you are, 
while authorization determines what you can do. Below are common methods used to handle both

✅ Use HTTPS → Prevents data from being intercepted.
✅ Secure Tokens → Store JWTs in HTTP-only cookies instead of local storage.
✅ Limit API Rate → Prevent brute-force attacks using rate limiting.
✅ Encrypt Sensitive Data → Hash passwords using bcrypt.
✅ Use Expiring Tokens → Reduce risk of stolen tokens being used indefinitely.



37) How do you version REST APIs and why is it important?
🔄 Backward Compatibility → Prevents breaking changes for existing clients.
🚀 Continuous Improvement → Allows new features without disrupting old versions.
🛠 Bug Fixes & Enhancements → Maintains stable versions while updating new ones.
🎯 Multiple Client Support → Different clients can use different API versions.


38) What is the time complexity of merge sort?
Merge Sort is a divide and conquer algorithm that splits the array into halves, sorts them recursively, and merges them back.--	O(n log n)
There is no sorting algorithm called Binary Sort, but if you're referring to Binary Insertion Sort, 
it's a modified version of Insertion Sort where binary search is used to find the correct position of an element.--O(n²)
 
39)What are the status code are available?
Commonly Used Status Codes in REST APIs
200 OK → Successful GET request.
201 Created → New resource successfully created.
400 Bad Request → Invalid request format.
401 Unauthorized → Authentication failure.
403 Forbidden → User lacks permission.
404 Not Found → Resource does not exist.
500 Internal Server Error → Unexpected server failure.


40) What is the website cookies?
Cookies are small text files that websites store in your browser to remember information about you. They help improve user experience by
saving preferences, login sessions, and tracking user behavior.
✅ Enhance User Experience (Remember preferences & login info).
✅ Enable Shopping Carts (Without them, cart items would disappear).
✅ Improve Website Analytics (Track visitor behavior for improvements).
❌ Can Be Used for Tracking (Privacy concerns with third-party cookies).


#### Note --Use pip for libraries & frameworks.
Use pipx for standalone CLI tools.

Here are some of the most used Python string methods illustrated with examples:

🔹 Case Transformation:
"HELlo".lower() ➡️ hello
"hello".upper() ➡️ HELLO

🔹 Word Formatting:
"hello world".capitalize() ➡️ Hello world
"hello world".title() ➡️ Hello World

🔹 Trimming and Formatting:
" hello ".strip() ➡️ hello
"Hello".startswith("He") ➡️ True
"Hello".endswith("lo") ➡️ True

🔹 Search and Replace:
"hello".find("e") ➡️ 1
"hello".index("e") ➡️ 1
"hello world".count("o") ➡️ 2
"one,three".replace(",", " ") ➡️ one three

🔹 Splitting and Joining:
"one,three".split(",") ➡️ ['one', 'three']
"-".join(["a", "b", "c"]) ➡️ a-b-c

🔹 Validation:
"12345".isnumeric() ➡️ True


1. “How would you find the first non-repeating value in a column using SQL?”
2. “What’s your approach for optimizing a query that takes 15 minutes to run on a billion-row table?”
3. “How do NULLs affect GROUP BY and JOINs? Can you give examples?”
4. “How would you design a data model for a ride-sharing app?”
5. “Explain normalization vs denormalization. When would you choose either?”
 Write a Python script to read a large CSV file and perform transformations.
 - How would you handle missing data in a dataset programmatically?
 - Explain the use of decorators in Python.
