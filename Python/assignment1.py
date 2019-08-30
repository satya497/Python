# printing The amount of money billed to the customer 
def billing(code,begin_read,end_read):
    if begin_read <= end_read :
        gallons = (end_read-begin_read)/10
        if code in ['r','R']:
            amount=(gallons*0.0005)+5   
        elif code in ['c','C']:
            if gallons <= 4000000:
                print(gallons)
                amount= 1000    
            else:
                gallons = gallons-4000000
                amount= (extragallons*0.00025)+1000
        elif code in ['i','I']:
            if gallons <=4000000:
                amount=1000
            elif gallons > 4000000 and gallons < 100000000:
                amount=2000
            else:
                gallons = gallons-10000000
                amount = (gallons*0.00025)+2000
    else:
        gallons = ((1000000000 - begin_read)+end_read)/10
        if code in ['r','R']:
            amount=(gallons*0.0005)+5
            
        elif code in ['c','C']:
            if gallons <= 4000000:
                amount= 1000
                
            else:
                gallons = gallons-4000000
                amount= (extragallons*0.00025)+1000
        elif code in ['i','I']:
            if gallons <=4000000:
                amount=1000
            elif gallons > 4000000 and gallons <= 100000000:
                amount=2000
            else:
                gallons = gallons-10000000
                amount = (gallons*0.00025)+2000

    return gallons,amount
def start():
    in_code = input("Enter The customer's code (a character) : ")
    if in_code not in ["r",'c',"i",'R','C','I']:
        return
    else:
        in_beginRead=int(input("Enter The beginning meter reading (a positive integer value) :"))
        in_endRead=int(input("The customer's ending meter reading (a positive integer value) :"))
        gallons,amount = billing(in_code,in_beginRead,in_endRead)

        print("The customer's beginning meter reading : ",in_beginRead)
        print("The customer's ending meter reading : ",in_endRead)
        print("The gallons of water used by the customer : ",gallons)
        print("The amount of money billed to the customer  : $",amount)
start()