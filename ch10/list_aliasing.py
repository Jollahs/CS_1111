alist = [4, 2, 8, 6, 5]
blist = alist     # is b copying a? Or pointing to the same object
blist[3] = 999    # does this also modify the list pointed to by a?
print(alist)


list1=[1,100,1000]
list2=[1,100,1000]
list3=list1

print(list1 == list2)  # do they have the same value?
print(list1 is list2)  # do they point to the same object?
print(list1 is list3)
print(list2 is not list3)  # do they point to different objects?
print(list2 != list3)    # do they have different values?
