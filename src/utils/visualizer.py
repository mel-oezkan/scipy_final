import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from src.scrapper.WebScrapper import Scrapper

def test_function():
    rand_img = np.random.uniform(size=(10,10))

    plt.imshow(rand_img)
    plt.title("Test Images")
    plt.show()

def show_samples(path="data/full_data.csv"):

    # read the data
    data = pd.read_csv(path, names=["user", "likes", "size", "brand", "price", "art-link", "user-link"])
    scrapper = Scrapper(silent=True)
    
    # create 4 random indices to plot from
    random_vals = []
    
    plt.figure(figsize=(12,10))
    for n in range(4):

        # Within the dataset there can be some articles for
        # which the page is deleted since they are sold so
        # we will search for entries which still work
        
        finished = True
        while finished:
            rand_index = np.random.randint(0, len(data))
            
            row_dict = data.iloc[rand_index]
            # using sample will only yield the first image instead of all 
            # images on the article page
            image = scrapper.article_images(row_dict["art-link"], sample=True)
            
            if image and rand_index not in random_vals:
                finished = False

        
        plt.subplot(1,4,n+1)
        plt.imshow(image[0])
        plt.axis("off")
        plt.title(f"size: {row_dict['size']}\nbrand: {row_dict['brand']}\nprice: {row_dict['price']}")


        random_vals.append(rand_index)
    
    plt.tight_layout()
    plt.show()    