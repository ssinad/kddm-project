import hdbscan
import numpy as np
from sklearn.preprocessing import scale
from sklearn import metrics

if __name__ == "__main__":

    NUM_CLASSES = 4199

    matrix = np.genfromtxt("../Matrix.csv", delimiter=',')
    tr = np.transpose(matrix)
    X_scaled = scale(tr, axis=1)
    y_true = np.asarray(list(range(NUM_CLASSES)) * 15)

    SAMPLE = NUM_CLASSES
    picking_ind = [class_num + i * NUM_CLASSES for class_num in range(SAMPLE) for i in range(15)]
    X_sampled = X_scaled[picking_ind, :]
    y_sampled = y_true[picking_ind]
    
    for cl_size in range(2, 15 + 1):
        for min_samples in range(1, 15 + 1):
            clusterer = hdbscan.HDBSCAN(min_cluster_size=cl_size, min_samples=min_samples)
            clusterer.fit(X_sampled)
            # print('HDBScan-------------------------------->')
            # print("Number of clusters is", clusterer.labels_.max() + 1)
            print('{},{},{},{},{},{}\n'.format(cl_size, min_samples, clusterer.labels_.max() + 1,  metrics.jaccard_similarity_score(y_sampled, clusterer.labels_), metrics.adjusted_rand_score(y_sampled, clusterer.labels_), np.count_nonzero(clusterer.labels_ == -1) / SAMPLE / 15.0 * 100.0), end='')
    np.save("HDBScan.npy", clusterer.labels_)
    # print("Jaccard Index for HDBScan is ", metrics.jaccard_similarity_score(y_sampled, clusterer.labels_))
    # print("Rand Index for HDBScan is", metrics.adjusted_rand_score(y_sampled, clusterer.labels_))
    # print("Silhouette score is", metrics.silhouette_score(X_sampled, clusterer.labels_))
    # print("Percent of noise is ", np.count_nonzero(clusterer.labels_ == -1)/ SAMPLE / 15.0 * 100.0)
