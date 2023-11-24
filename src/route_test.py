from route import *

def main():
    #EX 1
    ronda = read_route('./data/ruta.csv')
    print(f"We have {len(ronda)} points in the route")
    print('First point: ', ronda[0])
    print('Last point: ', ronda[-1])
    
    #EX 2
    first_ronda = get_sub_route(ronda, time(0,0,0), time(11,48,1))
    second_ronda = get_sub_route(ronda, time(11,48,1),time(23,36,0))
    print(f"We have {len(first_ronda)} points in the first part")
    print(f'We have {len(second_ronda)} points in the second part')
    
    #EX 3
    test_get_distance(ronda, 'complete route')
    test_get_distance(first_ronda, 'first part')
    test_get_distance(second_ronda, 'second part')
    
    #EX 4
    test_get_avg_speed(ronda, 'complete route')
    test_get_avg_speed(first_ronda, 'first part')
    test_get_avg_speed(second_ronda, 'second part')
    
    #EX 4.B
    print(speed_hour(ronda))
    
    #EX 5
    test_slope_difs(ronda, 'complete route')
    test_slope_difs(first_ronda, 'first part')
    test_slope_difs(second_ronda, 'second part')
    
    #EX 6
    show_elevation_profile(ronda)
    
    #EX 8
    show_track_map(ronda, './out/completeroute_ronda.html')
    show_track_map(first_ronda, './out/firstpart_ronda.html')
    show_track_map(second_ronda, './out/secondpart_ronda.html')
    
def test_slope_difs(list_points, name):
    print('Positive and negative altitude differences of ', name)
    print(get_accumulated_slope(list_points))

def test_get_avg_speed(list_points, name):
    print('Speed of the', name)
    print(get_avg_speed(list_points))

def test_get_distance(list_points, name):
    print('Distance of the', name)
    print(get_distance(list_points))
    

if __name__=='__main__':
    main()