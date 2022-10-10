# Justin Rinehuls, Student ID: 006465984
from datetime import timedelta
from FileReader import FileReader
from HashTable import HashTable
from Truck import Truck


# New hash table and FileReader instance
ht = HashTable()
reader = FileReader()
# Load hash table with packages read from CSV file
reader.packages(ht)

# New 2D matrix. Loaded with distances from CSV file.
# Learned from https://stackoverflow.com/questions/4230000/creating-a-2d-matrix-in-python
distanceMatrix = [['' for j in range(27)] for i in range(27)]
reader.distances(distanceMatrix)

# New list. Loaded with addresses from CSV file.
addressList = []
reader.addresses(addressList)

# Create dictionary for package IDs and times delivered.
deliveryTimes = {}
# Create dictionary for package IDs and times picked up.
loadTimes = {}

# Create two truck objects
truck1 = Truck(1)
truck2 = Truck(2)

# For delivering aall packages on the truck. Starts with number of items on truck. calls the "deliver" method of the
# truck class. Sets the new status for the truck as delivered by truck id and the time. Adds that package ID and time
# to deliveryTimes dictionary and updates current location.
# Big O time complexity of O(n^2) because truck.deliver, which is O(n) is called inside a for loop.
# Space complexity of O(n) memory usage in linear relation to data size.
def deliverPackages(truck, currentLocation):
    listSize = len(truck.packageList)
    updated = False
    for package in range(listSize):
        packageID = truck.deliver(currentLocation, distanceMatrix, addressList)
        ht.search(packageID).setStatus("Delivered by Truck %s at: %s" % (truck, truck.currentTime))
        deliveryTimes[packageID] = str(truck.currentTime)
        currentLocation = truck.location
        # This checks the time for each delivery to see if it's 10:20 yet. If it is, package 9's address is updated.
        # A boolean "updated" is used so that the update only happens once.
        if int(str(truck.currentTime).replace(':','')) >= 102000 and updated == False:
            ht.search(9).setAddress("410 S State St")
            ht.search(9).setZip(84111)
            updated = True

# Just prints the packages on a new line in a loop. Big O time complexity of O(n) because of a single for loop.
# Space complexity of O(1) data is not added to a structure.
def printPackages():
    for i in range(40):
        print(ht.search(i + 1))

# Method for converting input time as int to time format. Big O time complexity of O(1) because it's constant regardless
# of input. Space complexity of O(1) because no new data is added to a data structure.
def intToTime():
    specifiedTime = 0
    # While loop prevents the program from crashing if user enters an unacceptable value.
    # The try/except block handles inproperly formatted inputs.
    while (specifiedTime == 0):
        try:
            time = input("What time do you want to search? (Formatted as hhmmss) ")
            specifiedTime = int(time)
        except ValueError:
            print("It must be formatted as hhmmss")
        # Separate digits into hours, minutes and seconds.
        hours = int(specifiedTime / 10000)
        minutes = int((specifiedTime / 100) % 100)
        seconds = int(specifiedTime % 100)
        # Check to make sure there are no invalid digits, like minute being 67 or something.
        if (hours > 23 or minutes > 59 or seconds > 59):
            print("Hours must be 0 - 23, minutes must be 0 - 59, and seconds must be 0 - 59 ")
            specifiedTime = 0
        # Format so if minutes is 9, it prints 09. Also add colons between hh:mm:ss
        else:
            print()
            print(f"The current time is {hours:02d}:{minutes:02d}:{seconds:02d}")
    return specifiedTime

# This is where the trucks get loaded and deliver. Big O time complexity of O(n^2) because deliver packages gets called
# in this method. Every other function call is faster than or as fast as O(n^2). Space complexity of O(n), memory usage
# in linear relation to data size.
def runDeliverySim():
    end = False
    while (not end):
        print("\n1. Deliver packages")
        print("2. Quit")
        choice = input("1 or 2? ")
        if choice == "1":
            # have to reset distances to 0 in case this method gets run a second time in the menu method below.
            truck1.totalDistance = 0
            truck2.totalDistance = 0
            # have to reset location to hub in case this method gets run a second time in the menu method below.
            truck1.location = "4001 South 700 East"
            truck2.location = "4001 South 700 East"
