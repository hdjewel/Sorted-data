#read file
#with      .....  as restaurant_ratings:
#no close is needed, because we are using the 'with' keyword
with open("scores.txt", 'r') as restaurant_ratings:  
    restaurant_rating_dict = {}
    for line in restaurant_ratings:
        aline = line.rstrip().split(':')
#populate a dictionary with restaurant names as keys with rating values
        restaurant_rating_dict[aline[0]] = aline[1]


#get keys from the dictionary
#sort keys decending
#restaurant_names = restaurant_rating_dict.keys()
    restaurant_names = sorted(restaurant_rating_dict.keys())

    #count = 0
    index = 0
    number_of_keys = len(restaurant_names)

    while True:
#get rating of the restaurant by its name
        restaurant_name = restaurant_names[index] 
        rating = restaurant_rating_dict[restaurant_name]

#print restaurant names and rating
        print "%s has a rating of %s." % (restaurant_name, rating)

#        print restaurant_name + " ==== " + rating
        index += 1
        
        if index == number_of_keys:
            break


"""the following code is for testing only
        count += 1


        if count > 3:
            break

"""
# on github there is a hint file


