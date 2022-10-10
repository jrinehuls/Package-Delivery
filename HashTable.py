# HashTable class for storing package IDs <keys> and packages <values>.
# Most information learned from zyBooks 7.8.2 and "Let's Go Hashing" webinar, but modified to suit my preferences.
class HashTable:
    # Constructor assigns empty buckets.
    def __init__(self):
        # initialize the hash table with 10 empty buckets for lists to be stored into.
        self.table = []
        for index in range(10):
            self.table.append([])

    # Inserts new key-value pair into the hash table. Implemented in FileReader
    # Big O time complexity of O(1) runs in constant time.
    # Space complexity of O(1) data increases at same degree regardless of input.
    def insert(self, packageID, package):
        # Decides the index of the bucket the key-value pair will go into based on key % number of buckets
        index = packageID % len(self.table)
        # The bucket the key-value pair will go in
        bucket = self.table[index]
        # Insert the key-value pair to the end of the bucket list.
        bucket.append([packageID, package])

    # Searches for a value with matching key in the hash table.
    # Returns the value if found, or "Not found" if not found.
    # Big O time complexity of O(n) because of single for loop.
    # Space complexity of O(1) data stays the same regardless of input.
    def search(self, packageID):
        # Same explanation as in insert method for variables
        index = packageID % len(self.table)
        bucket = self.table[index]
        # search for the key in the bucket list
        for pair in bucket:
            if pair[0] == packageID:
                # Return the value of the key
                return pair[1]
        # If not found, return not found
        return "Not found"