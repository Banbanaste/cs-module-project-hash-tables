class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insertFirst(self, entry):
        entry.next = self.head
        self.head = entry

    def find(self, key):
        current = self.head
        while current:
            if current.key == key:
                return current
            current = current.next
        return None

    def delete(self, val):
        current = self.head

        if current.value == val:
            self.head = self.head.next
            return current

        previous = current
        current = current.next

        while current:
            if current.value == val:
                previous.next = current.next
                return current
            else:
                previous = previous.next
                current = current.next

        return None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here

        self.count = 0

        if capacity > MIN_CAPACITY:
            self.data = [LinkedList() for i in range(capacity)]
            self.capacity = capacity
        else:
            self.data = [LinkedList() for i in range(MIN_CAPACITY)]
            self.capacity = MIN_CAPACITY

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.count / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # Your code here
        hash = 5381
        for c in key:
            hash = (hash * 33) + ord(c)
        return hash

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.fnv1(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        self.count += 1

        slot = self.hash_index(key)
        entry = HashTableEntry(key, value)
        self.data[slot].insertFirst(entry)

        """ print("in the HT PUT:\nslot:", slot, "\nlist:",
              self.data[slot], "\nentry:", entry) """

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)
        hash_entry_list = self.data[slot]
        hash_entry = hash_entry_list.find(key)

        if hash_entry is not None:
            self.count -= 1
            hash_entry_list.delete(hash_entry.value)
            return

        return None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        slot = self.hash_index(key)

        hash_entry_list = self.data[slot]
        hash_entry = hash_entry_list.find(key)

        """ print("in the HT GET:\nslot:", slot, "\nlist:",
              hash_entry_list, "\nentry:", hash_entry) """

        if hash_entry is not None:
            return hash_entry.value

        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        old_capacity = self.capacity
        self.capacity = new_capacity
        old_data = self.data
        self.data = [LinkedList()] * new_capacity
        for i in self.data:
            current = i.head
            while True:
                if current is not None:
                    self.put(current.key, current.value)
                    current = current.next
                if current is None:
                    break


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    ht.resize(10)

    print("")
