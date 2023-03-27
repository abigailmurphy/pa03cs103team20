from transaction import Transaction
import sys


def print_usage():
    ''' print an explanation of how to use this command '''
    print('''usage:
            tracker quit
            tracker showall categories  
            tracker add_category (item_num, new_category)
            tracker modify category (old category, new category)
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
    ''' print the tracker items  ~monica ~aria'''
    if len(trackers)==0:
        print('no records to print')
        return
    print('\n')
    print("%-10s %-10s %-10s %-15s %-20s"%('item_num','amount','category','date', 'description'))
    print('-'*60)
    for item in trackers:
        values = tuple(item.values()) #(item_num,amount,category,date,description)
        print("%-10d %-10d %-10s %-15s %-20s"%(values))

def print_category_trackers(trackers):
    ''' print the summary tracker items  ~aria'''
    if len(trackers)==0:
        print('no tasks to print')
        return
    print('\n')
    print("%-10s"%('category'))
    print('-'*20)
    for item in trackers:
        values = tuple(item.values()) #(category)
        print("%-10s"%(values[0]))
        
def process_args(arglist):
    transaction = Transaction('tracker.db')
    ''' examine args and make appropriate calls to Transaction ~monica ~aria'''
    if arglist==[]:
        print_usage()
        
    elif arglist[0]=="showall":  #shows all the categories
        print_category_trackers(trackers = transaction.distinct_categories())
        
    elif arglist[0]=="add_category":   #adds the category 
        if len(arglist)!=2:
            print_usage()
        else:
            item = int(arglist[1])
            cat = arglist[2]
            transaction.add_category(item, cat)
    
    elif arglist[0]=="modify":  #modifys the category
        if len(arglist)!=3:
            print_usage()
        else:
            transaction.modify_category(arglist[1], arglist[2])
            
    elif arglist[0]=="show": #shows the transactions 
        print_trackers(trackers=transaction.select_all())

    elif arglist[0]=="add_transaction":  #adds the transactions 
        if len(arglist)!= 6:
            print_usage()
        else: 
            item_num = int(arglist[1])
            amount = float(arglist[2])
            cat = arglist[3]
            date = arglist[4]
            desc = arglist[5]
            transaction.add_transaction({'item_num': item_num, 'amount': amount, 'category': cat, 'date': date, 'description': desc})
            
    elif arglist[0]=="delete": #deletes the transaction
        if len(arglist)!=2:
            print_usage()
        else:
            transaction.delete_transaction(int(arglist[1]))
          
    elif arglist[0]=="summarize": 
        if len(arglist)!=2:
             print_usage()
        elif arglist[1]=="by_date":   #summarize by date 
            print_trackers(trackers = transaction.by_date())
        elif arglist[1]=="by_month":  #summarize by month
            print_trackers(trackers = transaction.by_month())
        elif arglist[1]=="by_year":   #summarize by year
            print_trackers(trackers = transaction.by_year())
        elif arglist[1]=="by_category": #summarize by category
            print_trackers(trackers = transaction.distinct_categories())
        else:
            print_usage()
            
    elif arglist[0]=="quit":  #exits the program 
        sys.exit()
        
    else:
        print_usage()
        
        
def toplevel():
    ''' read the command args and process them'''
    if len(sys.argv)==1:
        # they didn't pass any arguments, 
        # so prompt for them in a loop
        print_usage()
        args = []
        while args!=['']:
            args = input("command> ").split(' ')
            if args[0]=='add':
                # join everyting after the name as a string
                args = ['add',args[1]," ".join(args[2:])]
            process_args(args)
            print('-'*40+'\n'*3)
    else:
        # read the args and process them
        args = sys.argv[1:]
        process_args(args)
        print('-'*40+'\n'*3)

toplevel()

