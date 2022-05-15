# Web Scrapping


###### rpad


## Descripción
El proyecto, que está dividido en 4 programas junto con un archivo de texto el cual contiene los links con los que se va a trabajar, tiene como objetivo buscar información, eventos, imágenes y noticias sobre Sergio Pérez, para después recopilar todo lo anterior en un archivo de excel.

## Instalación
Antes de poder pasar a usar los programas es necesario contar con las siguientes librerías y módulos instalados: 

Librerías:

-re

-requests

-json

-openpyxl

Módulos:

-io

-os

-bs4

-datetime

Método de instalación:

`pip install name`

Una vez instalado todo lo anterior, se van importará en los programas y ahora sí se podrá ejecutar todo en orden 

## Uso 
Para ejecutar el programa se debe contar con el archivo links.txt
El programa principal, que es con el que se trabaja, es *main.py*

Al ejecutarlo, lo primero que se nos va a preguntar es si deseamos agregar un nuevo link al archivo link.txt con el que ya contamos. Si ponemos que si, podremos ingresar los links que deseamos añadir. En el caso de no querer agregar ninguno, el programa comenzará con la búsqueda y recoplación de información, así como a la generación del excel y la descarga de las imágenes.

main.py mandará a llamar funcones de scrapping.py para buscar la información del deportista, redes sociales, noticias y victorias, así como sus 3 próximos eventos. De la misma manera, descargará 3 imagenes y las meterá en una carpeta llamada Imagenes_Checo_Perez. 
Después de lo anterior, mandará a llamar al programa weather.py para obtener la temperatura máxima y mínima que habrá en los 3 eventos próximos que recopilamos.
Por último, se creará un archivo en excel con la ayuda de la función que se encuentra en xls.py, la cual crea el archivo de excel, toma los valores ingresados en la función y los acomoda dentro del archivo

Tras haber creado el archivo de excel, se nos mostrará un mensaje de que el programa fue ejecutado de manera satisfactoria (puesto que la información ya está vaciada en el archivo) y se nos preguntará si deseamos eliminar el archvio de excel creado. Ya sea que elijamos que si o no, el programa finalizará su ejecución.

