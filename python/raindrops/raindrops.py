def convert(number):
    drops = {3: "Pling", 5: "Plang", 7: "Plong"}
    result = "".join([values for key, values in drops.items() if number % key == 0])
    return result or str(number)
