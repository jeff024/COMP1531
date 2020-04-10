def inverse(d):
    '''
    Given a dictionary d, invert its structure such that values in d map to lists of keys in d. For example:
    >>> inverse({1: 'A', 2: 'B', 3: 'A'})
    {'A': [1, 3], 'B': [2]}
    '''
    key_list = list(d.keys())
    item_list = list(d.values())
    dic = {}
    for i in range(len(item_list)):
        item = item_list[0]
        if str(item) in dic.keys():
            dic[str(item)].append(key_list[item_list.index(item)])
        else:
            tmp = {}
            tmp[str(item)] = []
            tmp[str(item)].append(key_list[item_list.index(item)])
            dic.update(tmp)
        key_list.remove(key_list[item_list.index(item)])
        item_list.remove(item)
            
    return dic

if __name__ == "__main__":
    a = {1: 'A', 2: 'B', 3: 'A'}
    print(inverse(a))