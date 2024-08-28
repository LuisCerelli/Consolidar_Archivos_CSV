# Script para Consolidar Archivos CSV
Este script permite consolidar múltiples archivos .csv de la carpeta Input en un solo archivo, y exportar los datos combinados a un nuevo archivo .csv en la carpeta Output.

Project Root/<br>
├── Input/<br>
│   ├── file1.csv<br>
│   ├── file2.csv<br>
│   └── file3.csv<br>
├── Output/<br>
│   └── consolidados.csv<br>
├── script.py<br>
└── README.md<br>


### Cómo Funciona

#### El script realiza las siguientes acciones:

1. Importar las Bibliotecas Necesarias:

  - pandas se utiliza para la manipulación de datos.
  - glob se utiliza para buscar y recuperar la lista de archivos .csv en el directorio especificado.
  
2. Buscar Archivos CSV:

  - El script busca todos los archivos .csv que se encuentran en el directorio Input/.
  - Almacena los nombres y rutas de estos archivos en una lista.
    
3. Carga y Combinación de Datos:

  - Para cada archivo .csv encontrado, lee los datos en un DataFrame de pandas.
  - Luego, los datos se agregan a una lista de DataFrames.
4. Concatenación de los Datos:

  - El script concatena todos los DataFrames en uno solo, asegurando un índice continuo entre las filas.
5. Exportación a CSV:

  - Finalmente, el DataFrame consolidado se guarda como un nuevo archivo .csv en la carpeta Output/, usando un punto y coma (;) como delimitador.
