import json
import webbrowser
import re

#CARGAR archivo1.json, archivo2.json
lista = []
memoria = []
edades = []
promedios = []
nombres = []
edades = []
estados = []


def datos_edades():
    for e in memoria:
        ename = e["edad"]
        edades.append(ename)
    

def datos_promedios():
    for e in memoria:
        ename = e["promedio"]
        promedios.append(ename)
    

def datos_nombres():
    for e in memoria:
        ename = e["nombre"]
        nombres.append(ename)
    

def datos_estados():
    for e in memoria:
        ename = e["activo"]
        estados.append(ename)
    

def tamaño(lista):
    contador = 0
    for elemento in lista:
        contador+=1
    return contador


def leerJson(direccion):
    file = open(direccion)
    data = json.load(file)
    file.close()
    #for registro in data:
    #    print(registro)
    #print('caragado con exito')
    return(data)

while(True):
    cont=0
    entrada = input('Comando: ')
    entrada = entrada.replace(",", "")

    if re.match('[Cc][Aa][Rr][Gg][Aa][Rr]', entrada):
        memoria.clear()
        lista = entrada.split()
        for elemnt in lista:
            if elemnt.endswith('.json'):                
                dat = leerJson(elemnt)
                for regis in dat:
                    memoria.append(regis)
                    cont +=1
                    #print(regis)
        print("Cargado con exito")

    if re.match('[Mm][Aa][Xx][Ii][Mm][Oo]\s[Ee][Dd][Aa][Dd]', entrada):
        for e in memoria:
            ename = e["edad"]
            edades.append(ename)
        edades.sort()
        posicion = tamaño(edades)
        print("Edad maxima: ", edades[posicion - 1])
        edades.clear()

    if re.match('[Mm][Aa][Xx][Ii][Mm][Oo]\s[Pp][Rr][Oo][Mm][Ee][Dd][Ii][Oo]', entrada):
        for e in memoria:
            ename = e["promedio"]
            promedios.append(ename)
        promedios.sort()
        posicion = tamaño(promedios)
        print("Promedio maximo: ", promedios[posicion - 1])
        promedios.clear()
    
    if re.match('[Mm][Ii][Nn][Ii][Mm][Oo]\s[Ee][Dd][Aa][Dd]', entrada):
        for e in memoria:
            ename = e["edad"]
            edades.append(ename)
        edades.sort()
        print("Edad minima: ", edades[0])
        edades.clear()

    if re.match('[Mm][Ii][Nn][Ii][Mm][Oo]\s[Pp][Rr][Oo][Mm][Ee][Dd][Ii][Oo]', entrada):
        for e in memoria:
            ename = e["promedio"]
            promedios.append(ename)
        promedios.sort()
        print("Promedio minimo: ", promedios[0])
        promedios.clear()
        
    if re.match('[Ss][Uu][Mm][Aa]\s[Ee][Dd][Aa][Dd]', entrada):
        suma = 0
        for e in memoria:
            ename = e["edad"]
            suma = suma + int(ename)
        print('Suma de edades: ', suma)

    if re.match('[Ss][Uu][Mm][Aa]\s[Pp][Rr][Oo][Mm][Ee][Dd][Ii][Oo]', entrada):
        suma = 0
        for e in memoria:
            ename = e["promedio"]
            suma = suma + float(ename)
        print('Suma de promedios: ', round(suma,2))
                
    if re.match('[Cc][Uu][Ee][Nn][Tt][Aa]', entrada):
        print('Numero de registros: ', tamaño(memoria))

    if entrada.endswith('DONDE *'):
        hol = re.findall('nombre|edad|promedio|activo', entrada)
        for elemnt in memoria:
            for cad in hol:
                print(cad,': ', elemnt[cad])

    if re.match('[Ss][Ee][Ll][Ee][Cc][Cc][Ii][Oo][Nn][Aa][Rr]\s[*]', entrada):
        for ele in memoria:
            print('Nombre: ', ele["nombre"])
            print('Edad: ', ele["edad"])
            print('Promedio: ', ele["promedio"])
            print('Activo: ', ele["activo"])

    if re.match('[Ss][Ee][Ll][Ee][Cc][Cc][Ii][Oo][Nn][Aa][Rr]', entrada) and not(entrada.endswith('*')):
        #print(entrada)
        cahrl = entrada.split()
        atributo = cahrl[tamaño(cahrl) - 1]
        #print(atributo)
        hol = re.findall('nombre|edad|promedio|activo', entrada)
        del hol[-1]

        if entrada.endswith('"'):
            atributo = atributo.replace('"', '')
            for e in memoria:
                ename = e["nombre"]
                if ename == atributo:
                    for cad in hol:
                        print(cad,': ', e[cad])

        else:
            #print(atributo)
            #print(hol)
            for elm in memoria:
                name = elm["promedio"]
                #print(name)
                if float(atributo) == float(name) :
                    #print('bien')
                    for cad in hol:
                        print(cad,': ', elm[cad])

                
    
    if re.match('[Rr][Ee][Pp][Oo][Rr][Tt][Ee]\s[0-9]*', entrada):
       lis = entrada.split()
       N = 0
       N = int(lis[tamaño(lis) - 1])
       #print(N)
       datos_edades()
       datos_estados()
       datos_nombres()
       datos_promedios()

       
       with open('reporte.html', 'w') as reporte:
            reporte.write('<html>')
            reporte.write('<head>')
            reporte.write('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">')
            reporte.write('<body>')
            reporte.write('<center>')

            reporte.write('<table class="table table-hover">')

            reporte.write('<thead>')
            reporte.write('<tr>')
            reporte.write('<th scope="col">No.</th>')
            reporte.write('<th scope="col">Nombre</th>')
            reporte.write('<th scope="col">Edad</th>')
            reporte.write('<th scope="col">Activo</th>')
            reporte.write('<th scope="col">Promedio</th>')
            reporte.write('</tr>')
            reporte.write('</thead>')

            reporte.write('<tbody>')
            for ie in range(int(N)):
                valor = str(ie)
                #print(promedios[ie])
                reporte.write('<tr>')
                reporte.write('<th>' + str(ie + 1) + '</th>')
                reporte.write('<td class="active">' + str(nombres[ie]) + '</td>')
                reporte.write('<td class="success">' + str(edades[ie]) + '</td>')
                reporte.write('<td class="warning">' + str(estados[ie]) + '</td>')
                reporte.write('<td class="danger">' + str(promedios[ie]) + '</td>')
                reporte.write('</tr>')
            reporte.write('</tbody>')

            reporte.write('</table>')
            reporte.write('</center>')
            reporte.write('</body>')
            reporte.write('</html>')

            webbrowser.open('reporte.html')
            edades.clear()
            promedios.clear()
            nombres.clear()
            estados.clear()
        
    if re.match('[Ss][Aa][Ll][Ii][Rr]', entrada):
        exit()

       