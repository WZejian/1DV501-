from dataclasses import dataclass
from typing import Any

# The BstMap class is a binary search tree based implementation of
# a map (or dictionary). It works for any type of values and for
# all types keys that are comparable ==> we can compare keys using
# the operators < and >.


# The Node class is responsible for most of the work.
# Each call to the BstMap class is just delegated to the
# root node which starts a recursive sequence of calls to
# handle the request. Notice: All Node methods are recursive.
@dataclass
class Node:
    key: Any = None         # the key
    value: Any = None       # the value
    left: Any = None        # left child (a Node)
    right: Any = None       # right child (a Node)

    def put(self, key, value):
        if self.key == key:
            self.value = value
        elif key > self.key:
            if self.right is None:
                self.right = Node(key, value, None, None)
            else:
                self.right.put(key, value)
        elif key < self.key:
            if self.left is None:
                self.left = Node(key, value, None, None)
            else:
                self = self.left.put(key, value)

    def to_string(self):
        string = ''

        # Look down left branch
        if self.left is not None:
            string += self.left.to_string()

        # Add Node key and value
        string += '(' + self.key
        string += ', ' + str(self.value)
        string += ')' + ' '

        # Look down right branch
        if self.right is not None:
            string += self.right.to_string()

        return string

    def count(self):
        counter = 0
        # Left branch count
        if self.left is not None:
            counter += self.left.count()
        # Right branch count
        if self.right is not None:
            counter += self.right.count()
        counter += 1

        return counter

    def get(self, key):
        # Default if not in the tree
        value = None
        # Key found
        if key == self.key:
            value = self.value
        # Higher values
        if key > self.key:
            if self.right is not None:
                value = self.right.get(key)
        # Lower values
        if key < self.key:
            if self.left is not None:
                value = self.left.get(key)

        return value

    def max_depth(self):
        depth = 0
        l_depth = 0
        r_depth = 0

        # Check depth for left and right
        if self.left is not None:
            l_depth += self.left.max_depth()
        if self.right is not None:
            r_depth += self.right.max_depth()

        # See which is deeper
        if r_depth > l_depth:
            depth = r_depth
        else:
            depth = l_depth
        depth += 1

        return depth

    # We do a left-to-right in-order traversal of the tree
    # to get the key-value pairs sorted base on their keys
    def as_list(self, lst):
        tpl = (self.key, self.value)
        if self.left is not None:
            self.left.as_list(lst)
        lst.append(tpl)
        if self.right is not None:
            self.right.as_list(lst)

        return lst


# The BstMap class is rather simple. It basically just takes care
# of the case when the map is empty. All other cases are delegated
# to the root node ==> the Node class.
#
# The class below is complete ==> not to be changed
@dataclass
class BstMap:
    root: Node = None

    # Adds a key-value pair to the map
    def put(self, key, value):
        if self.root is None:    # Empty, add first node
            self.root = Node(key, value, None, None)
        else:
            self.root.put(key, value)

    # Returns a string representation of all the key-value pairs
    def to_string(self):
        if self.root is None:     # Empty, return empty brackets
            return "{ }"
        else:
            res = "{ "
            res += self.root.to_string()
            res += "}"
            return res

    # Returns the current number of key-value pairs in the map
    def size(self):
        if self.root is None:
            return 0
        else:
            return self.root.count()

    # Returns the value for a given key. Returns None
    # if key doesn't exist (or map is empty)
    def get(self, key):
        if self.root is None:
            return None
        else:
            return self.root.get(key)

    # Returns the maximum tree depth. That is, the length
    # (counted in nodes) of the longest root-to-leaf path
    def max_depth(self):
        if self.root is None:
            return 0
        else:
            return self.root.max_depth()

    # Returns a sorted list of all key-value pairs in the map.
    # Each key-value pair is represented as a tuple and the
    # list is sorted on the keys ==> left-to-right in-order
    def as_list(self):
        lst = []
        if self.root is None:
            return lst
        else:
            return self.root.as_list(lst)
