# mortgage.py
#
# Exercise 1.7

def main():

    principal = 500000.0
    rate = 0.05
    payment = 2684.11
    total_paid = 0.0
    month = 0

    # user "parameters"
    extra_payment = int(input('enter amount of the extra payment:'))
    extra_payment_start_month = int(input('enter month to begin extra payments i.e. 5 is 5th month:'))
    extra_payment_end_month = int(input('enter last month for extra payments i.e. 10 is 10th month:'))

    while principal > 0:
        month += 1
        this_payment = payment
        # increase payment amount if we are in extra payment window
        if month >= extra_payment_start_month and month <= extra_payment_end_month:
            this_payment += extra_payment
        
        # don't pay more than the remaining balance    
        if this_payment > principal * (1+rate/12):
            this_payment = principal * (1+rate/12)

        principal = principal * (1+rate/12) - this_payment
        total_paid = total_paid + this_payment
        print(month, round(total_paid, 2), round(principal, 2))

    print('Total paid', round(total_paid, 2), 'over', month, 'months')

if __name__ == '__main__':
    main()
