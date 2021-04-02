import kNN.kNN as knn
from numpy import *
import operator


def classify0(in_x, data_set, labels, k):
    data_set_size = data_set.shape[0]
    diff_mat = tile(in_x, (data_set, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis=1)
    distances = sq_distances ** 0.5
    sorted_distances_indicies = distances.argsort()
    class_count = {}
    for i in range(k):
        vote_i_label = labels[sorted_distances_indicies[i]]
        class_count[vote_i_label] = class_count.get(vote_i_label, 0) + 1
    sort_class_count = sorted(class_count.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sort_class_count[0][0]


if __name__ == '__main__':
    pass
