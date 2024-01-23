from pathlib import Path
import csv

path = Path('/Users/mariusoprea/Desktop/python_work/Part II-Projects/Chapter_16_Downloading_Data/Downloading_Data/weather_data/sitka_weather_07-2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)
print(header_row)