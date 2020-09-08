l_ = ["bob", "Rolf", "Anne"]

t_ = ("bob", "Rolf", "Anne")

s_ = {"bob", "Rolf", "Anne"}

# TypeError: 'set' object is not subscriptable
# We can't extract set value becuase its not orderd
# print(s_[3])

l_.append("Smith")
print(l_)

l_.remove('bob')
print(l_)

# Set show only uniqe value
s_.add('Smith')
s_.add('Smith')

print(s_)
