import numpy as np


class NeuralNetwork:
    def __init__(self):
        np.random.seed(27)
        self.synaptic_weights = 2 * np.random.random((3, 1)) - 1

    def __sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def __sigmoid_derivative(self, sigm):
        return sigm * (1 - sigm)

    def train(self, input_set, output_set, iterations):
        for iteration in range(iterations):
            prediction = self.predict(input_set)
            error = output_set - prediction
            # Gradient descent
            adjustment = np.dot(input_set.T, error * self.__sigmoid_derivative(prediction))
            self.synaptic_weights += adjustment

    def predict(self, inputs):
        return self.__sigmoid(np.dot(inputs, self.synaptic_weights))


if __name__ == '__main__':
    neural_network = NeuralNetwork()

    print('Random synaptic wieghts: ')
    print(neural_network.synaptic_weights)

    training_set_inputs = np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = np.array([[0, 1, 1, 0]]).T

    neural_network.train(training_set_inputs, training_set_outputs, 10000)
    print('Trained synaptic weights: ')
    print(neural_network.synaptic_weights)

    print('Predicting new case [1, 0, 0]: ')
    new_case = np.array([[1, 0, 0]])
    print(neural_network.predict(new_case))
