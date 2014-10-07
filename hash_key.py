def new(num_buckets=256):
    """Initializes a Map with the given number of buckets."""
    aMap = []
    for i in range(0, num_buckets):
        aMap.append([])
    return aMap

def hash_key(aMap, key):
    """Given a key this will create a number and then convert it to
    an index for the aMap's buckets."""
    return hash(key) % len(aMap)

def get_bucket(aMap, key):
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key)
    return aMap[bucket_id]

def get_slot(aMap, key, default=None):
    """
    Returns the index, key, and value of a slot found in a bucket.
    Returns -1, key, and default (None if not set) when not found.
    """
    bucket = get_bucket(aMap, key)

    for i, kv in enumerate(bucket):
        k, v = kv
        if key == k:
            return i, k, v

    return -1, key, default

def get(aMap, key, default=None):
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default=default)
    return v

def set(aMap, key, value):
    """Sets the key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key)
    i, k, v = get_slot(aMap, key)

    if i >= 0:
        # the key exists, replace it
        bucket[i] = (key, value)
    else:
        # the key does not, append to create it
        bucket.append((key, value))

def delete(aMap, key):
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)

    for i in xrange(len(bucket)):
        k, v = bucket[i]
        if key == k:
            del bucket[i]
            break

def list(aMap):
    """Prints out what's in the Map."""
    for bucket in aMap:
        if bucket:
            for k, v in bucket:
                print k, v

# create a mapping of state to abbreviation
states = new()
set(states, 'Oregon', 'OR')
set(states, 'Florida', 'FL')
set(states, 'California', 'CA')
set(states, 'New York', 'NY')
set(states, 'Michigan', 'MI')

# create a basic set of states and some cities in them
cities = new()
set(cities, 'CA', 'San Francisco')
set(cities, 'MI', 'Detroit')
set(cities, 'FL', 'Jacksonville')

# add some more cities
set(cities, 'NY', 'New York')
set(cities, 'OR', 'Portland')


# print out some cities
print '-' * 10
print "NY State has: %s" % get(cities, 'NY')
print "OR State has: %s" % get(cities, 'OR')

# print some states
print '-' * 10
print "Michigan's abbreviation is: %s" % get(states, 'Michigan')
print "Florida's abbreviation is: %s" % get(states, 'Florida')

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: %s" % get(cities, get(states, 'Michigan'))
print "Florida has: %s" % get(cities, get(states, 'Florida'))

# print every state abbreviation
print '-' * 10
list(states)

# print every city in state
print '-' * 10
list(cities)

print '-' * 10
# by default ruby says "nil" when something isn't in there
state = get(states, 'Texas')

if not state:
  print "Sorry, no Texas."

# default values using ||= with the nil result
# can you do this on one line?
city = get(cities, 'TX', 'Does Not Exist')
print "The city for the state 'TX' is: %s" % city