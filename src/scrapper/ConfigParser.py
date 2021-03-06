from src.scrapper.IdMaps import Mapper
import yaml


class Config:
    def __init__(self):
        self.base_url = "https://www.vinted.de/vetements?"

    def read_conf(self, config_path:str):
        """ Simple function to read a yaml file

        :params config_path: path to the config file
        """
        
        with open(config_path, "r") as file:
            conf = yaml.load(file, Loader=yaml.FullLoader)

        return conf

    def create_conf(self, config_path:str) -> str:
        """ Given the different preferences the function maps those inputs into 
        their respective string notation and appends them to the url
        
        args = [
            {"gender": "femal", "category": shoes", "size": [36, 37], "color": ["red", "green"], "brand": ["nike", "addidas"]},
            {"gender": "male", "category": shoes", "size": [36, 37], "color": ["red", "green"], "brand": ["nike", "addidas"]},
            {"gender": "male", "category": pants", "size": ["M", "L"]}
            {"gender": "male", "category": rings", "size": ["M", "L"]}
        ]

        :params config_path: path to the config file

        :returns base url combined with config tokens
        """

        args = self.read_conf(config_path)
        self.config = args

        # class will contain value
        url = self.base_url

        arg_dict = {
            "sizes": [],
            "colors": [],
            "brands": [],
            "categories": [],
        }

        for arg in args:
            temp_conf = Mapper[arg["gender"]]

            # check for category
            assert isinstance(arg["category"], str), """Only accepts single category types, to 
                include multiple categories just append them to the args"""

            # Handling of cases in which args are empty
            conf_categories = temp_conf["category"]
            # print(conf)
            if "category" in arg.keys():
                category = conf_categories[arg["category"]]
                arg_dict["categories"].append(category)        
            else:
                # take the category for all
                category = conf_categories["all"]
                arg_dict["categories"].append(category)


            # since some categories share the same sizes we 
            # need a way of looking up which sizes the config 
            # should grab 

            size_type = self.main_category(arg["category"])

            if "size" in arg.keys():
                # print(arg["category"])
                size_conf = temp_conf["sizes"][size_type]
                #print(temp_conf["sizes"])

                for size in arg["size"]:

                    if isinstance(size, int):
                        size = float(size)

                    # check if value is a valid key for the dict
                    if size not in size_conf: 
                        raise ValueError(f"Argument {size} is not supported. Either change the sizes or contact the creators via github")

                    # add the respective url tokens based on the 
                    # given catergory
                    arg_dict["sizes"].append(size_conf[size])
            

            if "color" in arg.keys():
                color_conf = Mapper["colors"]
                for color in arg["color"]:
                    # add the respective url tokens based on the 
                    # given catergory
                    if color not in color_conf: 
                        raise ValueError(f"Argument {color} is not supported. Either change the sizes or contact the creators via github")
                        

                    color_token = color_conf[color]
                    arg_dict["colors"].append(color_token)

            if "brand" in arg.keys():
                brand_conf = Mapper["brands"]
                for brand in arg["brand"]:
                    # add the respective url tokens based on the 
                    # given catergory
                    if brand not in brand_conf: 
                        raise ValueError(f"Argument {brand} is not supported. Either change the sizes or contact the creators via github")
                        
                    brand_token = brand_conf[brand]
                    arg_dict["brands"].append(brand_token)

        # Using the dict method to create the final url
        # allows for deleting multiples befor generation 
        for key in arg_dict.keys():
            for token in set(arg_dict[key]):
                url += str(token) + "&"

        return url, arg_dict


    def main_category(self, sub:str) -> str:
        """ Function to look up what kind of size to use
        given the category of the search

        :params sub: short for sub category 
            (e.g. stiefel would be mapped to shoes) 
        
        :returns string of main category
        """

        size_lookup = Mapper["helper"]

        size_type = None
        for key in size_lookup.keys():
            if sub in size_lookup[key]:
                size_type = key

        if size_type:
            return size_type

        raise NotImplementedError("""Sadly the selected category 
            does not match any predefined size category. Either 
            create an github issue or try a more general search term.""")