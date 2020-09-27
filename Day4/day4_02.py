a = [x for x in range(2, int(input("단: "))+1)]

for i in range(1, 10):
    for n in a:
        print("%d x %d = %3d" % (n, i, n*i), end=" | ")
    print("")


'''for i in range(1, 10):
    for n in range(2, 10):
        print("%d x %d = %2d" % (n, i, n*i), end=" | ")
   print("")
'''
