import numpy as np 

def concatenate(*args):
    final_dict = {key: [] for key in args[0].keys()}
    for dictionary in args:
        for key, value in dictionary.items():
            final_dict[key].extend(value)
    return final_dict

def highlight_max(s, props=''):
    values = [float(value.split()[0]) for value in s.values[1:]]
    result = [''] * len(s.values)
    if s.values[0].endswith('time'):
        result[np.argmin(values)+1] = props
    else:
        result[np.argmax(values)+1] = props
    return result
