
# Category: CLOTHES
clothes_f = {
    "XXS": "size_id[]=102",
    "XS": "size_id[]=2",
    "S": "size_id[]=3",
    "M": "size_id[]=4",
    "L": "size_id[]=5",
    "XL": "size_id[]=6",
    "XXL": "size_id[]=7",

    32: "size_id[]=102",
    34: "size_id[]=2",
    36: "size_id[]=3",
    38: "size_id[]=4",
    40: "size_id[]=5",
    42: "size_id[]=6",
    44: "size_id[]=7",

    4: "size_id[]=102",
    6: "size_id[]=2",
    8: "size_id[]=3",
    10: "size_id[]=4",
    12: "size_id[]=5",
    14: "size_id[]=6",
    16: "size_id[]=7",
}

clothes_m = {
    "XS": "size_id[]=206",
    "S": "size_id[]=207",
    "M": "size_id[]=208",
    "L": "size_id[]=209",
    "XL": "size_id[]=210",
    "XXL": "size_id[]=211",    
}

# Category: SHOES
shoes_f = {
    35.0:"size_id[]=55",
    35.5:"size_id[]=1195",
    36.0:"size_id[]=56",
    36.5:"size_id[]=1196",
    37.0:"size_id[]=57",
    37.5:"size_id[]=1197",
    38.0:"size_id[]=58",
    38.5:"size_id[]=1198",
    39.0:"size_id[]=59",
    39.5:"size_id[]=1199",
    40.0:"size_id[]=60",
    40.5:"size_id[]=1200",
    41.0:"size_id[]=61",
    41.5:"size_id[]=1201",
    42.0:"size_id[]=62",
    43.0:"size_id[]=63"
}

shoes_m = {
    38.0:"size_id[]=776",
    39.0:"size_id[]=778",
    40.0:"size_id[]=780",
    41.0:"size_id[]=782",
    42.0:"size_id[]=784",
    42.5:"size_id[]=785",
    43.0:"size_id[]=787",
    43.5:"size_id[]=788",
    44.0:"size_id[]=790",
    44.5:"size_id[]=791",
    45.0:"size_id[]=792",
    46.0:"size_id[]=793",
    47.0:"size_id[]=794"
}

# Category: CLOTHES

# Category: RINGS
ring_sizes = {
    14.1: "size_id[]=1202",
    14.5: "size_id[]=1203",
    14.9: "size_id[]=1204",
    15.3: "size_id[]=1205",
    15.7: "size_id[]=1206",
    16.1: "size_id[]=1207",
    16.5: "size_id[]=1208",
    16.9: "size_id[]=1209",
    17.3: "size_id[]=12010",
    17.7: "size_id[]=12011",
    # ...
}

# Category: CATEGORY
size_category_map = {

    "shoes": [
        "stiefel", "oxfords", "slippers",
        "elegante schuhe", "sportschuhe",
        "sandalen"],

    "clothes": [
        "mäntel", "jacken", "hemden",
        "pullis", "t-shirts", "westen",
        "hosen", "jeans", "shorts",
        "sport_hose", "sport_pulli", 
        "sport_shorts", "trainingsanzüge",
        "gürtel", "sonnenbrillen"],

    "rings": ["ringe"]
}


# only all 
male_catergories = {
    "jeans": "catalog[]=257",
    "jacken": "catalog[]=2052",
    "mäntel": "catalog[]=2051",
    "hemden": "catalog[]=536",
    "t-Shirts": "catalog[]=77",
    "anzughosen": "catalog[]=1787",
    "sweater": "catalog[]=1811",
    "pullis": "catalog[]=267",
    "hoodies": "catalog[]=267",
    "kapuzenjacken": "catalog[]=1812",
    "rollkragenpullover": "catalog[]=265",
    "lange pullover": "catalog[]=1814",
    "flipflops": "catalog[]=1237",
    "turnschuhe": "catalog[]=1242",
    "sportschuhe": "catalog[]=1452",
    "stiefel": "catalog[]=1233", 
} 

female_catergories = {
    "stiefel": "catalog[]=211",
    "gummistiefel": "catalog[]=2135",
    "cowboystiefel": "catalog[]=54",
    "boots": "catalog[]=1049",
    "absatzschuhe": "catalog[]=543",
    "flache schuhe": "catalog[]=1050",
    "ballerinas": "catalog[]=548",
    "stiefelette": "catalog[]=210",
    "turnschuhe": "catalog[]=1916",
    "sandalen": "catalog[]=207",
    "flip-flops": "catalog[]=546",
    "sonnenbrillen": "catalog[]=26",
    "ringe": "catalog[]=553",
    "ketten": "catalog[]=164",
    "ohrringe": "catalog[]=163",
} 

male_sizes = {
    "clothes": None,
    "shoes": shoes_m,
    "rings": ring_sizes
}

female_sizes = {
    "clothes": 12,
    "shoes": shoes_f,
    "rings": ring_sizes,
}

brands = {
    "nike":'brand_id[]=53',
    "zara": 'brand_id[]=12',
    "addidas": 'brand_id[]=14',
    "levis": 'brand_id[]=10',
    "h&m": 'brand_id[]=7',
    "ralph lauren": 'brand_id[]=88',
    "mango": 'brand_id[]=15',
    "tommy hilfiger": 'brand_id[]=94',
    "lacoste": 'brand_id[]=304',
    "calvin klein": 'brand_id[]=255',
    "guess": 'brand_id[]=20',
    "michael kors": 'brand_id[]=6005'
}

colors = {
    "schwarz": 'color_id[]=1',
    "grau": 'color_id[]=3',
    "weiß": 'color_id[]=12',
    "creme": 'color_id[]=20',
    "beige": 'color_id[]=4',
    "aprikose": 'color_id[]=21',
    "orange": 'color_id[]=11',
    "korallenrot": 'color_id[]=22',
    "rot": 'color_id[]=7',
    "burgunderrot": 'color_id[]=23',
    "pink": 'color_id[]=5',
    "rose": 'color_id[]=24',
    "lila": 'color_id[]=6',
    "flieder": 'color_id[]=25',
    "hellblau": 'color_id[]=26',
    "blau": 'color_id[]=9',
    "marienblau": 'color_id[]=27',
    "türkis": 'color_id[]=17',
    "mintgrün": 'color_id[]=30',
    "grün": 'color_id[]=10',
    "dunkelgrün": 'color_id[]=28',
    "khaki": 'color_id[]=16',
    "braun": 'color_id[]=2',
    "senffarben": 'color_id[]=29',
    "gelb": 'color_id[]=8',
    "silber": 'color_id[]=13',
    "gold": 'color_id[]=14',
    "bunt": 'color_id[]=15'
}

male_conf = {
    "sizes": male_sizes,
    "category": male_catergories,
}

female_conf = {
    "sizes": female_sizes,
    "category": female_catergories
}


Mapper = {
    "male": male_conf,
    "female": female_conf,    
    "colors": colors,
    "brands": brands, 
    "helper": size_category_map
}