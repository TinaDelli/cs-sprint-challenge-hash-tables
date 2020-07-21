def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    #create a dictionary
    hash_table = {}
    #create the array of results
    result = []

    #add positive numbers to our hash table
    for num in a:
        if num >= 0:
            hash_table[num] = num 

    #check if our positive number in our hash table has a negative value
    for num in a:
        if num < 0 and -num in hash_table:
            result.append(-num)
    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
