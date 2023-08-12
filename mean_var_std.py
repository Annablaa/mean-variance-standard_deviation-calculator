import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers." )
    else:
       matrix = np.array(list).reshape(3,3)

       column_means = np.mean(matrix,axis=0)
       row_means = np.mean(matrix,axis=1)
       flattened_means = float(np.mean(list))

       column_variance = np.var(matrix,axis=0)
       row_variances = np.var(matrix, axis=1)
       variance = float(np.var(list))

       column_std = np.std(matrix,axis=0)
       row_std = np.std(matrix,axis=1)
       std = float(np.std(list))

       max_column = np.max(matrix,axis=0)
       max_row = np.max(matrix,axis=1)
       max_flattened = np.max(list)

       min_column = np.min(matrix,axis=0)
       min_row = np.min(matrix, axis=1)
       min_flattened = np.min(list)

       sum_column = np.sum(matrix,axis=0)
       sum_row = np.sum(matrix,axis=1)
       sum_flattened = np.sum(list)

       calculations = {
            'mean': [column_means.tolist(), row_means.tolist(), flattened_means],
            'variance': [column_variance.tolist(), row_variances.tolist(), variance],
            'standard deviation': [column_std.tolist(), row_std.tolist(), std],
            'max': [max_column.tolist(), max_row.tolist(), max_flattened],
            'min': [min_column.tolist(), min_row.tolist(), min_flattened],
            'sum': [sum_column.tolist(), sum_row.tolist(), sum_flattened]
        }

    return calculations
# print(calculate([0,1,2,3,4,5,6,7,8]))


print(calculate([9,1,5,3,3,3,2,9,0]))