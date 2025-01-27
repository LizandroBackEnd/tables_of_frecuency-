import math 
import textwrap 
 
## Fuctions the project  
def order_numbers(numbers): 
    return sorted(numbers) 
 
def calculate_absolute_frecuency(data):  
    intervals = {} 
    for number in data: 
        if number in intervals: 
            intervals[number] += 1 
        else: 
            intervals[number] = 1 
    return intervals  
 
def calculate_relative_frecuency(data): 
    absolute_frecuency = calculate_absolute_frecuency(data) 
    total = sum(absolute_frecuency.values()) 
    relative_frecuency = {} 
    for key, value in absolute_frecuency.items(): 
        relative_frecuency[key] = value / total 
    return relative_frecuency 
 
def calculate_accumulated_frecuency(data): 
    absolute_frecuency = calculate_absolute_frecuency(data) 
    accumulated_frecuency = {} 
    acum = 0 
    for key in sorted(absolute_frecuency.keys()): 
        acum += absolute_frecuency[key] 
        accumulated_frecuency[key] = acum 
    return accumulated_frecuency 
 
def calculate_relative_accumulated_frecuency(data): 
    absolute_frecuency = calculate_absolute_frecuency(data) 
    total = sum(absolute_frecuency.values()) 
    relative_frecuency = {} 
    for key, value in absolute_frecuency.items(): 
        relative_frecuency[key] = value / total 
    accumulated_frecuency = {} 
    acum = 0 
    for key in sorted(relative_frecuency.keys()): 
        acum += value 
        accumulated_frecuency[key] = acum 
    return accumulated_frecuency
  
## Generate table of frecuency 
def print_table(data):
    absolute_frecuency = calculate_absolute_frecuency(data)
    relative_frecuency = calculate_relative_frecuency(data)
    accumulated_frecuency = calculate_accumulated_frecuency(data)
    relative_accumulated_frecuency = calculate_relative_accumulated_frecuency(data)
    
    print("""
                                                Tabla de frecuencia
--------------------------------------------------------------------------------------------------------------
| Clase | Frecuencia Absoluta | Frecuencia Relativa | Frecuencia Acumulada | Frecuencia Relativa Acumulada |
--------------------------------------------------------------------------------------------------------------""")
    
    for key in sorted(absolute_frecuency.keys()):
        print(f"| {key:^5} | {absolute_frecuency[key]:^20} | {relative_frecuency[key]:^18.2f} | {accumulated_frecuency[key]:^19} | {relative_accumulated_frecuency[key]:^28.2f} |")
    
    total_absolute_frecuency = sum(absolute_frecuency.values())
    print("--------------------------------------------------------------------------------------------------------------")
    print(f"| {'Total':^5} | {total_absolute_frecuency:^20} | {'':^18} | {'':^19} | {'':^28} |")
    print("--------------------------------------------------------------------------------------------------------------")
  
data = [31, 28, 28, 31, 32, 31, 30, 31, 31, 27, 28, 29, 30, 32, 31, 30, 30, 30, 29 ,29, 30, 30, 31, 30, 31, 30, 31, 34, 32, 33, 29] ## Escribir tus numeros!!  

print_table(data) 
print("Numeros ordenados: ", order_numbers(data))
#orderre_data = order_numbers(data)
    
''' Testing the functions 
result = calculate_absolute_frecuency(data) 
print(result) 
result = calculate_relative_frecuency(data) 
print(result)   
result = calculate_accumulated_frecuency(data) 
print(result) 
result = calculate_relative_accumulated_frecuency(data) 
print(result) '''