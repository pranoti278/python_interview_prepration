All the best and do your best , you are strong ,confidant and will achive great offer soon .

### 1) Write a Python function to find all unique pairs of integers in a list that sum up to a given target value

Ans:
-def find_unique_pair(nums,target):
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

#### How Do Decorators Work?
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


