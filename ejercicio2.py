side = float(input('Ingrese el lado del triángulo equilatero: '))
area = ((3**(1/2)/4))*side*side
if area>1000:
    print('<DATOS NO VALIDOS=')
else:
    print(f'<EL AREA DEL TRIÁNGULO ES: {area}')