#Nmae: Afsana Nawrozi
#Prog Purpose: This program finds the cost of pet vaccines & medications for dogs and cats
#
#NOTE: Pet medicaations prescribed by lincenced veterians are not subject to sales tax in Virginia
#
#PET CARE MEDS Pricing
#------------------------------
#Canine Vaccines:
# 1. Bordatella $30.00
# 2. RAPP $35.00
# 3. Influenza $48.00
# 4. Leptospirosis $21.00
# 5. Lyme Disease $41.00
# 6. Rabies $25.00
# 7. Full Vaccine package (includes all vaccines): 15% discount
#
#Canine Heartworm Preventative Chews (price per chew; one chew per month)
#Small dogs, Up to 25 lbs: $9.99
#Medium-sized dogs, 26 to 50 lbs: $11.99
#Large dogs: 51 to 100 lbs: $13.99


############## CAT functions ####################

# Fekine Vaccine Pricing:
# 1. Feline Leukmeia $35
# 2. Feline Viral Rhinptracheitis $30
# 3. Rabies (one year) $25
# 4. Full Vaccine Package (includes all vaccines): 10 % discount
# Feline Heartworm Prevention Chews (one size) $8.00


import datetime

################# define global variables###############
# define dog prices
PR_BORD = 30
PR_DAPP = 35
PR_FLU  = 48
PR_LEP  = 21
PR_LYME = 41
PR_RAB  = 25

PR_ALL = 0

PR_CHEWS_SMALL = 9.99
PR_CHEWS_MED = 11.99
PR_CHEWS_LARGE = 13.99


############## define global variables ##############
# define cat prices
PR_FEL_LEU = 35
PR_FEL_VIR = 30
PR_RAB = 25
PR_ALL = 0
PR_CHEWS = 8

#define global variables

############## define program functions ###########
def main():
    more = True
    while more:
        get_user_data()

        if pet_type.upper() == "D":
            get_dog_data()
            perform_dog_calculations()
            display_dog_results()
        else:
            get_cat_data()
            perform_cat_calculations()
            display_cat_results()

        askAgain = input("\nWould you like process another pet (Y/N: ")
        if askAgain.upper()== "N":
            more = False
            print ('Thank you for trusting PET CARE MEDS with your pet vaccines and medications.')

def get_user_data ():
    global pet_name, pet_type, pet_weight
    pet_name = input ("Pet name: ")
    pet_type = input ("Is this pet a dog (D) or cat (C)? ")
    pet_weight = int(input ("Weight of your pet (in pounds): "))

############# DOG functions ####################

def get_dog_data():
        global pet_vax, num_chews
        dog1 = "\n** Dog Vaccines: \n\t1.Bordatella \n\t2.DAPP"
        dog2 = "\n\t3.Influenza \n\t4.Leptopirosis \n\t5.Lyme Disease \n\t6.Rabies \n\t7.Full Vacccine Package \n\t8.NONE"
        dogmenu = dog1+dog2
        pet_vax = int(input(dogmenu+ "\n** Enter the vaccine number: "))

        print ("\nMonthly heartworm prevention medication is recomended for all dogs ")
        heart_yesno= input ("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N)? ")
        if heart_yesno.upper()== "Y" :
           num_chews = int(input("How many heart worm chews would you like to order? "))
        else:
            num_chews = 0

def perform_dog_calculations():
    global vax_cost, chews_cost, total

####### Vaccines #######
    if pet_vax == 1 :
        vax_cost = PR_BORD

    elif pet_vax == 2 :
        vax_cost = PR_DAPP

    elif pet_vax == 3 :
        vax_cost = PR_FLU

    elif pet_vax == 4 :
        vax_cost = PR_LEP

    elif pet_vax == 5 :
        vax_cost = PR_LYME

    elif pet_vax == 6 :
        vax_cost = PR_RAB

    elif pet_vax == 8:
        vax_cost = 0

    else:
        PR_ALL = PR_BORD + PR_DAPP + PR_FLU
        vax_cost = .85 * PR_ALL

######## Heartworm Chews ##############
    if num_chews != 0 :
        if pet_weight <25 :
            chews_cost = num_chews * PR_CHEWS_SMALL

        elif pet_weight >= 26 and pet_weight <50 :
            chews_cost = num_chews * PR_CHEWS_MED

        else:
            chews_cost = num_chews * PR_CHEWS_LARGE

    total = vax_cost + chews_cost

def display_dog_results():
    moneyformat = '8,.2f'
    line = '---------------------------------'
    print(line)
    print('**** Pet Care Medications ****')
    print('')
    print(line)
    print('Dog Vacccine         $ ' + format(vax_cost, moneyformat))
    print('Heartworm            $ ' + format(chews_cost, moneyformat))
    print('Total                $ ' + format(total, moneyformat))
    print(line)
    print(str(datetime.datetime.now()))
    
def get_cat_data():
        global pet_vax, num_chews, total
        cat1 = "\n** Cat Vaccines: \n\t1.Feline Leukmeia \n\t2.Feline Viral rhinptracheitis"
        cat2 = "\n\t3.Rabies (one year) \n\t4.Full Vacccine Package \n\t5.NONE"
        catmenu = cat1+cat2
        pet_vax = int(input(catmenu+ "\n** Enter the vaccine number: "))
        
        print ("\nMonthly heart worm prevention medication is recomended for all cats ")
        heart_yesno= input ("Would you like to order monthly heartworm medication for " + pet_name + " (Y/N)? ")
        if heart_yesno.upper()== "Y" :
           num_chews = int(input("How many heart worm chews would you like to order? "))

def perform_cat_calculations():
    global vax_cost, chews_cost, total

####### Vaccines #######
    if pet_vax == 1 :
        vax_cost = PR_FEL_LEU

    elif pet_vax == 2 :
        vax_cost = PR_FEL_VIR

    elif pet_vax == 3 :
        vax_cost = PR_RAB

    elif pet_vax == 4:
        vax_cost = 0

    else:
        PR_ALL = PR_FEL_LEU + PR_FEL_VIR + PR_RAB
        vax_cost = .90 * PR_ALL

    chews_cost = num_chews * PR_CHEWS

def display_cat_results():
    print("DISPLAY CATS")


########## call on main program to excute ########
main()


    
    
        
























        
