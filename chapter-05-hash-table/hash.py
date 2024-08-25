new_hash = dict()
# Another way of creating a dictionary -> new_hash = {}

new_hash["one"] = 1
new_hash["two"] = 2
new_hash["three"] = 3



print(new_hash)
print(new_hash.values())
print(new_hash["three"])
print(new_hash.get("hnhn") == None) # If the value is not in the hash table .get returns None (falsy)


# Simple usa case = Voting 
voters = {}
def vote(name):
    if voters.get(name):
        print("You already vote")
    else: 
        print("Let him voted")
        voters[name] = True

vote("Miki")
vote("Miki")