VM-WARE Interview question:
Total question 19
Solution 15
No-Resolved 4




1. Write a function to check if given machine is online using ping command.
Answer:

#!/usr/local/bin/python3

import subprocess

def check_connectivity(ip_addr):
    command = "ping {} -c 2".format(ip_addr).split()
    print("Wait for few second to check {} machine is pinging or not".format(ip_addr))
    obj = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    data_stdout = obj.stdout.readlines()
    data_stderr = obj.stderr.read()
    flag=False
    for line in reversed(data_stdout):
        if " 0% packet loss" in str(line,"utf-8").strip():
            flag=True
            break
    if flag:
        print("{} is pingable.".format(ip_addr))
    else:
        data_stderr=str(data_stderr,"utf-8").strip()
        if data_stderr != "":
            print("Error Message: {}".format(data_stderr))
        print("Unable to ping {}".format(ip_addr))

if __name__ ==  "__main__"    :
    machine=input("Enter the machine details for ping: ")
    check_connectivity(machine)


2. How we create modules in python.
Answer:
	In python every file is a module. We just need to write class, function in file and if we want use then we can using import keyword we can access that module.



3. Different ways to import modules in python

	To copy all functionality from mudule use syntax as e.g import <module_name>
	If we want access perticular class or function then we can use e.g from <module_name> import <function_name>


4. Given 2 lists, find the elements which are in 1st list and not in 2nd list
Answer:
	list1=[12,3,4,5,6,92,55,]
	list2=[1,4,8,3,66,2,5,67,0]
	""" to find element which are present in list1 but not present in list2"""

	for element in list1:
	    if element not in list2:
        	print(element)
    
        

5. module A has a code
print "Hello"
Whats is expected output if Module B has following code
import A
import A

Answer:
	Output will be only "Hello" one time only. Python maintains a dictionary named 'sys.modules' which is looked upon each time we do import of a module, if the module name as a 'key' already exists in the modules dictionary all the new imports is/are igonred as duplicate. 

	

6. Some coding on question on map, filter, reduce and lamdba expressions

Answer:   NR




7. find the even numbers from 1-100 (List comprehension)
Answer:
	list1=[number for number in range(1,101) if number&1 == 0]
	print(list1)




8. Can the 2nd argument in map/filter/reduce be a string or tuple ?
    Yes. Second argument in map can be string or tuple
        list1=list(map(str,(1,2,3)))
        print(list1)
        Python 3.6.1 (default, Dec 2015, 13:05:11)
        [GCC 4.8.2] on linux
   
        ['1', '2', '3']
        list1=list(map(int,"123"))
        print(list1)
        Python 3.6.1 (default, Dec 2015, 13:05:11)
        [GCC 4.8.2] on linux
   
        [1, 2, 3]
   



9. What is an iterator.
	Iteratior means creating some functionality using that we can iterate our container.



10. what is __init__  in class ?
Answer:

    The first method __init__() is a special method, which is called class constructor
or initialization method that Python calls when you create a new instance of this
class. Using __init__() we can initialize data member.

    
11. what is difference between __init__ and __new__
Answer:
    __call__ its overloaded of () and its calling to __new__ method.
    __new__ is creating object, allocating the memory and return allocated object reference
    __init__ is collecting the reference from __new__ and initialize variable value if programmer provided.




12. Explain the Overriding in multi-level inherihance


Answer:
class A():
  def fun(self):
    print("A:fun()")
class B(A):
    def fun(self):
      print("B:fun()")
  
class C(B):
  a=10
  
  def fun(self):
    super().fun()
    print("C:fun()")    
  
c_obj=C()
c_obj.fun()


output
Python 3.6.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
   
B:fun()
C:fun()




13. Diamond inheritance problem
Class A:
  def foo:
    # something
Class B(A):
  def foo:
    # something
Class C(A):
    def foo:
    # something
Class D(B,C):
   # no foo function
 
d = D()
d.foo()
Which class function will be invoked ?
Answer:
    B's foo function will be invok. As per MRO(Method resolution order)
 



12. Write a class whose objects are iterable
Answer:

class iterator():
    def __init__(self,limit):
        self.data=[i for i in range(limit)]
        self.count=0
    def __next__(self):
        if self.count<len(self.data):
            return_value = self.data[self.count]
            self.count += 1
            return return_value
        else:
            raise StopIteration("Out of index value")

try:
  obj=iterator(10)
  for i in range(12):
       print(next(obj))
except Exception as e:
    print(e)


