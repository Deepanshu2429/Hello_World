



def contactCorrection(number,country):
    number=str(number).replace(" ","")

    if country.lower()=='india':
        if len(number)  >10:
            number = number[-10:]
            number='91'+ str(number) 
            #print(number)
            return number
        else: 
            return number

    else:
        return number

