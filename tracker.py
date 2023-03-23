
from transaction import Transaction
import sys

# here are some helper functions ...

def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            tracker quit
            tracker showall categories
            tracker add_category
            tracker modify category
            tracker show transactions
            tracker add_transaction
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
    elif arglist[0]=="add_category":
        if len(arglist)!=1:
            print_usage()
        else:
            tracker =
    elif arglist[0]=="add_transaction":
        if len(arglist)!=1:
            print_usage()
        else:
    elif arglist[0]=="delete":
        if len(arglist)!=2:
            print_usage()
        else:
            



