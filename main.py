def calculate_bytes(string):
    bytes_length = len(string.encode('utf-8'))
    return bytes_length

input_string = input("Введите строку: ")
bytes_length = calculate_bytes(input_string)

print(f"Длина строки в байтах: {bytes_length} байт")
