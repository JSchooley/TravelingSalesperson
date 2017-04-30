'''
A program that takes in a file that has a specific format 
with a from city, a to city and the distance it takes 
to get there.
    
@author: Josh Schooley
'''

import sys
import copy

class TSPProblem:
    
    '''
    Reads in the specified input file containing
    cities and distances and constructs an
    adjacency list with those distances.

    The adjacency list is a dictionary that maps
    a from city to a tuple of a to city and the 
    distance required to reach that to city.
    '''
    def init(self, fileName): 
    
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }

        for line in graphFile:
            '''
            Gets the from city, the to city and the
            distances in appropriate variables
            '''
            (fromCity, toCity, distance) = line.split()
        

            '''
            Check if the first from city is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if fromCity not in self.adjacencyList:
                self.adjacencyList[fromCity] = [ ]

            '''
            Construct the tuples in the dictionary that match
            the from city with the list of to cities along with
            the distances to each of those to cities
            '''
            self.adjacencyList[fromCity].append((toCity, distance))
            
def permutate(values, distanceDict):
    # Variable that will hold the final result, the list of tuples
    results = []
    
    # If values is only one number, return that result
    if len(values) == 1:
        results.append(tuple(values))
        return results
    # List to be tuplified for the result
    workingLists = [[values[0]]]
    
    # For every number in values...
    for v in values[1:]:
        # Temporary list of lists that keeps track of our permutations
        tempList = []
        # for every list in workingLists, insert the current number
        # from values and add it to the permutations list
        for list in workingLists:
            list.insert(0, v)
            tempList.append(copy.deepcopy(list))
            # While the current number from values hasn't gone through the entire list, keep adding permutations
            while list.index(v) != (len(list)-1):
                itemLocation = list.index(v)
                temp = list[itemLocation+1]
                list[itemLocation+1] = v
                list[itemLocation] = temp
                tempList.append(copy.deepcopy(list))
        # Copy the list of permutations we created to the list we will tuplify
        workingLists = copy.deepcopy(tempList)
    # For every list in workingList, add the first element of the list and put them in results
    for resultList in workingLists:
        resultList.append(resultList[0])
        results.append(resultList)
    
    # Variable to report the best distance
    bestDistance = float("inf")
    # Variable to report the best route
    bestRoute = []
    # For all of the possible routes in results...
    for possibleRoute in results:
        # Calculates distance for each route
        distance = 0
        # For each city in the possible route...
        for i in range(len(possibleRoute)-1):
            # For each city in the adjacency list...
            for toCity in distanceDict[possibleRoute[i]]:
                # If it matches the next city in the route, save the distance
                if possibleRoute[i+1] == toCity[0]:
                    distance += int(toCity[1])
        # If the current route's distance is less than the best distance, set the best distance and route
        if distance < bestDistance:
            bestDistance = distance
            bestRoute = possibleRoute
    
    # Report of the best route with the best distance
    print "The best route is:", bestRoute
    print "With the best distance of:", bestDistance
    return results


if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print 'Usage python TSPProblem.py [input file]'
        quit()
        
    
    ga = TSPProblem()
    
    ga.init(sys.argv[1])
    
    result = permutate(list(ga.adjacencyList), ga.adjacencyList)
    '''
    don't forget the BFS algorithm!
    '''
