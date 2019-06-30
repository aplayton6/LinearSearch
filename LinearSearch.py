def linear_search(alist, key):
    """Return index of key in alist. Return -1 if key not present."""
    for i in range(len(alist)):
        if alist[i] == key:
            return i
    return -1


userList = input('Enter the list of numbers: ')
userList = userList.split()
userList = [int(x) for x in alist]
key = int(input('The number to search for: '))

index = linear_search(userList, key)
if index < 0:
    print('{} was not found.'.format(key))
else:
    print('{} was found at index {}.'.format(key, index))
