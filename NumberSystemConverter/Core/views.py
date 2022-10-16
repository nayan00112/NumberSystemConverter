from django.shortcuts import render

# Create your views here.

def Core(request):
    if request.method == 'POST':
        value = request.POST['InputNumber']
        valueType = request.POST['nsys']

        if valueType == "Decimal":
            value = int(value)
            objects = {
                'decValue': value,
                'binaryValue' : bin(value)[2:],
                'octValue' : oct(value)[2:],
                'hexValue' : hex(value)[2:],
            }
            # print(objects)
            return render(request, 'index.html', objects)
        else:
            if valueType == "Binary":
                n = 2
            if valueType == "Octal":
                n = 8
            if valueType == "Hexadecimal":
                n = 16

            try:
                value = int(value, n)
                objects = {
                    'decValue': value,
                    'binaryValue' : bin(value)[2:],
                    'octValue' : oct(value)[2:],
                    'hexValue' : hex(value)[2:],
                }
            except:
                objects = {
                    'error': "invalid literal"
                }
            # print(objects)
            return render(request, 'index.html', objects)            
    else:
        return render(request, 'index.html')
