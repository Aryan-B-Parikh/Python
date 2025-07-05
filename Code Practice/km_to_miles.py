def km_to_miles():
    print("🚗 Kilometers to Miles Converter")
    km = float(input("Enter distance in kilometers: "))
    miles = km * 0.621371
    print(f"{km} km is equal to {miles:.2f} miles")

if __name__ == "__main__":
    km_to_miles()
