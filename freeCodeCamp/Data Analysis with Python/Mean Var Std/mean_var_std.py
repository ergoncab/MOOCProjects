import numpy as np

def calculate(list):
    if len(list) < 9:
         raise ValueError('List must contain nine numbers.')
        

    array = np.array(list)

    array_rs = np.reshape(array, (3, 3))

    means = [array_rs.mean(axis = 0).tolist(), array_rs.mean(axis = 1).tolist(), array.mean().tolist()]
    variances = [array_rs.var(axis = 0).tolist(), array_rs.var(axis = 1).tolist(), array.var().tolist()]
    stds = [array_rs.std(axis = 0).tolist(), array_rs.std(axis = 1).tolist(), array.std().tolist()]
    maxs = [array_rs.max(axis = 0).tolist(), array_rs.max(axis = 1).tolist(), array.max().tolist()]
    mins = [array_rs.min(axis = 0).tolist(), array_rs.min(axis = 1).tolist(), array.min().tolist()]
    sums = [array_rs.sum(axis = 0).tolist(), array_rs.sum(axis = 1).tolist(), array.sum().tolist()]

    calculations = {'mean': means, 'variance': variances, 'standard deviation': stds, 'max': maxs, 'min': mins, 'sum': sums}

    return calculations