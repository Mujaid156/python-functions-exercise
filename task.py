def hotel_cost(nights):
    return nights*140


def plane_ride_cost(city):
    if "capetown" == city:
        return 2500
    elif "durban" == city:
        return 2300
    elif "jhb" == city:
        return 2000
    elif "bfn" == city:
        return 1800

    # defining a rental car cost
    # cost is in rands
def rental_car_cost(days):
    car_cost = 40 * days

    if days >= 7:
        car_cost = car_cost - 50

    elif days >= 3 and days < 7:
        car_cost = car_cost - 20
    return car_cost


def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money


location = input("Where did you go: ")
days = int(input("How many days did you stay: "))
extras = float(input("How much did spend on extras: "))

print(trip_cost("bfn", 2, 1000))

