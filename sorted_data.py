#read file
#with      .....  as restaurant_ratings:
#no close is needed, because we are using the 'with' keyword
with open("scores.txt", 'r') as restaurant_ratings:  
    restaurant_rating_dict = {}
    for line in restaurant_ratings:
        aline = line.rstrip().split(':')
#populate a dictionary with restaurant names as keys with rating values

# changed order of retreiving the input
        restaurant_rating_dict[aline[1]] = aline[0]


#get keys from the dictionary
#sort keys decending
    #try again?.items can't be used on dict.
    #sorted_restaurants = sorted(restaurant_rating_dict.items(), key = restaurant_rating_dict[0].itemgetter(1), reverse = True)
    sort_choice = raw_input("How would you like the restaurant guide to be sorted? By rating or by name?\n>").lower()
    
    if ( sort_choice[0] != "r" and sort_choice[0] != "n"):
        print "you didn't enter name or rating"
    else:
        restaurant_names = sorted(restaurant_rating_dict, reverse = True)

        index = 0
        number_of_keys = len(restaurant_names)

        while True:
#get rating of the restaurant by its name
            restaurant_name = restaurant_names[index] 
            rating = restaurant_rating_dict[restaurant_name]

# changing the order of printing the values
            print "%s has a rating of %s." % (restaurant_name, rating)

            index += 1

            if index == number_of_keys:
                break


# on github there is a hint file


