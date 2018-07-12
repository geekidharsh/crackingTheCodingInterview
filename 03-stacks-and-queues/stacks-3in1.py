# # Describe how you could use a single array to implement three stacks

# ''' solution: 
# 1. Method 1 (Divide the space in two halves)
# fixed stack solution: 
# A simple way to implement two stacks is to divide the array in two halves and assign the half half space to two stacks, i.e., use arr[0] to arr[n/2] for stack1, and arr[(n/2) + 1] to arr[n-1] for stack2 where arr[] is the array to be used to implement two stacks and size of array be n.

# The problem with this method is inefficient use of array space. A stack push operation may result in stack overflow even if there is space available in arr[]. For example, say the array size is 6 and we push 3 elements to stack1 and do not push anything to second stack2. When we push 4th element to stack1, there will be overflow even if we have space for 3 more elements in array.

# 2. Method 2 (A space efficient implementation)
# flexible stack solution
# This method efficiently utilizes the available space. It doesn’t cause an overflow if there is space available in arr[]. The idea is to start two stacks from two extreme corners of arr[]. stack1 starts from the leftmost element, the first element in stack1 is pushed at index 0. The stack2 starts from the rightmost corner, the first element in stack2 is pushed at index (n-1). Both stacks grow (or shrink) in opposite direction. To check for overflow, all we need to check is for space between top elements of both stacks. This check is highlighted in the below code.
# '''



# # Python Script to Implement a multi stack
class MultiStack:

    def __init__(self, stacksize):
        self.numstack = 3
        self.array = [0]*(stacksize*self.numstack)
        self.size = [0]*self.numstack
        self.stacksize = stacksize

    def Push(self, item, stacknum):
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        value = self.array[self.IndexOfTop(stacknum)]
        self.array[self.IndexOfTop(stacknum)] = 0
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1













































































# class multiStacks:     

#     def __init__(self, n):     #constructor
#         self.size = n
#         self.arr = [None] * n
#         self.top1 = -1
#         self.top2 = self.size
         
#     # Method to push an element x to stack1
#     def push1(self, x):
         
#         # There is at least one empty space for new element
#         if self.top1 < self.top2 - 1 :
#             self.top1 = self.top1 + 1
#             self.arr[self.top1] = x
 
#         else:
#             print("Stack Overflow ")
#             exit(1)
 
#     # Method to push an element x to stack2
#     def push2(self, x):
 
#         # There is at least one empty space for new element
#         if self.top1 < self.top2 - 1:
#             self.top2 = self.top2 - 1
#             self.arr[self.top2] = x
 
#         else :
#            print("Stack Overflow ")
#            exit(1)
 
#     # Method to pop an element from first stack
#     def pop1(self):
#         if self.top1 >= 0:
#             x = self.arr[self.top1]
#             self.top1 = self.top1 -1
#             return x
#         else:
#             print("Stack Underflow ")
#             exit(1)
 
#     # Method to pop an element from second stack
#     def pop2(self):
#         if self.top2 < self.size:
#             x = self.arr[self.top2]
#             self.top2 = self.top2 + 1
#             return x
#         else:
#             print("Stack Underflow")
#             exit()
#  