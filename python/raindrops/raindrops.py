def convert(number):
    drops = {3:"Pling", 5:"Plang", 7:"Plong"}
    result ="".join([drops[x] for x in range(1,8) if x in drops and (number%x==0)])
    return(result if result else str(number))
