import csv
from datetime import time, datetime
from typing import NamedTuple, List, Dict
from coordinates3D import Coordinates3D

Point = NamedTuple('Point', [('timestamp',datetime.time),('position',Coordinates3D)])

#EX 1
def read_route(file:str)->List[Point]:
    with open(file, encoding='utf-8') as f:
        lector = csv.reader(f)
        point_data = []
        for timestamp,latitude,longitude,altitude in lector:
            location = Coordinates3D(float(latitude), float(longitude),float(altitude))
            timestamp = datetime.strptime(timestamp, '%H:%M:%S').time()
            point_data.append(Point(timestamp,location))
    return point_data

#EX_2
def get_sub_route(track:List[Point], iniT:datetime.time, finalT:datetime.time)->List[Point]:
    return [n for n in track if iniT<=n.timestamp<finalT]
 
#EX_3
def get_distance(track:List[Point])->float:
    #implement harvesine_distance_3D in module coordinates3D
    
    #compute the total distance using "intermediate" distances
    pass

#HOMEWORK: EXERCISE 4

#HOMEWORK:
def speed_hour(track:List[Point])->Dict[int, float]:
    #{0:speed0, 1:speed1, ....., 23:speed23}
    pass