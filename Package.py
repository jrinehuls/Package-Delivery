class Package:
    # Class constructor for setting variable values.
    def __init__(self, packageID, address, city, state, zip, deadline, weight, status):
        self.packageID = packageID
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.deadline = deadline
        self.weight = weight
        self.status = status
    # Sets package's status
    def setStatus(self, status):
        self.status = status
    # Sets package's address
    def setAddress(self, address):
        self.address = address
    # Sets package's zip code
    def setZip(self, zip):
        self.zip = zip
    # Converts a package object to a string
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.packageID, self.address, self.city, self.state, self.zip,
        self.deadline, self.weight, self.status)