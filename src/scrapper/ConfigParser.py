from src.scrapper.IdMaps import Mapper
import yaml


class Config:
    def __init__(self):
        self.base_url = "https://www.vinted.de/vetements?"

    def read_conf(self, config_path):
        with open(config_path, "a") as file:
            conf = yaml.load(file, Loader=yaml.FullLoader)

        return conf

    def create_conf(self, config_path) -> str:
        """ Given the different preferences the function maps those inputs into 
        their respective string notation and appends them to the url
        
        args = [
            {"gender": "femal", "category": shoes", "size": [36, 37], "color": ["red", "green"], "brand": ["nike", "addidas"]},
            {"gender": "male", "category": shoes", "size": [36, 37], "color": ["red", "green"], "brand": ["nike", "addidas"]},
            {"gender": "male", "category": pants", "size": ["M", "L"]}
            {"gender": "male", "category": rings", "size": ["M", "L"]}
        ]
        """

        args = self.read_conf(config_path)

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
                include multiple category just append them to the args"""

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
            # shoudl grab 

            size_type = self.main_category(arg["category"])

            if "size" in arg.keys():
                # print(arg["category"])
                size_conf = temp_conf["sizes"][size_type]

                for size in arg["size"]:
                    # check if value is a valid key for the dict
                    if size not in size_conf: 
                        raise ValueError(f"Argument {size} is not supported. Either change the sizes or contac the creators via github")

                    # add the respective url tokens based on the 
                    # given catergory
                    print(float(size))
                    arg_dict["sizes"].append(size_conf[float(size)])
            

            if "color" in arg.keys():
                color_conf = Mapper["colors"]
                for color in arg["color"]:
                    # add the respective url tokens based on the 
                    # given catergory
                    if color not in color_conf: 
                        raise ValueError(f"Argument {color} is not supported. Either change the sizes or contac the creators via github")
                        

                    color_token = color_conf[color]
                    arg_dict["colors"].append(color_token)

            if "brand" in arg.keys():
                brand_conf = Mapper["brands"]
                for brand in arg["brand"]:
                    # add the respective url tokens based on the 
                    # given catergory
                    if brand not in brand_conf: 
                        raise ValueError(f"Argument {brand} is not supported. Either change the sizes or contac the creators via github")
                        
                    brand_token = brand_conf[brand]
                    arg_dict["brands"].append(brand_token)

        # Using the dict mehtod to create the final url
        # allows for delteting multiples befor generation 
        for key in arg_dict.keys():
            for token in set(arg_dict[key]):
                url += str(token) + "&"

        return url, arg_dict


    def main_category(self, sub):
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