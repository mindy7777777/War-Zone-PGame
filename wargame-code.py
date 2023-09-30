import math
from colorama import Fore, Back, Style


message1 = Fore.CYAN+'\t\t\t\tWelcome to the War Zone'
message2 = 'There is a tank  2,000 meters away from you. The tank is approaching with a speed of 30km/h toward you. If the tank is less than 100 meters from you, the tank destroy you. You need to enter the angle for a missile and if the missile hit the tank 50 meters in the front or in the back the tank is destroyed   '

print(message1)
print('-'*80 + Style.RESET_ALL)
print(Fore.LIGHTBLACK_EX + message2 + Style.RESET_ALL)

distance_of_the_tank = 2000
speed_of_the_tank = 80

gravity = 9.8
speed_of_missile = 150
counter = 0

while distance_of_the_tank > 100:
    angle = float(input(Fore.YELLOW+'\n\tEnter the angle in degrees: >'+ Style.RESET_ALL))
    angle = math.radians(angle)
    counter += 1

    missile_distance = (math.pow(speed_of_missile,2) * math.sin(2*angle))/gravity
    impact_dist = abs(distance_of_the_tank - missile_distance)
    if abs(impact_dist) == 50:
        print(Fore.RED+'Congratulation ! You destroyed the tank in', counter,'times'+Style.RESET_ALL)
        break
    else:
        distance_of_the_tank = distance_of_the_tank - speed_of_the_tank
        if impact_dist > 0:
            print(Fore.MAGENTA + 'MISSILE IMPACT:'+ Style.RESET_ALL, abs(round(impact_dist,2)), 'in the front of the tank')
            print(Fore.MAGENTA+'NOW THE TANK\'S NEW POSITION IS:'+ Style.RESET_ALL, distance_of_the_tank)
        else:
            print(Fore.MAGENTA+'MISSILE IMPACT:'+ Style.RESET_ALL, abs(round(impact_dist,2)), 'in the back of the tank')
            print(Fore.MAGENTA+'NOW THE TANK\'S NEW POSITION IS:'+Style.RESET_ALL, distance_of_the_tank)
        if distance_of_the_tank <= 100:
            print('Sorry ! The tank destroyed you...JAJAJA')
            break