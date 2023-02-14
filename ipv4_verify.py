print("This program takes an IPv4 address as input and tells you whether it is a valid IPv4 address or not. Please enter your IPv4 address now...")
IP = input()

bytes = IP.split(".")

int_bytes = []

for byte in bytes:
    byte = int(byte)
    int_bytes.append(byte)

correct_bytes = 0

for n in int_bytes:
    if n >= 0 and n <= 255:
         correct_bytes = correct_bytes + 1
   
if len(range(correct_bytes)) == 4:
    print("This is a valid IP address.")
else:    
    print("This is not a valid IP address.")

