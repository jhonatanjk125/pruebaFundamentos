sum=0
n=5
for i in range(n):
    current_input = float(input(f'Ingrese voltaje {i+1}: '))
    sum += current_input
avg = sum/n
if avg>220:
    print(f'<ALTO VOLTAJE= {avg}')
else:
    print(f'<VOLTAJE CORRECTO = {avg}')