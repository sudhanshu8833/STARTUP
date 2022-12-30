import numpy as np

def shift(arr, num, fill_value=np.nan):
    result = np.empty_like(arr)
    if num > 0:
        result[:num] = fill_value
        result[num:] = arr[:-num]
    elif num < 0:
        result[num:] = fill_value
        result[:num] = arr[-num:]
    else:
        result[:] = arr
    return result

# NP1 CROSSES OVER NP2
def crossover(np1,np2,no_of_candles=1):

    if isinstance(np1,int):
        np3=np1
    else:
        np3=shift(np1,no_of_candles,0)

    if isinstance(np2,int):
        np4=np1
    else:
        np4=shift(np2,no_of_candles,0)

    return np.where((np1>np2) &(np3<np4),True,False)
    


def crossunder(np1,np2,no_of_candles=1):
    np3=shift(np1,no_of_candles,0)
    np4=shift(np2,no_of_candles,0)

    return np.where((np1<np2) &(np3>np4),True,False)
    

