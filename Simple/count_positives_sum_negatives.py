def count_postives_sum_negatives(arr):
    import numpy as np
    arr1 = np.array(arr)
    pos_arr = arr1[arr1>0]
    neg_arr = arr1[arr1<0]
    
    if len(pos_arr) !=0 or sum(neg_arr) !=0:
        return [len(pos_arr),sum(neg_arr)]
    
    
    else:
        return []
    
def count_positives_sum_negatives_1(arr):
    import numpy as np
    # check if the input is an empty array or null
    if not arr:
        return []
    # create a numpy array from the input
    arr = np.array(arr)
    # count the number of positive values
    positive_count = np.sum(arr > 0)
    # sum the negative values
    negative_sum = np.sum(arr[arr < 0])
    # return the result as a list
    return [positive_count, negative_sum]

def count_positives_sum_negatives_2(arr):
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []