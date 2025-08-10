def calculate_trip_cost(hotel_per_day,num_days,plane_cost,vehichle_cost):
    hotel_total = hotel_per_day * num_days
    total_cost = hotel_total+plane_cost+vehichle_cost
    return total_cost
hotel_per_day = int(input("Enter hotel cost per day: "))
num_days = int(input("Enter number of days: "))
plane_cost = int(input("Enter the plane ticket cost: "))
vehichle_cost = int(input("Enter the vehichle cost: "))
total = calculate_trip_cost(hotel_per_day,num_days,plane_cost,vehichle_cost)
print("total trip expenditure",total)