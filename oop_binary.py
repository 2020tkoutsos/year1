class Node():

    def __init__(self, data):
        self.right = none
        self.left = none
        self.data = data

    def insert(self, data):
        if self.data:
            # left hand side
            if data <= self.data:
                if self.left == none:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # right hand side
            elif data > self.data:
                if self.right == none:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
    def find_value(self, value):
        if value < self.data:
            if self.left  is None:
                return str(value) + "not in tree"
            return self.right.find(value)
        elif:
            if value > self.data:
                if self.left  is None:
                    return(value + "not in tree")
                return self.right.find(value)
            else:
                print(str(self.data)) + "in tree"


root = Node(100)
root.insert(98)
root.insert(50)
root.insert(1984)
root.insert(143)
root.insert(54)
root.insert(2001)
root.insert(501)


print(root.find(501))
print(root.make_array(arr=[]))
