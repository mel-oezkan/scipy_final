


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

# only all 
male_catergories = {
    "shoes": "test"
} 

female_catergories = {
    "shoes": None,
    "pants": None,
    "shirt": None,
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
    "addidas": None,
    "nike": None,
    "prada": None,
}

colors = {
    "red": "color_id[]=187", # not real id
    "green": None,
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
}