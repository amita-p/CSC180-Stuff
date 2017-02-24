"""The Credit Card Simulator starter code
You should complete every incomplete function,
and add more functions and variables as needed.
Ad comments as required.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author: Michael Guerzhoy.  Last modified: Sept. 27, 2015
"""

#You should modify initialize()
def initialize():
    '''float variables-cur_balance_owing_intst stores the amount 
    owed that is accruing interest, cur_balance_owing_recent stores 
    the amount that is owed that is not accruing interest'''
    global cur_balance_owing_intst, cur_balance_owing_recent 
    #integer variables which store the last day that the account was updated
    global last_update_day, last_update_month 
    '''string variables which stores the last two countries in which 
    #purchases were made'''
    global last_country, last_country2 
    #boolean variable which stores True if account deactivated, False if not
    global deactivated 
    deactivated = False
    
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
    
    last_update_day, last_update_month = -1, -1
    
    last_country = None
    last_country2 = None
    
    #float variable which stores the monthly interest rate, does not change
    global MONTHLY_INTEREST_RATE 
    MONTHLY_INTEREST_RATE = 0.05

def reset():
    global last_update_day
    global last_update_month
    global cur_balance_owing_intst
    global cur_balance_owing_recent
    global last_country 
    global last_country2 
    global deactivated 
    last_country = None
    last_country2 = None
    deactivated = False
    cur_balance_owing_intst = 0
    cur_balance_owing_recent = 0
    last_update_day, last_update_month = -1, -1

'''Take in two dates, consisting of a day and a month. The first date is 
described by day1 and month2 and the second date is described by day2 and 
month2. Assume all parameters to be integers. Return a boolean value-True if 
date 1 is the same or later than date 2, False if not.'''

def date_same_or_later(day1, month1, day2, month2):
    #all the params are assumed to be integers, dummy proof this
    returnVal = False
    if (month1 > month2):
        returnVal = True
    elif (month1 == month2 and day1 >= day2):
        returnVal = True
    else:
        returnVal = False
    return returnVal

'''Take in 3 values, c1, c2, and c3, which are assumed to be strings or None. 
Returns a boolean value-True if all three of them are different from each other,
False if not (not case sensitive). However, if any of them are None, it returns
false. '''

def all_three_different(c1, c2, c3): 
    c1 = c1.lower()
    if (c2 != None):
        c2 = c2.lower()
    if (c3 != None):
        c3 = c3.lower()
    if (c1 == None or c2 == None or c3 == None):
        return False
    if (not c1 == c2 and not c2 == c3 and not c1 == c3):
        return True
    else:
        return False

'''Take in the current day and month, 'day' and 'month', and assume to be 
integer values; update the interest on the account'''

def end_Of_Month_Update(day,month):
    global last_update_day
    global last_update_month
    global MONTHLY_INTEREST_RATE
    global cur_balance_owing_intst
    global cur_balance_owing_recent
    #if the last update occured last month or before that
    if (last_update_month < month): 
        #Increase the amount accruing interest by 0.05. 
        cur_balance_owing_intst = cur_balance_owing_intst * \
        MONTHLY_INTEREST_RATE + cur_balance_owing_intst
        '''Add whatever was not accruing interest (cur_balance_owing_recent) to
         cur_balance_owing_intst, so that it starts acruing interest'''
        cur_balance_owing_intst += cur_balance_owing_recent
        cur_balance_owing_recent = 0 
        #For every month after, increase the amount accruing interest by 0.05
        for i in range((month - last_update_month) - 1):
            cur_balance_owing_intst = cur_balance_owing_intst * \
            MONTHLY_INTEREST_RATE + cur_balance_owing_intst
        
'''Take in the current day and month, 'day and 'month' (assume to be integers), 
as well as the amount of the purchase (assume to be a float).  Also take in the 
country where the purchase is taking place (assume it to be a string). Add the 
purchase to the cur_balance_owing_recent, only if the card is not deactivated. 
If the last 2 countries that purchases were made in and the parameter 'country'
 are all different, deactivate. Do not return any value.'''

def purchase(amount, day, month, country): 
    global last_update_day
    global last_update_month
    global cur_balance_owing_intst
    global cur_balance_owing_recent
    global last_country
    global last_country2
    global deactivated
    if (date_same_or_later(day,month, last_update_day, last_update_month) == \
    False):
        return "error (date is before last date)"
    end_Of_Month_Update(day,month)
    last_update_day = day
    last_update_month = month
    if (deactivated == False):
        if (all_three_different(country, last_country, last_country2)):
            deactivated = True
            return "error (3 diff countries in row)"
        #add the amount to the recent balance 
        cur_balance_owing_recent = cur_balance_owing_recent + amount 
        #update the variables which store the previous countries
        last_country2 = last_country
        last_country = country
    else:
        return "error (card disabled)"
    
    
    
'''Take in the current date, through the parameters 'day' and 'month' and assume
 them to be integers. Return the total amount owed. '''

def amount_owed(day, month):
    global last_update_day
    global last_update_month
    global cur_balance_owing_intst
    global cur_balance_owing_recent
   
    end_Of_Month_Update(day,month)
    if (date_same_or_later(day,month, last_update_day, last_update_month) == \
    False):
        return "error (date is before last date)"
    
    last_update_day = day
    last_update_month = month
    return (cur_balance_owing_intst + cur_balance_owing_recent)
    
