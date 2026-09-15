# marks=[10,20,30,40,50,60,70,80,90,100,"kunal chaure",6.2]
# print(marks[9])
# print(len(marks))
# print(type(marks))

# now we are going to look towards list methods

# nos = [  1,4,4,55,666,4443,5,  2 ,  3]

# nos.append(4)
# print(nos)
# nos.insert(2,10)
# print(nos)
# # nos.sort()
# # print(nos)
# # nos.sort(reverse=True)
# # print(nos)
# nos.reverse()
# print(nos)


# linear search

        
        
nos = [1, 4, 4, 55, 666, 4443, 5, 2, 3]

index = 0

for num in nos:
    if num == 2:
        print(f"no found at index {index}")
    index += 1