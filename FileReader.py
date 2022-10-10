import csv

from Package import *

class FileReader:
    #Found out how to read into a list here: https://stackoverflow.com/questions/24662571/python-import-csv-to-list
    # Loads the hash table with packages from the Packages.csv file. Each package has the info input into the hash
    # table's insert function.
    # Big O time complexity of O(n) because of single for loop. Space complexity of O(n) data and space grow at same rate.
    def packages(self, ht):
        with open('Packages.csv', 'r') as packageFile:
            packageReader = csv.reader(packageFile)
            for package in packageReader:
                packageID = int(package[0])
                address = package[1]
                city = package[2]
                state = package[3]
                zip = int(package[4])
                deadline = package[5]
                weight = int(package[6])
                status = "At Hub"
                # A new package with all needed info is created and added to the hash table.
                package = Package(packageID, address, city, state, zip, deadline, weight, status)
                ht.insert(packageID, package)

    # Loads the distance matrix with floating point numbers from the Distances.csv file
    # Big O time complexity of O(n^2) because of nested for loops. Space complexity of O(n) data and space grow at same rate.
    def distances(self, distanceMatrix):
        j = 0
        with open('Distances.csv', 'r') as distanceFile:
            distanceReader = csv.reader(distanceFile)
            for row in distanceReader:
                for col in range(27):
                    # Only updates matrix at indecies where there is a value in the Distance.csv file.
                    if row[col] != '':
                        distanceMatrix[j][col] = float(row[col])
                j+=1

    # Loads the address list with addresses from the Addresses.csv file
    # Big O time complexity of O(n) because of single for loop. Space complexity of O(n) data and space grow at same rate.
    def addresses(self, addressList):
        with open('Addresses.csv') as addressFile:
            addressReader = csv.reader(addressFile)
            for row in addressReader:
                addressList.append(row[0])

