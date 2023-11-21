from typing import NamedTuple
from math import sin, cos, asin, sqrt, radians

Coordinates3D = NamedTuple ("Coordinates3D",
                            [("latitude", float), ("longitude",float), ("altitude",float)])

def to_radians(c:Coordinates3D)->Coordinates3D:
    '''Devuelve una nueva coordenada con la latitud y longitud de la coordenada
    dada como parámetro convertida en radianes. La altitud es la misma que
    la coordenada original

    :param c: Coordenada con la latitud y la longitud en grados
    :type c: Coordenadas3D
    :return: Una coordenada en la que la latitud y la longitud está en radianes
    :rtype: Coordenadas3D
    '''
    return Coordinates3D(radians(c.latitude), radians(c.longitude), c.altitude)

def haversine_distance(coordenadas1:Coordinates3D, coordenadas2: Coordinates3D)->float:
    '''Calcula la distancia haversine entre dos puntos (en km)

    :param coordenadas1: Coordenadas del primer punto
    :type coordenadas1: Coordenadas3D
    :param coordenadas2: Coordenadas del segundo punto
    :type coordenadas2: Coordenadas3D
    :return: Distancia haversine en km
    :rtype: float
    '''
    #1. Convertir las coordenadas a radianes
    c1 = to_radians(coordenadas1)
    c2 = to_radians (coordenadas2)

    #2. Diferencia de latitudes y longitudes
    dif_lat = c2.latitude - c1.latitude
    dif_lon = c2.longitude - c1.longitude

    #3. Calcular a 
    a = sin(dif_lat/2)**2 + \
        cos(c1.latitude) * cos(c2.latitude) * sin (dif_lon/2) **2

    #4. calcular la distancia
    r = 6371 # Radio de la tierra
    return 2 * r * asin (sqrt(a))                            


def haversine_distance_3D(coordenada1:Coordinates3D, coordenada2:Coordinates3D)->float:
    '''Calcula la distancia haversine entre dos puntos, teniendo en cuenta la altitud
    mediante el teorema de pitágoras.

    :param coordenadas1: Coordenadas del primer punto
    :type coordenadas1: Coordenadas3D
    :param coordenadas2: Coordenadas del segundo punto
    :type coordenadas2: Coordenadas3D
    :return: Distancia haversine en km, teniendo en cuenta la altitud
    :rtype: float
    '''
    alt_dif = (coordenada1.altitude-coordenada2.altitude)/1000
    dist2D = haversine_distance(coordenada1, coordenada2)
    return sqrt(alt_dif**2 + dist2D**2)