# --------------Loading Truck 1 for first load and adding package IDs and load times to loadTimes dictionary------------
            loadTimes[truck1.loadPackage(13, ht)] = str(truck1.currentTime)  # Must deliver together
            loadTimes[truck1.loadPackage(14, ht)] = str(truck1.currentTime)  # Must deliver together
            loadTimes[truck1.loadPackage(15, ht)] = str(truck1.currentTime)  # Must deliver together and by 9:00
            loadTimes[truck1.loadPackage(16, ht)] = str(truck1.currentTime)  # Must deliver together
            loadTimes[truck1.loadPackage(19, ht)] = str(truck1.currentTime)  # Must deliver together
            loadTimes[truck1.loadPackage(20, ht)] = str(truck1.currentTime)  # Must deliver together
            loadTimes[truck1.loadPackage(21, ht)] = str(truck1.currentTime)  # same address as 20
            loadTimes[truck1.loadPackage(27, ht)] = str(truck1.currentTime)  # same address as 35
            loadTimes[truck1.loadPackage(34, ht)] = str(truck1.currentTime)  # same address as 15
            loadTimes[truck1.loadPackage(35, ht)] = str(truck1.currentTime)  # same address as 27
            loadTimes[truck1.loadPackage(39, ht)] = str(truck1.currentTime)  # same address as 13
            # Delivering the first load.
            deliverPackages(truck1, truck1.location)
            # Return to hub for more packages
            truck1.returnToHub(truck1.location, distanceMatrix, addressList)

# -------------Loading Truck 1 for second load and adding package IDs and load times to loadTimes dictionary------------
            loadTimes[truck1.loadPackage(6, ht)] = str(truck1.currentTime)  # delayed until 9:05 deliver by 10:30
            loadTimes[truck1.loadPackage(25, ht)] = str(truck1.currentTime)  # delayed until 9:05 deliver by 10:30
            loadTimes[truck1.loadPackage(26, ht)] = str(truck1.currentTime)  # same address as 25
            loadTimes[truck1.loadPackage(28, ht)] = str(truck1.currentTime)  # delayed until 9:05
            loadTimes[truck1.loadPackage(31, ht)] = str(truck1.currentTime)  # deliver by 10:30 and goes with 32
            loadTimes[truck1.loadPackage(32, ht)] = str(truck1.currentTime)  # delayed until 9:05  and goes with 31
            # Delivering the second load
            deliverPackages(truck1, truck1.location)
# -------------Loading Truck 2 for first load and adding package IDs and load times to loadTimes dictionary-------------
            loadTimes[truck2.loadPackage(1, ht)] = str(truck2.currentTime)  # deliver by 10:30
            loadTimes[truck2.loadPackage(2, ht)] = str(truck2.currentTime)  # same address as 33
            loadTimes[truck2.loadPackage(3, ht)] = str(truck2.currentTime)  # only on truck 2
            loadTimes[truck2.loadPackage(4, ht)] = str(truck2.currentTime)  # same address as 40
            loadTimes[truck2.loadPackage(5, ht)] = str(truck2.currentTime)  # same address as 38
            loadTimes[truck2.loadPackage(7, ht)] = str(truck2.currentTime)  # same address as 29
            loadTimes[truck2.loadPackage(8, ht)] = str(truck2.currentTime)  # same address as 30
            loadTimes[truck2.loadPackage(18, ht)] = str(truck2.currentTime)  # only on truck 2
            loadTimes[truck2.loadPackage(29, ht)] = str(truck2.currentTime)  # deliver by 10:30
            loadTimes[truck2.loadPackage(30, ht)] = str(truck2.currentTime)  # deliver by 10:30
            loadTimes[truck2.loadPackage(33, ht)] = str(truck2.currentTime)  # same address as 2
            loadTimes[truck2.loadPackage(36, ht)] = str(truck2.currentTime)  # only on truck 2
            loadTimes[truck2.loadPackage(37, ht)] = str(truck2.currentTime)  # deliver by 10:30
            loadTimes[truck2.loadPackage(38, ht)] = str(truck2.currentTime)  # only on truck 2
            loadTimes[truck2.loadPackage(40, ht)] = str(truck2.currentTime)  # deliver by 10:30
            # Delivering the first load
            deliverPackages(truck2, truck2.location)
            truck2.returnToHub(truck2.location, distanceMatrix, addressList)
# -------------Loading Truck 2 for second load and adding package IDs and load times to loadTimes dictionary------------
            loadTimes[truck2.loadPackage(9, ht)] = str(truck2.currentTime)  # Update address at 10:20
            loadTimes[truck2.loadPackage(10, ht)] = str(truck2.currentTime)  # That's what's left
            loadTimes[truck2.loadPackage(11, ht)] = str(truck2.currentTime)  # That's what's left
            loadTimes[truck2.loadPackage(12, ht)] = str(truck2.currentTime)  # That's what's left
            loadTimes[truck2.loadPackage(17, ht)] = str(truck2.currentTime)  # That's what's left
            loadTimes[truck2.loadPackage(22, ht)] = str(truck2.currentTime)  # That's what's left
            loadTimes[truck2.loadPackage(23, ht)] = str(truck2.currentTime)  # That's what's left
            loadTimes[truck2.loadPackage(24, ht)] = str(truck2.currentTime)  # That's what's left
            # Delivering the second load
            deliverPackages(truck2, truck2.location)
            # ---------------------------------------Display packages-----------------------------------------
            printPackages()
            # have to reset times to 8:00 in case this method gets run a second time in the menu method below.
            truck1.currentTime = timedelta(hours=8.0, minutes=0.0)
            truck2.currentTime = timedelta(hours=8.0, minutes=0.0)
            # Bring up the menu options
            menu()
            end = True
        elif choice == "2":
            end = True
        else:
            print("Try again")

