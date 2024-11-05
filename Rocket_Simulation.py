
import math

METER_TO_FEET_CONV = 3.28
DENSITY_METER_CUBED = 1.225
MID_ROCKET_MASS_KG = 100000
HEAVY_ROCKET_MASS_KG = 400000
LIGHT_ROCKET_FUEL_RATE = 1360
MID_ROCKET_FUEL_RATE = 2000
HEAVY_ROCKET_FUEL_RATE = 2721
DOLLAR_COST_METAL_SQUARE_METER = 5
DOLLAR_COST_FUEL_KG = 6.1
QUEBEC_TAX_RATE = 1.15
MAX_STORAGE_SPACE_PERCENT = 0.4
MAX_STORAGE_WEIGHT_PERCENT = 0.05
MIN_BOX_WEIGHT_KG = 20
MAX_BOX_WEIGHT_KG = 500
MIN_BOX_VOL_METERS = 0.125

def round_two_dec(float):
    '''
    (num) -> num
    Returns a value rounded to two decimal places
    
    examples:
    
    round_two_dec(4.54656)
    >>> 4.55
    
    round_two_dec(67.451)
    >>> 67.45
    
    round_two_dec(5657.23123131)
    >>> 5657.23
    '''

    return round(float, 2)


def feet_to_meter(feet):
    '''
    (num) -> num
    Takes value in feet and returns equal value in meters rounded to two decimal places
    
    example:
    feet_to_meter(1.0)
    >>> 3.28
    
    feet_to_meter(5.0)
    >>> 1.52
    
    feet_to_meter(2.0)
    >>> 6.56
    '''

    return round_two_dec(feet / METER_TO_FEET_CONV)


def rocket_volume(radius, height_cone, height_cyl):
    '''
    (num, num, num) -> num
    Returns the total volume of the rocket ronded to two decimal places
    
    examples:

    rocket_volume(6, 45, 90)
    >>> 11875.22

    rocket_volume(78, 123, 384)
    >>> 8123216.12

    rocket_volume(0.23445, 9.345, 3.5456)
    >>> 1.15
    '''   
#   Computing volumes of each component of the rocket.
    vol_cone = math.pi * (radius ** 2) * (height_cone / 3)
    vol_cyl = math.pi * (radius ** 2) * height_cyl

    return round_two_dec(vol_cone + vol_cyl)


def rocket_area(radius, height_cone, height_cyl):
    '''
    (num, num, num) -> num
    Returns the surface area of the rocket based on given dimensions

    example: 
    rocket_area(4.0, 4.3, 9.5)
    >>> 362.83

    rocket_area(13.4, 17.6, 3.9)
    >>> 1823.68

    rocket_area(4.2 ,9.5 ,6.8)
    >>> 371.92
    '''
#   Computing surface area of each component of the rocket.
    area_cone = math.pi * radius * (radius + math.sqrt((height_cone ** 2) + (radius ** 2)))
    area_cyl = 2 * math.pi * radius * (height_cyl + radius)

#   Adding surface area, subtracting the circular base of each component where they meet.
    total_area = area_cone + area_cyl - (2 * math.pi * (radius ** 2))
    
    return round_two_dec(total_area)


def rocket_mass(radius, height_cone, height_cyl):
    '''
    (num, num, num) -> num
    Returns mass of the rocket based on the volume
    
    examples:

    rocket_mass(4.5, 3.7, 8.7)
    >>> 774.11

    rocket_mass(6.4, 8.9, 2.7)
    >>> 893.25

    rocket_mass(13.4, 17.6, 3.9)
    >>> 6749.04
    '''
#   Computing rocket volume.
    volume = rocket_volume(radius, height_cone, height_cyl)

#   Multiply volume by density to get mass, round to 2 decimal places
    return round_two_dec(volume * DENSITY_METER_CUBED)


def rocket_fuel(radius, height_cone, height_cyl, velocity_e, velocity_i, time):
    '''
    (num, num, num, num, num, num) -> num
    Returns the mass of fuel consumed by the rocket depending on mass,
    velocity, and time the rocket spends in orbit
    
    examples:
    rocket_fuel(5.6, 6.5, 9.7, 4.8, 5.9, 5.2)
    >>> 10535.51

    rocket_fuel(4.55, 61.5, 16.7, 17.8, 25.9, 65.2)
    >>> 98407.3

    rocket_fuel(50.0, 100.0, 800.0, 700.0, 300.0, 120.0)
    >>> 4616444.53
    '''

#   Calling mass function and computing fuel required for takeoff. 
    mass = rocket_mass(radius, height_cone, height_cyl)
    takeoff_fuel = mass * ((math.e ** (velocity_i / velocity_e)) - 1)

#   Computing fuel for orbit based on rocket mass
    if mass < MID_ROCKET_MASS_KG:
        orbit_fuel = LIGHT_ROCKET_FUEL_RATE * time
    elif mass < HEAVY_ROCKET_MASS_KG:
        orbit_fuel = MID_ROCKET_FUEL_RATE * time
    else:
        orbit_fuel = HEAVY_ROCKET_FUEL_RATE *time
    
    total_fuel = takeoff_fuel + orbit_fuel
    return round_two_dec(total_fuel)


