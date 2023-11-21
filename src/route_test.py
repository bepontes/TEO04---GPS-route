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
    

def test_get_distance(list_points, name):
    print('Distance of the', name)
    print(get_distance(list_points))
    

if __name__=='__main__':
    main()