sum=0
n=3
for i in range(n):
    current_input = float(input(f'Ingrese voltaje {i+1}: '))
    sum += current_input
avg = sum/n
if avg<115:
    print(f'<VOLTAJE CORRECTO= {avg} V')
elif 115<=avg<=220:
    print(f'<ALTO VOLTAJE= {avg} V')
else:
    print(f'<PELIGRO= {avg} V')