def calculate_cost(radius, height_cone, height_cyl, velocity_e, velocity_i, time, tax):
    '''
    (num, num, num, num, num, num, bool) -> num
    Returns the approximate cost of building and launching 
    the rocket rounded to the nearest cent
    
    examples:
    calculate_cost(6.7, 5.76, 9.65, 12.5, 4.43, 6.54, False)
    >>> 63107.89

    calculate_cost(126.7, 35.76, 69.65, 32.5, 12.93, 26.54, True)
    >>> 18689557.85

    calculate_cost(16.7, 36.23, 12.5, 3.32, 2.41, 45.99, True)
    >>> 660742.47
    '''

#   Defining the mass and surface area of the rocket.
    fuel_mass = rocket_fuel(radius, height_cone, height_cyl,\
     velocity_e, velocity_i, time)
    surface_area = rocket_area(radius, height_cone, height_cyl)

#   Calculating cost of the materials and the fuel required for the rocket.
    cost_rocket = surface_area * DOLLAR_COST_METAL_SQUARE_METER
    cost_fuel = fuel_mass * DOLLAR_COST_FUEL_KG

#   Calculating total cost based on tax input
    total_cost = cost_rocket + cost_fuel
    if tax:
        return round_two_dec(total_cost * QUEBEC_TAX_RATE)
    else:
        return round_two_dec(total_cost)
    

def compute_storage_space(radius, height_cyl):
    '''
    (num, num) -> num, num, num
    Returns the dimensions (width, length, height) of 
    a storage unit inside the rocket based on given dimensions
    
    examples:
    compute_storage_space(44.5, 53.1)
    >>> (62.93, 62.93, 26.55)

    compute_storage_space(904.223, 433.2)
    >>> (1278.76, 1278.76, 216.6)

    compute_storage_space(25.6, 94.3)
    >>> (36.2, 36.2, 47.15)
    '''

#   Computing storage dimensions.
    len_storage = round_two_dec(math.sqrt(2) * radius)
    width_storage = len_storage
    height_storage = round_two_dec(height_cyl / 2)

    return len_storage, width_storage, height_storage


def load_rocket(init_weight, radius, height_cyl):
    '''
    (num, num, num) -> num
    Returns the weight of a rocket after loading it based on given constraints
    
    examples:
    load_rocket(8760.0, 245.2, 497.5)
    Please enter the weight of the next item (type "Done" when you are done filling the rocket): 19
    Enter the item width: 21
    Enter the item length: 12
    Enter the item height: 12
    Item could not be added... please try again...
    Please enter the weight of the next item (type "Done" when you are done filling the rocket): 30
    Enter the item width: 12
    Enter the item length: 12
    Enter the item height: 12
    Please enter the weight of the next item (type "Done" when you are done filling the rocket): Done
    >>> 8790.0

    Please enter the weight of the next item (type "Done" when you are done filling the rocket): 56
    Enter the item width: 0.2
    Enter the item length: 0.1
    Enter the item height: 0.1
    Item could not be added... please try again...
    Please enter the weight of the next item (type "Done" when you are done filling the rocket): 56
    Enter the item width: 12
    Enter the item length: 12
    Enter the item height: 12
    Please enter the weight of the next item (type "Done" when you are done filling the rocket): 678
    Enter the item width: 43
    Enter the item length: 34
    Enter the item height: 34
    Item could not be added... please try again...
    Please enter the weight of the next item (type "Done" when you are done filling the rocket): 121 
    Enter the item width: 45
    Enter the item length: 45
    Enter the item height: 45
    Please enter the weight of the next item (type "Done" when you are done filling the rocket): Done
    >>> 73270.0

    Please enter the weight of the next item (type "Done" when you are done filling the rocket): 20
    Enter the item width: 1
    Enter the item length: 1
    Enter the item height: 1
    No more items can be added
    >>> 564.0
    '''
#   Retrieving storage space and computing volume.
    [storage_len, storage_width, storage_height] = compute_storage_space(radius, height_cyl)
    storage_vol = storage_len * storage_width * storage_height
    
#   Creating iterateable values to track available and current weight and volume.
    current_weight = init_weight
    available_storage = storage_vol * MAX_STORAGE_SPACE_PERCENT
    available_weight = init_weight * MAX_STORAGE_WEIGHT_PERCENT

#   While loop to evaluate available storage before adding an item.
    while available_storage > MIN_BOX_VOL_METERS and available_weight > MIN_BOX_WEIGHT_KG:

#       Requesting item weight from user.      
        weight_input = input('Please enter the weight of the next item (type "Done" when you are done filling the rocket): ')

#       Ending function by returning current weight if input is "Done".        
        if weight_input == "Done":            
            return round_two_dec(current_weight)
        
