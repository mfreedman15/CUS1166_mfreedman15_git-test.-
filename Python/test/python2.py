# Basic for loop
print("\nLoop using range(5)")
#range(5) : [0,1,2,3,4]
for i in range (0,10,2);
print(i)

#Using enumerate
#range(a,b,c) : from a to <b by step c
print("\nLoop Using enumerate + range ")
for i_idx, i_value in enumerate(range(2,10)):
    print(f"{i_idx} - {i_value}" )

    #Looping over a sequence
    print("\nLoop over a list")
    names = ["Chris", "Tom", "Paul"]
