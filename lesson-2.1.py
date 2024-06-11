num_int = int(input("Enter a five digit number:"))

ones = (num_int // 1) % 10
tens = (num_int // 10) % 10
hundreds = (num_int // 100) % 10
thousands = (num_int // 1000) % 10
ten_thousands = (num_int // 10000) % 10

print(f"{ones}{tens}{hundreds}{thousands}{ten_thousands}")



