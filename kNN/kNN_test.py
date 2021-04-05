import kNN
import matplotlib.pyplot as plt
from numpy import *
import operator


def classify_test():
    group, labels = kNN.create_data_set()
    result = kNN.classify0([0, 0], group, labels, 3)
    return result


def read_file_test(file_name = 'datingTestSet2.txt'):
    dating_data_mat, dating_labels = kNN.file2matrix(file_name)
    return dating_data_mat, dating_labels


def matplotlib_with_dating_data_test():
    dating_data_mat, dating_labels = read_file_test('datingTestSet2.txt')
    # below code report error on python 3.8, plt.figure() object has no attribute 'plot'.
    # fig = plt.figure()
    # ax = fig.add_plot(111)
    ax = plt.axes()
    ax.scatter(dating_data_mat[:, 1], dating_data_mat[:, 2], 15.0 * array(dating_labels), 15.0 * array(dating_labels))
    plt.show()


if __name__ == '__main__':
    # 1 classify_test()
    # print(read_file_test('datingTestSet2.txt'))
    # 2 matplotlib_with_dating_data_test()
    dating_data_mat, dating_labels = read_file_test()
    norm_data_set, ranges, min_value = kNN.auto_norm(dating_data_mat)
    print(norm_data_set)
    pass
