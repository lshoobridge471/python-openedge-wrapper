# Libreria con funciones para conectar ODBC OpenEdge y Python.

Es una libreria que funciona como wrapper a las funciones que nos provee pyodbc.

### Conexion por DSN o por Driver.
```
conn_kwargs = {
        "type_connection": 'DSN', # DSN o DRIVER
        "uid": 'sysprogress, # Usuario de la base
        "pwd": 'sysprogress', # Clave de la base
}
```
#### Para DSN:
```
conn_kwargs["dsn"] = 'odbcdsn'
```
#### Para driver:
```
conn_kwargs['driver_path'] = {/usr/dlc/odbc/lib/pgoe1023.so}
conn_kwargs["host"] = 'localhost'
conn_kwargs["port"] = 40000
conn_kwargs["dbname"] = dbname
```

### Ejecutamos la conexion al a OpenEdge.
```
conn = OpenEdgeConnector(**conn_kwargs)
```
## Metodos

### query(query)

Ejecutar una query. Ejemplo:
```
users = conn.query('SELECT * from PUB.usuarios')
```
### update(query)
Ejecutar un update (devuelve la cantidad de rows afectados).
```
updated = conn.update('UPDATE PUB.usuarios SET updated=1')
print("{} usuarios actualizados.".format(updated))
3 usuarios actualizados.
```
### fetchall(query, as_dict=False)
Traer un listado de datos dependiendo de una query.
users = conn.fetchall('SELECT TOP 10 * from PUB.usuarios', True)
```
print(users)
[
    {'name': 'Lucas', 'lastname': 'Shoobridge' },
    {'name': 'Javier', 'lastname': 'Palomino' }
]
```
El parametro ```as_dict``` en False hace que en vez de un diccionario sea una tupla lo que recibimos.

### fetchone(query, as_dict=False)
Traer un dato especifico dependiendo de una query.
```
user = conn.fetchone('SELECT TOP 1 * from PUB.usuarios', True)
print(user)
{'name': 'Lucas', 'lastname': 'Shoobridge' }
```

El parametro ```as_dict``` en False hace que en vez de un diccionario sea una tupla lo que recibimos.

# Creditos
Lucas Shoobridge - [shoobridgelucas@gmail.com](mailto:shoobridgelucas@gmail.com)