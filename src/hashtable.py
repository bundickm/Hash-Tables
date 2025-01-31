# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        '''
        index = self._hash_mod(key)
        current_pair = self.storage[index]
        previous_pair = None

        while (current_pair is not None) and (current_pair.key != key):
            previous_pair = current_pair
            current_pair = previous_pair.next

        if current_pair is not None:
            current_pair.value = value
        else:
            next_pair = LinkedPair(key, value)
            next_pair.next = self.storage[index]
            self.storage[index] = next_pair


    def remove(self, key):
        '''
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        '''
        index = self._hash_mod(key)

        current_pair = self.storage[index]
        previous_pair = None

        while (current_pair is not None) and (current_pair.key != key):
            previous_pair = current_pair
            current_pair = previous_pair.next

        if current_pair is None:
            print("KEY ERROR: " + key)
        else:
            if previous_pair is not None:
                previous_pair.next = current_pair.next
            else:
                self.storage[index] = current_pair.next


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        '''
        index = self._hash_mod(key)
        current_pair = self.storage[index]

        while current_pair is not None:
            if current_pair.key == key:
                return current_pair.value
            current_pair = current_pair.next


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''
        self.capacity = self.capacity * 2
        old = self.storage
        self.storage = [None] * self.capacity
        current_pair = None

        for current_pair in old:
            while current_pair is not None:
                self.insert(current_pair.key, current_pair.value)
                current_pair = current_pair.next




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
