# 201906053_PracticaUnicaLFP
## Manual de Usuario SimpleSQL
Este proyecto se basa en la carga de registros en formato json, los cuales deben poseer una estructura como la de este [ejemplo], los cuales pueden ser 
consultados de una manera simple sin tener que recorrer registro por registro, este consta de diferentes comandos los cuales realizan una accion
en especifico y los cuales se explican en este manual para el funcionamiento correcto del programa. Los comandos se deben ingresar en la consola de ejecucion de la aplicacion
y como primer punto se deben tener N archivos en formato json los cuales deben contener N registros con 4 atributos cada uno los cuales deben ser nombre, edad, promedio y activo,
nombre debe ser un tipo de dato string, edad debe ser un tipo de dato int, promedio debe ser un tipo de dato float y activo debe ser un tipo de dato booleano. Los archivos deben
estar guardados en la misma direccion del proyecto sino este no encontrara los archivos a cargar y al empezar la ejecucion del programa se debe ingresar el comando
CARGAR, el cual se explica mas adelante, ya que si la memoria del programa esta vacia no se podra ejecutar ningun otro comando.

### Comandos: estos son las instrucciones las cuales se les pueden dar al programa y su uso y sintaxis se explica acontinuacion

1. ___Cargar___: el comando cargar realiza la carga de diferentes archivos a la memoria del programa para
su posterior consulta, este debe de ser el primer comando a ejecutar, este se debe escribir en la consola
de la siguiente manera:
    - CARGAR archivo1, archivo2, ... archivoN
    - Ej. cargado con exito

    
2. ___Seleccionar___: el comando seleccionar devuelve en pantalla uno o muchos atributos especificos de un registro,
este posee diferentes comandos con diferente funcion:
    - SELECCIONAR *
    - Nota: el uso de * devuelve todos los atributos de todos los registros
    - SELECCIONAR nombre promedio DONDE nombre = "jon"
    - Nota: el uso de 'DONDE' devuelve todos los atributos escritos en consola del registro que coincida con el dato proporcionado en consola, este puede ser el nombre que posee un registro o el promedio de un registro.
    - Ej. nombre = juanito
    
3. ___Maximo___: el comando maximo devuelve en pantalla el valor maximo de el atributo edad o promedio de todos los registros cargados en memoria, se debe ingresar en consola de la siguiente forma:
    - MAXIMO edad
    - Ej. edad maxima = 16

4. ___Minimo___: el comando minimo devuelve en pantalla el valor maximo de el atributo edad o promedio de todos los registros cargados en memoria, se debe ingresar en consola de la siguiente forma:
    - MINIMO edad
    - Ej. edad minima = 16
    
5. ___Suma___: el comando suma devuelve en pantalla el valor de la suma de los atributos edad o promedio de todos los registros cargados en memoria, se debe ingresar en consola de la siguiente forma:
    - SUMA edad
    - Ej. suma de edades = 20
    
6. ___Cuenta___: el comando cuenta devuelve en pantalla el numero de registros los cuales estan cargados en memoria, se debe ingresar en consola de la siguiente manera:
    - CUENTA
    - Ej. Numero de registros = 2
    
7. ___Reporte___: el comando reporte muestra en su navegador una tabla de registros en html donde se debe especificar el valor de registros los cuales se desean ver en el reporte siempre y cuando este no exceda el 
numero de registros cargados en memoria, se debe ingresar en consola de la siguiente manera:
    - REPORTE 7
    
8. ___Salir___: el comando salir termina la ejecuacion de la aplicacion y debe ser ingresado de la siguiente manera:
    - SALIR
    
[ejemplo]: https://drive.google.com/file/d/11P9Ms_1mJw5y6JSreRBsOOPOWhPQe3Yt/view?usp=sharing
