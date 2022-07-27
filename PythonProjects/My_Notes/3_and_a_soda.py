# 3 peice and a soda
import re

ground_resistance = 0
ground_resistance_high = 0
voltage_exceeded_thresh = 0
voltage_response = 0
lin_response = 0
battery_voltage = 0
antenna_resistance = 0
antenna_harness_resistance = 0
# ground_resistance_high = None
# voltage_exceeded_thresh = None

check_ground = True
check_twelveVolt = False


def twelveVoltsystem(ground_resistance,
                     voltage_response,
                     lin_response
                     ):
    
    '''
    This function will take in users input and based on component being checked will return a True or false statement
    We can then determin which steps need to be taken after. Components default values are set to "0" if user needs the values 
    the question will populate and will return an answer for the user based on the information needed. Values will still be "0"
    on components not used
    '''
    
    voltage_exceeded_thresh = ''
    ground_resistance_high = ''
    
    
    # Validate ground resistance response from user
    if isinstance(ground_resistance, str):
        val_ground_resistance = re.search(r'\d+.\d+', ground_resistance) #check if user provided float i.e 10.4
        if val_ground_resistance :
            ground_resistance = float(val_ground_resistance.group())
        else:
            ground_resistance = re.search(r'\d+', ground_resistance) #else default to whole number
            ground_resistance = float(ground_resistance.group())
    # Validate voltage response from user
    if isinstance(voltage_response, str):
        val_voltage_response = re.search(r'\d+.\d+', voltage_response) #check if user provided float i.e 10.4
        if val_voltage_response :
            voltage_response = float(val_voltage_response.group())
        else:
            voltage_response = re.search(r'\d+', voltage_response) #else default to whole number
            voltage_response = float(voltage_response.group())
            
    # Validate LIN response from user
    if isinstance(lin_response, str):
        val_lin_response = re.search(r'\d+.\d+', lin_response) #check if user provided float i.e 10.4
        if val_lin_response :
            lin_response = float(val_lin_response.group())
        else:
            lin_response = re.search(r'\d+', lin_response) #else default to whole number
            lin_response = float(lin_response.group())
            
            
    if isinstance(lin_response, float) and isinstance(voltage_response, float):
        if abs(lin_response + voltage_response) <= 12:
            voltage_exceeded_thresh = True
        else:
            voltage_exceeded_thresh = False
            
        if abs(ground_resistance) <= 1.0:
            ground_resistance_high = False
        else:
            ground_resistance_high = True
        
        
    
    return ground_resistance, voltage_response, lin_response, voltage_exceeded_thresh, ground_resistance_high


ground_resistance_high = False
ground_resistance = input('what is the ground resistance: ')
voltage_response = input('what is the voltage: ')
lin_response = input("what is the LIN: ")
total = twelveVoltsystem(ground_resistance,voltage_response,lin_response)
# print(type(lin_response))
# print(type(total))
print(total)

# print(type(ground_resistance))

# print(ground_resistance)

if  ground_resistance_high is True:
    print("im too high")
else:
    print("im low enough ")


if check_ground is True:
    if  ground_resistance_high is True:
        print("im too high")
    else:
        print("im low enough ")
    
if check_twelveVolt is True:
    voltage_response = input("check 12V wires: ")

# if check_ground is True:
#     total = twelveVoltsystem(ground_resistance,voltage_response,lin_response)

# for thing in total:
#     if ground_resistance_high is  True:
#         print("Resistance in circuit is high/ Request  double check")
#     else:
#         print("Resistance is aOkay")
# print(total)





print(ground_resistance_high)
print(type(ground_resistance_high))

#components we should need for math#  Voltage drop test
#5V circuit test
#3V Circuit Test
#antenna resistance test
#antenna harness 
#battery voltage
#resistance of wires