output:
Python 3.6.1 (default, Dec 2015, 13:05:11)
[GCC 4.8.2] on linux
   
0
1
2
3
4
5
6
7
8
9
Out of index value
   



13. Difference between iterator and generator.
Answer:
    Generator ie useful for creating new container and iterator is useful for iterate existing data.

iterator is a more general concept: any object whose class has a next method (__next__ in Python 3) and an __iter__ method that does return self.
Every generator is an iterator, but not vice versa. A generator is built by calling a function that has one or more yield expressions (yield statements, in Python 2.5 and earlier), and is an object that meets the previous paragraph's definition of an iterator.

You may want to use a custom iterator, rather than a generator, when you need a class with somewhat complex state-maintaining behavior, or want to expose other methods besides next (and __iter__ and __init__). Most often, a generator (sometimes, for sufficiently simple needs, a generator expression) is sufficient, and it's simpler to code because state maintenance (within reasonable limits) is basically "done for you" by the frame getting suspended and resumed.

For example, a generator such as:
def squares(start, stop):
    for i in range(start, stop):
        yield i * i
generator = squares(a, b)

or the equivalent generator expression (genexp)

generator = (i*i for i in range(a, b))

would take more code to build as a custom iterator:

class Squares(object):
    def __init__(self, start, stop):
       self.start = start
       self.stop = stop
    def __iter__(self): return self
    def next(self):
       if self.start >= self.stop:
           raise StopIteration
       current = self.start * self.start
       self.start += 1
       return current

iterator = Squares(a, b)

But, of course, with class Squares you could easily offer extra methods, i.e.

    def current(self):
       return self.start

if you have any actual need for such extra functionality in your application.



14. fibonacci using generators for large numbers
Answer:
    
def fibonacci_series(number):
  a=0
  b=1
  c=0
  while c<number:
      yield c
      a,b=b,c
      c=a+b
number=eval(input("Enter number to print fibonacci series: "))
fib_series = fibonacci_series(number)
for i in fib_series:
  print(i,end=" ")


    Second solution:
    



14. Context managers, how they work, __entry__ and __exit__
Answer: NR



15. [1,,0,1,1,1,1,0,0,1,1,1] find the max sum of subsequence by flipping one 0 to 1 at a time.
Answer: NR

16. write code for Recursive directory traversal without os.walk.
Answer:    os.walk() function takes input as a path and return the 3 value in tuple format   current_directoryname, current_directory's_available_dir_name, current_directory_available_file in the tuple format recurssively.
    
devi@devi-Vostro-1540:~/hw$ cat ./example.py 
#!/usr/bin/python3
import os

def my_walk(path):
    for member in os.listdir(path):
        child=os.path.join(path,member)
        if os.path.isdir(child):
            my_walk(child)
        else:
            print(child)

path="/home/devi/hw/c"
my_walk(path)
devi@devi-Vostro-1540:~/hw$ 




17. Merging sequence [[1,3],[3,9],[11,17]] --> [[1,9],[11,17]]
Answer:
    devi@devi-Vostro-1540:~/hw$ cat ./example.py 
#!/usr/bin/python3


def new_list(list1):
    output_list=[]
    for index in range(len(list1)-1):
        if list1[index][1] == list1[index+1][0]:
            output_list.append([list1[index][0],list1[index+1][1]])
    return output_list
list1=[[1,2],[2,4],[3,5],[34,565],[565,565],[1,1]]
return_value=new_list(list1)
print("Input List: ",list1)
print("Output list: ",return_value)


devi@devi-Vostro-1540:~/hw$ ./example.py 
Input List:  [[1, 2], [2, 4], [3, 5], [34, 565], [565, 565], [1, 1]]
Output list:  [[1, 4], [34, 565]]
devi@devi-Vostro-1540:~/hw$ 






18. 12 ball with 1 defective, how many min iterations required to find it.
Answer: NR




19. Have u used decorator? Implement decorator functionality without @<decorator> syntax
Answer:  Decorator means provide extra functionality to existing function.


import time
def main_function(*args,**kargs):
    print("Inside main function")
    print("Input argument: {}".format(args, **kargs))
    time.sleep(5)
    return True

def decorator(fun_addr,*args,**kargs):
    import time
    t1=time.time()
    return_value=fun_addr(args,kargs)
    t2=time.time()
    print("Total execution time is {} second".format(t2-t1))
    return return_value

ret=decorator(main_function,10,11)
print("Return vaule main_function: {}".format(ret))
    



