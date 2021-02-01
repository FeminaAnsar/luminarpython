expenses={"jan":30000,"feb":25000,"march":28000,"april":25000,"may":22000}
print(expenses["march"])
#value stored as key value pair
#key must be unique
#check for a key value
print("june" in expenses)

#adding new key value pairs
#june:25000
expenses["june"]=25000
print(expenses)

print("march" in expenses)
expenses["march"]-=3000
print(expenses)

