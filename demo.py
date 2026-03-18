import matplotlib.pyplot as plt
import datasets
import utils

def analyse(x, y):
    plt.scatter(x, y)

    correlacao = utils.correlacao(x, y)
    bone, bzero = utils.regressao(x, y)
    predicted_ys = []
    for i in range(len(x)):
        predicted_y = bzero + (bone * x[i])
        predicted_ys.append(predicted_y)

    plt.plot(x, predicted_ys)
    plt.title(f"Correlação {correlacao:.2f}, Regressão B1: {bone:.2f}, B0: {bzero:.2f}")
    plt.show()


analyse(datasets.x1, datasets.y1)
analyse(datasets.x2, datasets.y2)
analyse(datasets.x3, datasets.y3)
analyse(datasets.x4, datasets.y4)