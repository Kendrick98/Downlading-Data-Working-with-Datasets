from pathlib import Path
import json

# Read data as a string and convert to a Python object.
path = Path('/Users/mariusoprea/Desktop/python_work/Part II-Projects/Chapter_16_Downloading_Data/Downloading_Data/eq_data/eq_1_day_m1.geojson')
contents = path.read_text()
all_eq_data = json.loads(contents)

# Create a more readable version of the data file.
path = Path('/Users/mariusoprea/Desktop/python_work/Part II-Projects/Chapter_16_Downloading_Data/Downloading_Data/eq_data/readabale_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)