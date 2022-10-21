minnum = 2000
maxnum = 3200
num_list = []
for x in range(minnum-1, maxnum+1):
    if x % 5 == 0 and x % 7 == 0:
        num_list.append(x)

print(num_list)


# /usr/bin/python3.10 /home/sask/Documents/edureka/edureka-python-scripting/mod3-cs1/mod3cs1-Q6.py
# [2030, 2065, 2100, 2135, 2170, 2205, 2240, 2275, 2310, 2345, 2380, 2415, 2450, 2485, 2520, 2555, 2590, 2625, 2660, 2695, 2730, 2765, 2800, 2835, 2870, 2905, 2940, 2975, 3010, 3045, 3080, 3115, 3150, 3185]
