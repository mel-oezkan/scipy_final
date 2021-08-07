import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def test_function():
    rand_img = np.random.uniform(size=(10,10))

    plt.imshow(rand_img)
    plt.title("Test Images")
    plt.show()

def show_samples(ds_path):
    """ given the name of one of the datasets plots 
    randomly selected images off it 
    """

    data = pd.read_csv(ds_path)

    