import csv
from datetime import time, datetime
from typing import NamedTuple, List, Dict, Tuple
from coordinates3D import Coordinates3D, haversine_distance_3D
from matplotlib import pyplot as plt
from maps import * 

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
    coor= [t.position for t in track]
    distance_3d= [haversine_distance_3D(coor[n],coor[n+1]) for n in range(len(coor)-1)]
    return sum(n for n in distance_3d)

#HOMEWORK: EXERCISE 4
def get_avg_speed(track:List[Point])->float:
    distance=get_distance(track)
    hours1=track[0].timestamp.hour+track[0].timestamp.minute/60+track[0].timestamp.second/3600
    hours2=track[-1].timestamp.hour+track[-1].timestamp.minute/60+track[-1].timestamp.second/3600
    return(distance/(hours2-hours1))
    
#HOMEWORK:
def speed_hour(track:List[Point])->Dict[int, float]:
    #{0:speed0, 1:speed1, ....., 23:speed23}
    
    speed_dict = dict()
    hours = {p.timestamp.hour for p in track}
    for h in hours:
        points_h = [p for p in track if p.timestamp.hour == h]
        speed_dict[h] = get_avg_speed(points_h)
    
    return speed_dict

#EX 5
def get_accumulated_slope(track:List[Point])->Tuple[float,float]:
    aux_list1=track[:-1]
    aux_list2=track[1:]
    positive=0
    negative=0
    for e_list1, e_list2 in list(zip(aux_list1,aux_list2)):
       diff=e_list2.position.altitude-e_list1.position.altitude
       if diff>0:
         positive+=diff
       else:
         negative+=diff
    return(positive,negative)

#EX 6
def show_elevation_profile(track:List[Point])->None:
    altitudes = [p.position.altitude for p in track]
    kms = get_distance(track) 
    distances = [(kms*i)/len(track)  for i in range(len(track))]
    
    plt.title('Elevation profile of the route')
    plt.xlabel('distance')
    plt.ylabel("altitudes")
    plt.plot(distances,altitudes)
    plt.show()
    
#EX 8
def show_track_map(track:List[Point], outfile:str)->None:
    
    my_map = create_map(track[0].position)
    add_polyline(my_map,[p.position for p in track], 'blue')
    add_marker(my_map,track[0].position, 'Initial point', 'red')
    add_marker(my_map,track[-1].position, 'End point', 'green')
    save_map(my_map,outfile)