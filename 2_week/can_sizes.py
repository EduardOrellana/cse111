'''
Team Activity. 1/17/2024
'''

import math

Names_list = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "6Z", "#8Z short", "#10", "211", "#300", "#303"]

Radius_list = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]

Height_list = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]

Cost_per_Can_list = [0.28, 0.43, 0.45, 0.61, 0.86 , 0.83, 0.22, 0.26, 1.53, 0.34, 0.38, 0.42]

def compute_volume(parRadius, parHeight):
    volume = math.pi * parRadius**2 * parHeight
    return volume

def compute_surface_area(parRadius, parHeight):
    surface_area = 2 * math.pi * parRadius * (parRadius + parHeight)
    return surface_area

def compute_storage_efficiency(parVolume, parSurface):
    storage_efficiency = parVolume/parSurface
    return storage_efficiency

def compute_cost_efficiency(parVolume, parCost):
    cost_efficiency = parVolume/parCost
    return cost_efficiency

def main ():
    for i in range(len(Names_list)):
        r = Radius_list[i]
        h = Height_list[i]
        n = Names_list[i]
        c = Cost_per_Can_list[i]
        volume = compute_volume(r,h)
        surface = compute_surface_area(r,h)
        storage = compute_storage_efficiency(volume, surface)
        cost_efficiency = compute_cost_efficiency(volume,c)
        print(f'{n}, {storage:.2f} and its price {cost_efficiency:.2f}')

        

main()