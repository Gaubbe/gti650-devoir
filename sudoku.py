import pennylane as qml
import pennylane.typing as qmlt
import numpy as np
import matplotlib.pyplot as plt

dev = qml.device("default.qubit", wires = 2)

@qml.qnode(dev)
def test_qnode():
    qml.PauliX(wires = 1)
    qml.Hadamard(wires=0)
    qml.Hadamard(wires=1)
    qml.CNOT(wires=range(2))

    return qml.state()

if __name__ == "__main__":
    state = test_qnode()
    state_data = {
        "Real": np.real(state),
        "Imaginary": np.imag(state)
    }
    bin_repr = [np.binary_repr(i, width=2) for i in range(2**2)]
    x = np.arange(len(bin_repr))

    width = 0.375
    fig, ax = plt.subplots()
    for i, (label, data) in enumerate(state_data.items()):
        offset = width * i
        ax.bar(x + offset, data, width, label=label)

    ax.set_xticks(x + width / 2, bin_repr)
    ax.legend(loc='upper left', ncols=2)

    plt.show()
