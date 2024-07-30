# # def cube(x):
# #     x**3
# # or
# # cube=lambda x: x**3 # For using line 7
# l=[1,2,3,4,6]
# #Can aslo do mapping like this
# # newl=list(map(cube,l))
# newl=list(map(lambda l: l**3 ,l))
# # newl=[]
# # for i in l:
# #     print(cube(i))
# #     newl.append(cube(i))
# # print(l)
# print(newl)
# filter_func=lambda a: a>2
# n_newl= list(filter(filter_func, l))
# print(n_newl)


from functools import reduce
nums=[1,2,3,4,5 ]

sum=reduce(lambda x,y: x+y , nums)
print(sum)