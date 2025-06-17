def dist_update(di,key,value):
    if key in di.keys():
        di["d"] = 4
        return di
    if not key in di.keys():
        di[key] = value
        return di
    
print(dist_update({'a': 1, 'b': 2, 'c': 3},'d',20))
print(dist_update({'a': 1, 'b': 2, 'c': 3},'z',20))