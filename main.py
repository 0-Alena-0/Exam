def calculate_bytes(string):
    # Преобразуем строку в байты, используя кодировку UTF-8, и затем определяем длину байтовой строки
    bytes_length = len(string.encode('utf-8'))
    return bytes_length

input_string = input("Введите строку: ")
bytes_length = calculate_bytes(input_string)

print(f"Длина строки в байтах: {bytes_length} байт")
