#attempt to make the Autodiag
#The goal of this autodiag will be to do basic math for techs and will inform them of what the voltage should be:
#things i would like to check Vehicle type to use schematics?
#if there is a CAN network VS LIN I would like to call the one based on the cars Configurations:
#This is going to become a list of things that need to happen for all of this to work
#I would like to define by vehicle type, maybe the questions or all questions that apply
#Adding CAN Voltage inputs
# LIN = {"thing1":"what is the voltage of pin1 ","thing2":"what is the voltage of pin2: "}
# CAN = {}
# CAN_1 = float(input("what is the voltage of Pin 2: "))

# MAX_CAN = float(3.7)
# MIN_CAN = float(1.2)

# print(CAN)
# print(type(CAN))
# print(type(MAX_CAN))
# print(type(LIN))

# if CAN == MAX_CAN:
#         print("Stuff")
# else:
#     print("not equal")

# input(LIN.keys(thing1))
Voltage_Too_Low = False
#Voltage_Too_Low
Ground_Resistance = 0.02
LIN = float(input("What is the LIN Voltage?: "))

print(LIN)

if LIN < 9:
    Voltage_Too_Low = bool(input("LIN Voltage is too low, are drive rails on? "))
if Voltage_Too_Low == True: #no
    float(input("Please Enable DriveRails and perform test once again,\nWhat is the LIN voltage: "))
    pass

Voltage_is_Okay = float(input("We will now check Ground Resistance\nWhat is the Ground Resistance: "))
if Ground_Resistance < 1.0:
    Ground_resistance_recheck = print("Ground Resistancee is too high!!!")
else:
    pass
#elif LIN < 12 :
#    print("incorrect")


