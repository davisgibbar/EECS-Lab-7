from stack import stack_class
from queue import queue_class
from linked_list import Linked_List
import time

def single_pop():
    print("Times for single pop:")
    my_stack = stack_class()
    for i in range(100):
        for j in range(1000):
            my_stack.push(j)
        start_time = time.process_time_ns()
        my_stack.pop()
        end_time = time.process_time_ns()
        my_stack.push(i)
        print(end_time-start_time)

def all_pop():
    print("Times for popping all:")
    my_stack = stack_class()
    for i in range(100):
        for j in range(1000):
            my_stack.push(j)
    start_time = time.process_time()
    for i in range(100):
        for j in range(1000):
            my_stack.pop()
        end_time = time.process_time()
        print(end_time - start_time)
        for k in range(i*1000):
            my_stack.push(k)


def time_enqueue():
    print("Times for enqueue:")
    my_queue = queue_class()
    start_time = time.process_time()
    for i in range(100):
        for j in range(1000):
            my_queue.enqueue(j)
        end_time = time.process_time()
        print(end_time - start_time)

def list_index_0():
    print("Times for get entry of index 0 of linked list:")
    my_LL = Linked_List()
    for i in range(100):
        for j in range(1000):
            my_LL.insert(0,j)
        start_time = time.process_time_ns()
        my_LL.get_entry(0)
        end_time = time.process_time_ns()
        print(end_time - start_time)

def list_index_last():
    print("Times for get entry of last index of linked list:")
    my_LL = Linked_List()
    for i in range(1):
        for j in range(10):
            my_LL.insert(0,j)
        start_time = time.process_time_ns()

        for i in range(10):
            print('entry at '+str(i) + 'is ='+ str(my_LL.get_entry(i)))
        print('len is = ' + str(my_LL.length()))
        print('len is 1 = ' + str(int(my_LL.length())-1))
        print('entry is last = ' + str(int(my_LL.length())-1))
        print('check-->'+ str(my_LL.get_entry(9)))
        my_LL.get_entry(int(my_LL.length())-1)
        end_time = time.process_time_ns()
        print(end_time - start_time)

def print_all_get_entry_LL():
    my_LL = Linked_List()
    for i in range(100):
        for j in range(1000):
            my_LL.insert(0, j)
    for i in range(100):
        start_time = time.process_time_ns()
        for j in range(1000):
            print(my_LL.get_entry(j+i*1000))
        end_time = time.process_time_ns()
        print(f"Time outputs: {end_time-start_time}")

def executive():
    #single_pop()
    #all_pop()
    #time_enqueue()
    #list_index_0()
    #list_index_last()
    #print_all_get_entry_LL()

executive()