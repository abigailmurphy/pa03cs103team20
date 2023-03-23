
from transaction import Transaction
import sys

# here are some helper functions ...

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            tracker quit
            tracker showall categories
            tracker add category
            tracker modify category
            tracker show transactions
            tracker add transaction
            tracker delete transaction
            tracker summarize by_date
            tracker summarize by_month
            tracker summarize by_year
            tracker summarize by_category
            '''
            )

def print_trackers(trackers):
    ''' print the tracker items '''
    if len(trackers)==0:
        print('no tasks to print')
        return
    print('\n')


def process_args(arglist):
    ''' examine args and make appropriate calls to Transaction'''
    transaction = Transaction()
    if arglist==[]:
        print_usage()
    elif arglist[0]=="showall categories":
        print_trackers(trackers = transaction.distinctCategories())
    elif 
    