'''Takes in the current date through the parameters 'day' and 'month' and assume
 them to be integers. Take in the amount to be paid, 'amount' and assume it to 
 be a float. Before paying the cur_balance_owing_recent, pay the 
 cur_balance_owing_intst.'''

def pay_bill(amount, day, month):
    global cur_balance_owing_intst 
    global cur_balance_owing_recent 
    global last_update_month
    global last_update_day
   
    end_Of_Month_Update(day,month)

    if (date_same_or_later(day,month, last_update_day, last_update_month) == \
    False):
        return "error (date is before last date)"
        
    if (amount <= cur_balance_owing_intst and amount>0):
        cur_balance_owing_intst = cur_balance_owing_intst-amount
    elif (amount > cur_balance_owing_intst and amount <= \
    (cur_balance_owing_intst+cur_balance_owing_recent)):
        cur_balance_owing_recent = cur_balance_owing_recent - \
        (amount - cur_balance_owing_intst)
        cur_balance_owing_intst = 0;
    #Reaching this else statement indicates that either amount is not greater 
    #than 0 or is greater than the amount owed, making it an invalid payment 
    #value
    else:
        return "This is not a valid payment value!"
    last_update_day = day
    last_update_month = month
    
        
        
        
    
    
if __name__ == '__main__':
    #Describe your testing strategy and implement it below.
    initialize()
    #Testing 1 (Simulation from handout)
    print ("TESTING 1")
    purchase(80, 8, 1, "Canada")
    print("Now owing:", amount_owed(8, 1))      #80.0
    pay_bill(50, 2, 2)
    print("Now owing:", amount_owed(2, 2))      #30.0     (=80-50)
    print("Now owing:", amount_owed(6, 3))      #31.5     (=30*1.05)
    purchase(40, 6, 3, "Canada")
    print("Now owing:", amount_owed(6, 3))      #71.5     (=31.5+40)
    pay_bill(30, 7, 3)
    print("Now owing:", amount_owed(7, 3))      #41.5     (=71.5-30)
    print("Now owing:", amount_owed(1, 5))      #43.65375 
    purchase(40, 2, 5, "France")
    print("Now owing:", amount_owed(2, 5))      #83.65375 
    print(purchase(50, 3, 5, "United States"))  #error    (3 diff. countries in 
                                                #          a row)
                                                
    print("Now owing:", amount_owed(3, 5))      #83.65375 (no change, purchase
                                                #          declined)
    print(purchase(150, 3, 5, "Canada"))        #error    (card disabled)
    print("Now owing:", amount_owed(1, 6))      #85.8364375 
                                                #(43.65375*1.05+40)
    reset()
    '''Testing 2-How does pay_bill react when the 'amount' parameter is given an
     invalid payment (ex. greater than amount owed, negative, or 0)'''
    print ("TESTING 2")
    print (purchase (100,1,1,"Canada"))
    purchase (50,2,5,"Canada")                  
    print("Now owing:", amount_owed(2, 5))      #165.7625
    print(pay_bill(-500,2,5))                   #not a valid payment value
    print (pay_bill(50000,2,5))                 #not a valid payment value
    print (pay_bill(0,2,5))                     #not a valid payment value
    
    reset()
    '''Testing 3-What happens when purchase() is called with the different 
    country for the third time in a row, and invalid date is entered'''
    print ("TESTING 3")
    print (purchase (500,1,1,"Canada"))
    print (purchase(200,5,6,"France"))
    print (purchase (700,1,1,"United States"))   #error (date before last date)         
    print (deactivated)                          #False-the account does not get
                                                 #deactivated
    
    reset()
    '''Testing 4-What happens when the last 2 countries of purchase and the 
    current country are the same, but have different cases'''
    print ("TESTING 4")
    print (purchase (500,1,1, "Canada"))               #None (purchase success)
    print (purchase (500,1,1, "canada"))               #None (purchase success)
    print (purchase (500,1,1, "canaDa"))               #None (purchase success)
    
    reset()
    '''Testing #5- What happens when the last_country2=None, and last_country 
    and the current country where the purchase is trying to be made aren't 
    equal?'''
    print ("TESTING 5")
    print (purchase (500,1,1,"Canada"))                 #None (purchase success)
    print (purchase(200,5,6,"France"))                  #None (purchase success)
    
    reset()
    '''Testing #6-Do purchases that were made that month have interest acrued on
     them the next month? Does the amount owed due to those purchases end up in 
     the cur_balance_owing_ints variable as they should be?'''
    print ("TESTING 6")
    print (purchase (100,1,1,"Canada"))                 #None (purchase success)
    print (cur_balance_owing_recent)                    #100
    print("Now owing:", amount_owed(5, 2))              #100
    print (cur_balance_owing_intst)                     #100
    print (cur_balance_owing_recent)                    #0
    
    reset()
    #Testing #7-What happens if a huge number of days is entered as a parameter of the functions which take in dates?
   
#what should happen if 65 is entered as the number of days
                                            
                                            
    