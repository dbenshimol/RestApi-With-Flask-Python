friends = {"Bob", "Rolf", "Anne"}
abroad = {"Bob", "Anne"}

local_friends = friends.difference(abroad)

print(local_friends)


# -- Union of two sets --

local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print(friends)


# -- Intersection of two sets --

art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)


set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}

inter = set1.intersection(set2)
print(inter)

my_tuple = (10)
my_tuple
