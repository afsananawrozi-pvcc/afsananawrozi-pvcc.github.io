#Name: Afsana Nawrozi
# Prog Purpose: This program computes the amount of tax for vehicals in Charlottesville.

import datetime
TAX = .042
PR_TAX_RE = .33
value = 0
annualtax = 0
sixmonth = 0
eligible = 0
totaldue = 0


################ define program functions ###############
def main():
    more = True

    while more:
        get_user_data()
        perform_calculations()
        display_results()

        askAgain = input("\nDo you have another vehicle? (Y or N)?: ")
        if askAgain.upper() == "N" or askAgain.upper() == "NO":
            print("Pay by December 05, 2023!")
            more = False
            
def get_user_data():
    global value, taxrelief_yesno, totaldue, eligible  
    value = int(input("\nWhat is assessed value of the vehicle? "))
    taxrelief_yesno = input ("\nIs this vehicle eligible for tax relief? (Y or N)?: ")
  
def perform_calculations():
    global annualtax, taxrelief, total, sixmonth, totaldue, eligible
    annualtax = value * TAX
    sixmonth = annualtax / 2
    if taxrelief_yesno.upper() == "Y":
        eligible = sixmonth * PR_TAX_RE
    else:
        eligible = 0
    totaldue = sixmonth - eligible
    
def display_results():
    line ='---------------------------------------------'
    moneyf = '>10,.2f'
    print(line)
    print('********** City of Charlottesville, VA *********')
    print('********** Personal Property Tax       **********')
    print('Assessed value of vehicle    $ ' + format (value,moneyf))
    print('Annual Tax                   $ ' + format(annualtax,moneyf))
    print('sixmonth Tax                 $ ' + format(sixmonth,moneyf))
    print('Tax Relief Eligible          $ ' + format(eligible,moneyf))
    print(line)
    print('Total Due                    $ ' + format(totaldue,moneyf))

    print(str(datetime.datetime.now()))


########### call o main program to excute ###########
main()
    

        












