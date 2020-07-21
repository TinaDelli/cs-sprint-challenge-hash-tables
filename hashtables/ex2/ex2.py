#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    #create a dictionary
    hash_table = {}
    #create array with None
    route = [None] * length
    #create key value pair
    #iterate through array
    for i in range(length):
        #add the destinations into our hash table 
        hash_table[tickets[i].source] = tickets[i].destination 
        #if the current ticket index has a source of None
        if tickets[i].source == "NONE" and route[0] == None:
            route[0] = tickets[i].destination #this will be our first flight

    # now we can check the value of the starting location and go from there to construct the entire route 
    
    #iterate through array
    for ticket in range(length):
        #if the ticket isn't the first and the last index is not none
        if ticket > 0 and route[ticket - 1] is not None:
            #set the destination to the ticket
            route[ticket] = hash_table[route[ticket - 1]]


    return route
