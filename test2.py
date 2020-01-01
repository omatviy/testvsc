import numpy as np


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# print(sigmoid([1,2]))


training_inputs = np.array([[0, 0, 1],
                            [1, 1, 1],
                            [1, 0, 1],
                            [0, 1, 1]])

training_outputs = np.array([[0, 1, 1, 0]]).T

np.random.seed(1)

synaptic_weights = 2 * np.random.random((3, 1)) - 1

print("Веса после иниц")
print(synaptic_weights)

print("Обучение:")
for i in range(20000):
    #    if i == 20000-1:
    input_layer = training_inputs
#        print("Inf:")
#        print(np.dot(input_layer,synaptic_weights))
    outputs = sigmoid(np.dot(input_layer, synaptic_weights))

    err = training_outputs - outputs
#        print("training_outputs:")
#       print(training_outputs)

#        print("outputs:")
#        print(outputs)

#        print("Error:")
#        print(err)
    if i == 20000-1:
        print("Test")
        print(outputs)
        print(outputs * (1 - outputs))
    adjustments = np.dot(input_layer.T, err * (outputs * (1 - outputs)))

    synaptic_weights += adjustments

print("Веса:")
print(synaptic_weights)

print("Результат:")
print(outputs)

print("Тест:")
new_inputs = np.array([1, 1, 0])
output = sigmoid(np.dot(new_inputs, synaptic_weights))

print(output)
