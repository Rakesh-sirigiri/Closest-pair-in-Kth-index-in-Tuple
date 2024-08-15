test_list = [(3,4), (78,76), (3,4), (9,8), (19,23)]
tup = (17,23)
K = 1
res = min(test_list, key=lambda x: abs(x[K-1] - tup[K-1]))
print("The nearest tuple to K th index element is :" + str(res))
