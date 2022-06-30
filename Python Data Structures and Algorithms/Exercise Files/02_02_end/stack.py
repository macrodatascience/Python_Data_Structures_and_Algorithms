"""
Python Data Structures - A Game-Based Approach
Stack class
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
        # return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            return None


    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    # this magic method allows to view the content of the object (rather than the address)

    def __str__(self):
        return str(self.items)

    def __repr__(self):
        return repr(self.items)
# if this is the main file that is being executed then run the code below. otherwise only import the above class and its methods

if __name__ == "__main__":
    s1 = Stack()
    s2 = Stack()
    print(s1, s2)
    print(s1.is_empty())
    s1.push([1, 2, 3, 4])
    print(s1)
    s1.push(90)
    s1.push('abc')
    s1.push('{1,2,3}')
    print(s1)
    print(s1.pop())
    print(s1)
    print(s1.peek())
    print(s1.size())
    print(str(s1))
    print(repr(s1))