# This method contains the options for looking up things like: a specific package at a specific time, all packages
# at a specific time, and total distance of the trucks. Big O time complexity of O(n^2) because deliver packages gets
# called in this method. Every other function call is faster than or as fast as O(n^2). Space complexity of O(1),
# because no new data is added.
def menu():
    end = False
    while (not end):
        global ht
        print("\n1. Display all packages at a certain time")
        print("2. Look up a single package by package ID")
        print("3. See total miles of trucks")
        print("4. Quit")
        choice = input("1, 2, 3, or 4? ")
        if choice == "1":
            # Call intToTime to get time from user
            specifiedTime = intToTime()
            i = 0
            # Loops through both deliveryTimes and loadTimes dictionaries and compares to specified times to determine
            # (actually set) package status
            for key, value in deliveryTimes.items():
                # Set the old address for package 9 for times before 10:20.
                if int(specifiedTime) < 102000:
                    ht.search(9).setAddress("300 State St")
                    ht.search(9).setZip(84103)
                # replace method removes colons, get method returns key. Inside the loadTimes.get()
                # there is deliveryTimes.keys() which is cast to a list so that keys can be indexed. the counter i
                # starts at zero, so it gets the first key in deliverTimes. This is so that the loadTimes and
                # deliveryTimes are getting the same key (package ID) as each other for each run of the loop.
                # if the time selected is before it was picked up, then it's at the hub. If the time selected is after
                # being picked up, but before being delivered, it is in route. Times are cast to integers for
                # comparison. I got the idea of "list(deliveryTimes.keys())" from Biarys on a Stack Overflow post.
                # https://stackoverflow.com/questions/36090175/how-to-get-position-of-key-in-a-dictionary-in-python
                if int(specifiedTime) <= int(loadTimes.get(list(deliveryTimes.keys())[i]).replace(':','')):
                    ht.search(key).setStatus("At Hub")
                elif int(specifiedTime) > int(loadTimes.get(list(deliveryTimes.keys())[i]).replace(':','')) and int(specifiedTime) < int(deliveryTimes.get(key).replace(':','')):
                    ht.search(key).setStatus("En Route")
                i+=1
            printPackages()
            # Have to run delivery sim again to reset statuses back to normal in case someone wants to search with a
            # different time.
            runDeliverySim()
            end = True
        elif choice == "2":
            # While loop prevents the program from crashing if user enters an unacceptable value.
            # The try/except block handles non-integer inputs.
            package = "Not found"
            #specifiedTime = 0
            while(package == "Not found"):
                try:
                    id = input("Which package ID do you want to search? (1 - 40) ")
                    package = ht.search(int(id))
                except ValueError:
                    print("Please enter an integer.")
            # Call intToTime to get time from user
            specifiedTime = intToTime()
            # Set the old address for package 9 for times before 10:20.
            if specifiedTime < 102000:
                ht.search(9).setAddress("300 State St")
                ht.search(9).setZip(84103)
            # This works just like in the above for searching all packages, but it's only one, no no loop needed.
            if specifiedTime <= int(loadTimes.get(int(id)).replace(':','')):
                package.setStatus("At Hub")
            elif specifiedTime > int(loadTimes.get(int(id)).replace(':', '')) and int(specifiedTime) < int(deliveryTimes.get(int(id)).replace(':', '')):
                package.setStatus("En Route")
            print(package)
            # Have to run delivery sim again to reset status back to normal in case someone wants to search with a
            # different time.
            runDeliverySim()
            end = True
        elif choice == "3":
            # Just print truck mileage.
            print("Truck 1 total distance: ", truck1.totalDistance)
            print("Truck 2 total distance: ", truck2.totalDistance)
            print("Total distance of both trucks: ", truck1.totalDistance + truck2.totalDistance)
        elif choice == "4":
            end = True
        else:
            print("Try again")
#----------------------------------------------Finally, run the program-------------------------------------------------
runDeliverySim()

print("\nEnd program")