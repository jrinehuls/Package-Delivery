from datetime import timedelta

class Truck:

    def __init__(self, truckID):
        # initialize the hash table with 10 empty buckets for lists to be stored into.
        self.packageList = []
        self.totalDistance = 0
        self.location = "4001 South 700 East"
        self.currentTime = timedelta(hours=8.0, minutes=0.0)
        self.truckID = truckID

    # Loads packages into the package list. # Big O time complexity of O(1) runs in constant time.
    # Space complexity of O(1) no data added at constant rate regardless of input.
    def loadPackage(self, packageID, hashtable):
        # Gets the package from the hash table and adds to list
        self.packageList.append(hashtable.search(packageID))
        return packageID

    # Gets the distance between 2 addresses.
    # Big O time complexity of O(1) runs in constant time. Space complexity of O(1) no data is added to memory.
    def getDistance(self, currentLocation, nextAddress, distanceMatrix, addressList):
        # inputs the indecies of 2 addresses to the matrix to get the value at that index
        distance = distanceMatrix[addressList.index(currentLocation)][addressList.index(nextAddress)]
        # Just switch order of indecies if there is no data at that index.
        if distance == '':
            distance = distanceMatrix[addressList.index(nextAddress)][addressList.index(currentLocation)]
        return distance

    # Nearest neighbor algorithm for delivering packages. Big O time complexity of O(n) because of single for loop.
    # Space complexity of O(1) data is removed from list, not added.
    def deliver(self, currentLocation, distanceMatrix, addressList):
        # Closest is distance to the closest destination. Initialized to 20 because all addresses are closer
        # than 20 miles from each other.
        closest = 20
        destAddress = "address"
        packageID = 0
        index = 0
        # Loop through all packages in the truck's packageList.
        for i in self.packageList:
            # Get address of package
            nextAddress = i.address
            # Calculate distance to that address
            distance = self.getDistance(currentLocation, nextAddress, distanceMatrix, addressList)
            # if that distance is less than the value of the "closest" variable, we update the values for closest, the
            # destination address, the package ID, and the index of that package in the package list.
            if distance < closest:
                closest = distance
                destAddress = nextAddress
                packageID = i.packageID
                index = self.packageList.index(i)
        # Adds that closest distance to the truck's totalDistance. (Add miles to the odometer so to speak)
        self.totalDistance += closest
        # Remove that package from the truck
        self.packageList.pop(index)
        # Update location to that nearest neighbor since that's where we are now.
        self.location = destAddress
        # Keeping track of time. Time is added based on truck speed of 18mph. Time taken to travel
        # to that address is added to current time.
        self.currentTime += timedelta(minutes=60*closest/18.0)
        return packageID

    # To go back and get more packages. Big O time complexity of O(1) runs in constant time.
    # Space complexity of O(1) no data is added to memory.
    def returnToHub(self, currentLocation, distanceMatrix, addressList):
        # Works pretty much like deliver, except there's no package list since the truck isn't delivering, just driving.
        distance = distanceMatrix[addressList.index(currentLocation)][addressList.index("4001 South 700 East")]
        self.totalDistance += distance
        self.currentTime += timedelta(minutes=60*distance/18.0)
        self.location = "4001 South 700 East"
        return timedelta(minutes=60*distance/18.0)

    # So deliver packages method in Main can print the truck ID as a string
    def __str__(self):
        return "%s" % (self.truckID)