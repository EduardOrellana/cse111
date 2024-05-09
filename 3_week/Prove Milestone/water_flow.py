#Copyright @Erick Orellana

"""Getting clean water to all buildings in a city is a large and expensive task. 
Many cities will build an elevated water tank, and install a pump that pushes 
water up to the tank where the water is stored. In the city, when a thirsty person 
opens a water faucet, water runs from the tank through pipes to the faucet. 
Earths gravity pulling on the water in the elevated tank pressurizes the water 
and causes it to spray from the faucet.
"""

#First Exceeding Requirement
#Constant to the full programm

EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
WATER_DENSITY = 998.2000000
WATER_DYNAMIC_VISCOSITY = 0.0010016


def water_column_height(tower_height, tank_height):
    """Compute and return the height of the water column 
    to resolve the problem to one Engineer who will build the water distribution
    system.
    
    Parameters:
        tower_height: An measure to extract the height of the tower.
        Tank Height: will be indicate the size and height of the tank of water

    Return: Water Column Height.
    """

    water_column_height = tower_height + ((3 * tank_height) / 4)

    return water_column_height

def pressure_gain_from_water_height(height):
    '''This functions will calculate and return the pressure caused
    by Earth's gravity pulling on the water stored in an elevated tank.
    
    Parameter: 
        height: height of the water column in meters (water_column_height result)
    '''
    #Measure to discover the height
    density_of_water = WATER_DENSITY
    acceleration_from_earths_gravity = EARTH_ACCELERATION_OF_GRAVITY

    
    #Return presssure in kilopascals
    pressure_in_kilopascals = (density_of_water * \
                               acceleration_from_earths_gravity * \
                                height) \
                                / 1000

    return pressure_in_kilopascals


def pressure_loss_from_pipe(pipe_diameter,
                            pipe_lenght, friction_factor,
                            fluid_velocity):
    
    '''Calculates and returns the water pressure lost because of the friction
    between the water and the walls of a pipe that it flows through.
    Variables:
    P is the lost pressure in kilopascals
    f is the pipe's friction factor
    L is the lenght of the pipe in meters
    pw is the density of water 997.2 (kilogram/meter 3)
    v is the velocity of t he water flowing through the pipe in meters/second
    d is the diameter of the pipe in meters

    Parameters:
    Pipe diameter, Pipe lenght, Friction Factor, Fluid Velocity
    '''
    #Variables in the description of the function there is the means of each one.
    f = friction_factor
    L = pipe_lenght
    pw = WATER_DENSITY #water density constant
    v = fluid_velocity
    d = pipe_diameter

    P = -f*L*pw*(v**2) / (2000 * d)

    #Return the function purpose 
    
    return P



def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    '''calculates the water pressure lost because of fittings such as 45° 
    and 90° bends that are in a pipeline. The function must have this header:

    Use this formula: P = -0.04pv**2n/2000

    Where (they are the variables):
    P is the lost pressure in kilopascals
    p is the density of the water 998.2
    v is the velocity of the water flowing through the pipe in meters/second
    n is the quantity of fittings

    Parameters, fluid velocity and quantity fittings 

    Returns P
    '''
    #Variables in the description of the function there is the means of each one.
    p = WATER_DENSITY #Constan Water Density
    v = fluid_velocity
    n = quantity_fittings



    pressure = (-0.04 * p * (v**2) * n) / 2000

    #Return the function purpose

    return pressure



def reynolds_number(hydraulic_diameter, fluid_velocity):
    ''''calculates and returns the Reynolds number for a pipe with water flowing
    through it. The Reynolds number is a unitless ratio of the inertial and
    viscous forces in a fluid that is useful for predicting fluid flow in
    different situations.

    Parameters:
    hydraulic_diameter and fluid_velocity

    Formula:
    R = pdv/μ

    Variables:

    p is the density of water 998.2
    d is the hydraulic diameter of a pipe in meters (parameter)
    v is the velocity of the water flowing through the pipe in meters/second
    dy = dynamic viscosity of water 0.0010016 Pascal seconds
    '''

    #variables for the working on this function:

    p = WATER_DENSITY #Constant Water Density
    d = hydraulic_diameter
    v = fluid_velocity
    dy = WATER_DYNAMIC_VISCOSITY #Constant Water Dynamic Viscosity


    reynols_num = (p*d*v) / dy

    #Return the function purpose

    return reynols_num



def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, 
                                      reynolds_number, smaller_diameter):
    '''calculates the water pressure lost because of water moving from a pipe
    with a large diameter into a pipe with a smaller diameter.
    
    Parameters:
    Larger diameter
    Fluid velocity
    reynolds number
    Smaller diameter

    Fomrulas:
    k = (0.1 +(50/R) ) * ( ((D/d) **4) -1)
    P = (-k*p*(v**2))/200


    where (variables):

    k is a constant computed by the first formula and used in the second formula
    
    R is the Reynolds number that corresponds to the pipe with 
    the larger diameter
    
    D is the diameter of the larger pipe in meters
    
    d is the diameter of the smaller pipe in meters
    
    P is the lost pressure kilopascals
    
    den is the density of water (998.2 kilogram / meter3)
    
    v is the velocity of the water flowing through the larger diameter 
    pipe in meters / second
    '''

    #variables

    reynolds = reynolds_number
    larg_diameter = larger_diameter
    small_diameter = smaller_diameter
    density = WATER_DENSITY #Constant Water Density
    velocity = fluid_velocity

    #first formula:

    konstand = (0.1 +(50/reynolds))*(((larg_diameter/small_diameter)**4)-1)

    pressure_kilopascals = (-konstand * density * (velocity**2)) / 2000

    return pressure_kilopascals

#Second Exciding Requirement
#Function to convert kPa to psi

def convert_kPa_to_psi(kPa):
    '''calculate water pressure in kilopascals (kPa). In the United States,
    water pressure is usually expressed in pounds per square inch (psi).

    Paremeters:
    kPa the value that the principal program provide us

    measures:
    1 psi = 6894.76 Pa (Pascals)
    1 kPa = 1000 Pa

    psi value x 6894.76 Pa = kPa value * 1000 Pa

    Formula:

    psi value = kPa value * 0.145038

    Returns the kPa value in psi value
    '''
    
    measure_psi = 0.145038

    psi = kPa * measure_psi

    #Return the kPa convert into psi
    return psi


PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)

HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)


def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))

    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)

    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss

    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss

    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss

    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss

    #Thrid Exciding Requirement
    psi = convert_kPa_to_psi(pressure)
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    print(f'Convert to: {psi:.1f} psi')



if __name__ == "__main__":
    main()


