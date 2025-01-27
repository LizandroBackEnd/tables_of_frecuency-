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
        acum += relative_frecuency[key] 
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
    
    print("--------------------------------------------------------------------------------------------------------------")
  
data = [2, 3, 4, 1, 5, 0, 1, 1, 1, 5, 2, 2, 3, 2, 2, 2, 1, 0, 1, 3, 1, 3, 4, 1, 1, 2, 3] ## Escribir tus numeros!!  

result = calculate_absolute_frecuency(data) 
print(result) 
 
result = calculate_relative_frecuency(data) 
print(result)   
 
result = calculate_accumulated_frecuency(data) 
print(result) 
 
result = calculate_relative_accumulated_frecuency(data) 
print(result) 
 
print_table(data)