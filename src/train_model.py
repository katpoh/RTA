from sklearn import datasets

from src.perceptron import Perceptron


def train_model():
    iris_data = datasets.load_iris()
    model = Perceptron()
    model.fit(iris_data.data[:, :2], iris_data.target)

    return model
