from NeuralNetwork import NeuralNetwork
if __name__ == '__main__':
    nn = NeuralNetwork()
    nn.fit_network()
    model = nn.load_model()
