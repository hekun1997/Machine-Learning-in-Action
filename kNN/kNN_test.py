import kNN
from numpy import *
import operator


# get the K nearest neighbors.
# according to the distances.
def classify0(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = tile(in_x, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_distances_indicies = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_i_label = labels[sorted_distances_indicies[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1
    sort_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)
    return sort_class_count[0][0]


# get mat from file
def file2matrix(file_name):
    fr = open(file_name)
    array_o_lines = fr.readline()
    number_of_lines = len(array_o_lines)
    return_mat = zeros(number_of_lines, 3)
    class_labels_vector = []
    index = 0
    for line in array_o_lines:
        line = line.strip()
        list_from_line = line.split('\t')
        return_mat[index, :] = list_from_line[0:3]
        class_labels_vector.append(int(list_from_line[-1]))
        index += 1
    return return_mat, class_labels_vector


if __name__ == '__main__':
    group, labels = kNN.create_data_set()
    result = classify0([0, 0], group, labels, 3)
    print(result)
