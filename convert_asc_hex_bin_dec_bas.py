import base64

# Prompt user for input type
input_type = input("Enter the input type - 3 char- (ascii, hex, binary, decimal, base64): ")

# Prompt user for input string
input_string = input("Enter the input string: ")

# Convert input string to bytes based on input type
if input_type == "asc":
    input_bytes = input_string.encode('ascii')
elif input_type == "hex":
    input_bytes = bytes.fromhex(input_string)
elif input_type == "bin":
    input_bytes = int(input_string, 2).to_bytes((len(input_string) + 7) // 8, byteorder='big')
elif input_type == "dec":
    input_bytes = int(input_string).to_bytes((int(input_string).bit_length() + 7) // 8, byteorder='big')
elif input_type == "bas":
    input_bytes = base64.b64decode(input_string)

# Prompt user for output type
output_type = input("Enter the output type - 3 char- (ascii, hex, binary, decimal, base64): ")

# Convert bytes to output string based on output type
if output_type == "asc":
    output_string = input_bytes.decode('ascii')
elif output_type == "hex":
    output_string = input_bytes.hex()
elif output_type == "bin":
    output_string = ''.join(format(byte, '08b') for byte in input_bytes)
elif output_type == "dec":
    output_string = int.from_bytes(input_bytes, byteorder='big')
elif output_type == "bas":
    output_string = base64.b64encode(input_bytes).decode()

# Display the output string
print("Output string: ", output_string)

