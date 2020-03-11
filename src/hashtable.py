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

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            self.storage[index] = LinkedPair(key, value)
        else:
            node = self.storage[index]
            while True:
                if node.key == key:
                    node.value = value
                    break
                elif node.next is None:
                    node.next = LinkedPair(key, value)
                    break
                else:
                    node = node.next


    def _insert_node(self, node):
        self.insert(node.key, node.value)
        if node.next is not None:
            self._insert_node(node.next)


    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is None:
            print(f"error: key {key} not found")
        elif self.storage[index].key == key:
            node = self.storage[index]
            self.storage[index] = node.next
        else:
            node = self.storage[index]
            while node.next is not None:
                if node.next.key == key:
                    node.next = node.next.next
                    break
                else:
                    node = node.next
        
            


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        node = self.storage[index]
        
        while True:
            if node is None:
                return None
            elif node.key == key:
                return node.value
            else:
                node = node.next
          


    # def resize(self):
    #     '''
    #     Doubles the capacity of the hash table and
    #     rehash all key/value pairs.

    #     Fill this in.
    #     '''
    #     old_storage = self.storage.copy()
    #     self.capacity *= 2
    #     self.storage = [None]*self.capacity

    #     for bucket_item in old_storage:
    #         self.insert(bucket_item.key, bucket_item.value)



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
