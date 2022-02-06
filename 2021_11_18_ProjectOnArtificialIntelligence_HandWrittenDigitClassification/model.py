
from sklearn import datasets
digits = datasets.load_digits()

# Import Math
import math

# Import datasets and classifiers
from sklearn import datasets, svm

# Import pickle
import pickle

# Load the digits dataset
digits = datasets.load_digits()

# To apply a classifier on this data, we need to flatten the image, to
# turn the data in a (samples, feature) matrix:
n_samples = len(digits.images)
nh_samples = int(math.ceil(n_samples / 3) * 2)
data = digits.images.reshape(n_samples, -1)

# Create a classifier: a support vector classifier
classifier = svm.SVC(gamma=0.001)

# We learn the digits on the first half of the digits
classifier.fit(data[:nh_samples], digits.target[:nh_samples])

# Save model to disk
pickle.dump(classifier, open('model.pkl', 'wb'))