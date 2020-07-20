def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    #create a dictionary
    hash_table = {}

    #iterate through our array
    for i in range(length):
        #create the value needed to equal the weight limit
        difference = limit - weights[i]
        #check if a key with the difference exists
        if difference in hash_table:
            #if it exists return the matching items in a tuple
            return (i, hash_table[difference])
        else:
            #if not, add it to our hash table, with value of index
            hash_table[weights[i]] = i
    #if the pair doesnt exist return None        
    return None
