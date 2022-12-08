# Package Delivery

Simulation of a parcel delivery service in Salt Lake City, UT. There are about 40 packages to be delivered to 27 addresses by two trucks.
The goal is to deliver all packages under a total distance of 140 miles. On top of that, there are various constraints for many of the packages, such as packages not arriving at the hub on time, some packages must be delivered by a certain time, some packages must go out on the same truck together, etc. Those constraints have to be factored in to determine which packages to load onto which trucks and what time to pick them up. A nearest neighbor algorithm is used to determine in which order to deliver the packages on each truck.
