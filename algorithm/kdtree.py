import numpy as np


class Node(namedtuple('Node', 'left_child right_child node_feature node_label axis')):
    def __repr__(self):
        pformat(tuple(self))


def kdtree(data, labels, depth=0):
    assert(data.shape[0]==labels.shape[0])
    k = data.shape[1]
    axis = depth % k

    if data.shape[0] < 1:
        return None
    elif data.shape[0] == 1:
        return Node(left_child=None, right_child=None,
                    node_feature=data[0], node_label=labels[0],
                    axis=axis)

    sorted_idx = data[:, axis].argsort()
    sorted_data = data[sorted_idx]
    sorted_labels = labels[sorted_idx]
    median = data.shape[0]//2

    return Node(left_child=kdtree(sorted_data[:median], sorted_labels[:median], depth+1),
                right_child=kdtree(sorted_data[median+1:], sorted_labels[median+1:], depth+1),
                node_feature=sorted_data[median], node_label=sorted_labels[median], axis=axis)


def construct_kdtree(data, labels):
    data = np.atleast_2d(data)
    assert(data.shape[0] == labels.shape[0])
    return kdtree(data, labels)


def get_distance(a, b):
    return np.linalg.norm(a-b)


def nn_search(test_point, node, best_point, best_dist, best_label):
    if node is not None:
        cur_dist = get_distance(test_point, node.node_feature)
        if cur_dist < best_dist:
            best_dist = cur_dist
            best_point = node.node_feature
            best_label = node.node_label

        axis = node.axis
        search_left = False
        if test_point[axis] < node.node_feature[axis]:
            search_left = True
            best_point, best_dist, best_label = nn_search(test_point, node.left_child,
                                                          best_point, best_dist, best_label)
        else:
            best_point, best_dist, best_label = nn_search(test_point, node.right_child,
                                                          best_point, best_dist, best_label)

        if np.abs(node.node_feature[axis] - test_point[axis]) < best_dist:
            if search_left:
                best_point, best_dist, best_label = nn_search(test_point, node.right_child,
                                                  best_point, best_dist, best_label)
            else:
                best_point, best_dist, best_label = nn_search(test_point, node.left_child,
                                                  best_point, best_dist, best_label)

    return best_point, best_dist, best_label


def nn(test_point, tree):
    best_point, best_dist, best_label = nn_search(test_point, tree, None, np.inf, None)
    return best_label


class BPQ:
    def __init__(self, length=5, hold_max=False):
        self.data = []
        self.length = length
        self.hold_max = hold_max

    def append(self, point, distance, label):
        self.data.append((point, distance, label))
        self.data.sort(key=itemgetter(1), reverse=self.hold_max)
        self.data = self.data[:self.length]

    def get_data(self):
        return [item[0] for item in self.data]

    def get_label(self):
        labels = [item[2] for item in self.data]
        uniques, counts = np.unique(labels, return_counts=True)
        return uniques[np.argmax(counts)]

    def get_threshold(self):
        return np.inf if len(self.data) == 0 else self.data[-1][1]

    def full(self):
        return len(self.data) >= self.length


def knn_search(test_point, node, queue):
    if node is not None:
        cur_dist = get_distance(test_point, node.node_feature)
        if cur_dist < queue.get_threshold():
            queue.append(node.node_feature, cur_dist, node.node_label)

        axis = node.axis
        search_left = False
        if test_point[axis] < node.node_feature[axis]:
            search_left = True
            queue = knn_search(test_point, node.left_child, queue)
        else:
            queue = knn_search(test_point, node.right_child, queue)

        if not queue.full() or np.abs(node.node_feature[axis] - test_point[axis]) < queue.get_threshold():
            if search_left:
                queue = knn_search(test_point, node.right_child, queue)
            else:
                queue = knn_search(test_point, node.left_child, queue)

    return queue


def knn(test_point, tree, k):
    queue = BPQ(k)
    queue = knn_search(test_point, tree, queue)
    return queue.get_label()
