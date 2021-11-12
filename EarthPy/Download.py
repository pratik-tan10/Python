import earthpy as ep

# Specify custom directory to download the dataset

ep.data.path = "."

# Specify the dataset name to download

ep.data.get_data('colorado-flood') 
