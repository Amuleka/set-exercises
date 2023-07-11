# Set

A. Introduction to Sets
In computer science, a set is an abstract data type that represents a collection of unique elements. It does not allow duplicate values, and the order of elements is typically not important. Sets are useful for modeling situations where uniqueness is required.

# Set Operations (Add, Remove, Contains)

    Add Operation:
        The add operation adds an element to the set.
        Implementation: Depending on the underlying data structure, adding an element to a set can be done efficiently by checking for duplicates and adding the element if it doesn't already exist.

    Remove Operation:
        The remove operation removes an element from the set if it exists.
        Implementation: Removing an element from a set involves searching for the element and deleting it if found.

    Contains Operation:
        The contains operation checks whether an element is present in the set.
        Implementation: This operation involves searching for the element in the set and returning a boolean value indicating its presence.

# Implementing a Set using an Array, Linked List, or Hash Table

Sets can be implemented using different data structures:

    Array-based Set:
        An array-based set uses an array to store elements. Adding an element requires checking for duplicates, and removing an element involves shifting the elements to fill the gap.

    Linked List-based Set:
        A linked list-based set uses a linked list to store elements. Adding an element involves traversing the list to check for duplicates, and removing an element requires updating the list connections.

    Hash Table-based Set:
        A hash table-based set uses a hash table or hash set data structure for efficient element storage and retrieval. Adding, removing, and checking for element existence can be done in constant time (on average) using the hashing technique.

# Set Operations Complexity Analysis

The time complexity of set operations depends on the underlying implementation:

    For an array-based set, adding and removing elements typically have a time complexity of O(n), where n is the number of elements in the set. Searching for an element has a time complexity of O(n) as well.
    For a linked list-based set, adding and removing elements also have a time complexity of O(n). However, searching for an element has a time complexity of O(n) in the worst case but can be optimized to O(1) with additional bookkeeping.
    For a hash table-based set, the average time complexity for adding, removing, and checking for an element is O(1), while the worst-case time complexity can be O(n) if there are many hash collisions.

# Set Intersection, Union, and Difference Operations

In addition to the basic set operations, sets also support operations to combine or compare multiple sets:

    Intersection: Returns a new set containing the common elements present in both sets.
    Union: Returns a new set containing all the elements from both sets without duplicates.
    Difference: Returns a new set containing the elements present in the first set but not in the second set.

These set operations provide convenient ways to work with multiple sets and perform logical operations on their elements.

## Exercise: Implementing a Set

In this exercise, we will implement a set data structure using a Python class. We will focus on the fundamental operations of a set: adding elements, removing elements, checking membership, and getting the size of the set.

1. Create an empty set using the `set()` constructor or the curly braces `{}` notation.

2. Implement the `add(element)` operation:

   - This operation adds an element to the set.
   - Use the `add()` method of the set to add the element.
   - Here's an example implementation of `add`:

   ```python
   def add(element):
       my_set.add(element)
   ```

3. Implement the remove(element) operation:

   - This operation removes an element from the set.
   - Use the remove() method of the set to remove the element.
   - Here's an example implementation of remove:

   ```python
   def remove(element):
       my_set.remove(element)
   ```

4. Implement the contains(element) operation:

   - This operation checks if an element is present in the set.
   - Use the in operator to check if the element is in the set.
   - Here's an example implementation of contains:

   ```python
   def contains(element):
       return element in my_set
   ```

5. Implement the size() operation:

   - This operation returns the number of elements in the set.
   - Use the len() function to get the length of the set.
   - Here's an example implementation of size:

   ```python
   def size():
      return len(my_set)
   ```

6. Test your set implementation by performing the following operations:

   - Call the add operation to add elements to the set.
   - Call the remove operation to remove an element from the set.
   - Call the contains operation to check if an element is present in the set.
   - Call the size operation to get the size of the set.

   ```python
   add(10)
   add(20)
   add(30)
   remove(20)
   print(contains(10))   # Expected output: True
   print(contains(20))   # Expected output: False
   print(size())         # Expected output: 2
   ```

# Practice

It is time to test your knowledge. Click on [this link](https://github.com/Amuleka/set-exercises/blob/main/set-incomplete.py) to do the exercise.

Once you've done it or tried it for a couple of times you can check the solution [here](https://github.com/Amuleka/set-exercises/blob/main/set-complete.py).
