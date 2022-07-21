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

def get_winner(s, models):
    metric = s.values[0]
    values = [float(value.split()[0]) for value in s.values[1:]]
    
    if s.values[0].endswith('time'):
        return models[np.argmin(values)]
    else:
        return models[np.argmax(values)]
    
def save_object(obj, filename):
    with open(filename, 'wb') as outp:
        pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)