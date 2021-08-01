# Scientific Python Final Project

## Short description
<<<<<<< HEAD
This project will contain an interactive **web scrapper** with an **user intafece** based on the browser where the use will be able to filter their search and **annotate** the scrapped data. However the scrapper will only work on the webstore of Vinted.com.
=======
This project will contain an interactive **web scrapper** with an **user intafece** created in the browser where the use will be able to filter their search and **annotate** the scrapped data
>>>>>>> de7c702456f72be9ec09d4d697f5d313d92c3b87

## Requirements
For the scrapper to run 

Install python requirements using pip:  
```pip install -r requirements.txt```  

Create conda env using:  
```conda env create -f environment.yml ```

## File structure
- data
    - contains the generated csv files with information about the seller, price, color, clothing type
- scripts
    - to eas the handling of the multiple modules we created seperate scripts file for each of the module which are called by using the respective argument when running the main file
- src
    - the code modules for the different functionalities

├── data     
│   └── run0.csv  
│   └── run1.csv  
├── scripts  
│   └── annotator.py  
│   └── scrapper.py  
│   └── trainer.py  

## Functionalities

### Scrapper
given the arguments the scrapper will generate a scv file containing the values specified in the articles while a second hdf5 file containing the image values will be generated to
