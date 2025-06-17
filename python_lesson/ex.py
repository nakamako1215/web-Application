scores = {'Ken': 88, 'Mio': 76, 'Taro': 93, 'Yui': 85}

for key,value in scores.items():
    scores_sorted = sorted(scores.items(), key = lambda x:x[1] )

print(scores_sorted)