#Receba uma temperatura em farenheit e converta para celsius

farenheit = float(input('Digite a temperatura em Farenheit:'))

c = (farenheit - 32) / 1.8

print(f'A temperatura em Celsius é: {c:.2f}°C')