#       Setting item weight and dimensions to floats.
        item_weight = float(weight_input)
        item_width = float(input('Enter the item width: '))
        item_length = float(input('Enter the item length: '))
        item_height = float(input('Enter the item height: '))

#       Computing volume of the box based on dimensions.
        item_vol = item_width * item_length * item_height

#       Evaluating if the box is outside given constraints (volume constraints, then weight constraints)
        if item_vol < MIN_BOX_VOL_METERS or available_storage - item_vol < 0:
            print("Item could not be added... please try again...")
        elif item_weight > MAX_BOX_WEIGHT_KG or item_weight < MIN_BOX_WEIGHT_KG or available_weight - item_weight < 0:
            print("Item could not be added... please try again...")

#       Adding the box to storage, incrementing available and current data. 
        else:
            available_storage -= item_vol
            available_weight -= item_weight
            current_weight += item_weight

#   Ending function by indicating that rocket is at capacity and returning current weight
    print("No more items can be added")
    return round_two_dec(current_weight)


def projectile_sim(simulation_time, interval, velocity_i, launch_angle):
    '''
    (int, int, num, num) -> None
    Prints the position of the projectile in the air based on starting conditions until the time window is over, or the projectile hits the ground
    
    examples:
    projectile_sim(45, 5, 56.0, 1.55)
    0.0
    157.31
    69.38
    >>> None

    projectile_sim(23, 1, 45.3, 0.78)
    0.0
    26.95
    44.1
    51.43
    48.95
    36.67
    14.57
    >>> None

    projectile_sim(10, 1, 50.0, 0.79)
    0.0
    30.61
    51.42
    62.41
    63.59
    54.96
    36.53
    8.28
    >>> None
    '''

#   Iterating through each value for time within the simulation period on the given interval.
    for time in range(0, simulation_time + 1, interval):
        height = (-1 / 2 * 9.81 * (time ** 2) + velocity_i * math.sin(launch_angle) * time)

#       Only print the value if it is 0 or positive.        
        if height >= 0:
            print(round_two_dec(height))


def rocket_main():
    '''
    (None) -> None
    Prints details about the trip of a rocket based on inputted information

    example:

    Welcome to the Rocket Simulation!
    Enter the rocket radius in feet: 56
    Enter the rocket cone height in feet: 30
    Enter the rocket cylinder height in feet: 90
    Enter the exhaust velocity for the upcoming trip: 45.8
    Enter the initial velocity for the upcoming trip: 12.4
    Enter the angle of launch for the upcoming trip: 1.55
    Enter the length of the upcoming trip: 12334
    Would you like to factor in tax? 1 for yes, 0 for no: 1
    This trip will cost $117774029.88
    Now loading the rocket:
    Please enter the weight of the next item (type "Done" when you are done filling the rocket): 37
    Enter the item width: 1
    Enter the item length: 1
    Enter the item height: 1
    Please enter the weight of the next item (type "Done" when you are done filling the rocket): Done 
    The rocket and its equipment will weigh 34227.89 kg
    Enter the simulation total time: 60
    Enter the simulation interval: 3
    Now simulating the rocket trajectory:
    0.0
    >>> None
    '''
    
    print("Welcome to the Rocket Simulation!")

#   Revieving inputs related to the rocket and trip.
    radius_feet = float(input("Enter the rocket radius in feet: "))
    cone_height_feet = float(input("Enter the rocket cone height in feet: "))
    cyl_height_feet = float(input("Enter the rocket cylinder height in feet: "))
    velocity_e = float(input("Enter the exhaust velocity for the upcoming trip: "))
    velocity_i = float(input("Enter the initial velocity for the upcoming trip: "))
    launch_angle = float(input("Enter the angle of launch for the upcoming trip: "))
    trip_length = float(input("Enter the length of the upcoming trip: "))
    tax_bool = bool(input("Would you like to factor in tax? 1 for yes, 0 for no: "))

#   Changing values inputted in feet to meters.
    radius_meter = feet_to_meter(radius_feet)
    cone_height_meter = feet_to_meter(cone_height_feet)
    cyl_height_meter = feet_to_meter(cyl_height_feet)

#   Calculating cost from given inputs
    print("This trip will cost $" + \
          str(calculate_cost(radius_meter, cone_height_meter, cyl_height_meter, velocity_e, velocity_i, trip_length, tax_bool)))

#   Computing initial weight to load the rocket
    init_weight = rocket_mass(radius_meter, cone_height_meter, cyl_height_meter)

#   Running load rocket function and displaying end weight
    print("Now loading the rocket:")
    end_weight = load_rocket(init_weight, radius_meter, cyl_height_meter)
    print("The rocket and its equipment will weigh", end_weight, "kg")

#   Retrieving additional variables for simulation
    sim_time = int(input("Enter the simulation total time: "))
    sim_interval = int(input("Enter the simulation interval: "))

#   Simulating rocket trajectory
    print("Now simulating the rocket trajectory:")
    projectile_sim(sim_time, sim_interval, velocity_i, launch_angle)


