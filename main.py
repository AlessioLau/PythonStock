import sqlite3

# Variables globales       
db = sqlite3.connect('stock.sqlite')
cursor = db.cursor()
op_final = 's'
nombre_usuario = ''

def resetear_tabla():
    cursor.execute('DROP TABLE IF EXISTS productos')
    cursor.execute('CREATE TABLE productos (id INTEGER PRIMARY KEY, nombre TEXT, cantidad INTEGER, precio INTEGER)')
    db.commit()

def insertar_producto(nombre, cantidad, precio):
    cursor.execute('INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)', (nombre, cantidad, precio))
    db.commit()

def mostrar_productos():
    print('Productos: \nID Nombre Cantidad Precio')
    cursor.execute('SELECT id, nombre, cantidad, precio FROM productos')
    for fila in cursor:
        print(' '.join(map(str, fila)))

def mostrar_producto_especifico(nombre):
    cursor.execute('SELECT id, nombre, precio FROM productos WHERE nombre = ?', (nombre,))
    for fila in cursor:
        print(f'ID: {fila[0]}, Nombre: {fila[1]}, Precio: {fila[2]}')

def modificar_atributos(id_producto, nuevos_atributos):
    update_query = 'UPDATE productos SET ' + ', '.join([f'{clave} = ?' for clave in nuevos_atributos.keys()]) + ' WHERE id = ?'
    cursor.execute(update_query, list(nuevos_atributos.values()) + [id_producto])
    db.commit()

def main():
    op = 'a'
    menu = '\n(1) Reiniciar tabla productos'\
           '\n(2) Insertar producto'\
           '\n(3) Mostrar productos'\
           '\n(4) Mostrar producto especifico'\
           '\n(5) Modificar atributos de un producto'\
           f'\n({op_final}) Para salir: '
    print('\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
          f'\nBuen dia {nombre_usuario} ¿que queres hacer?'
          '\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

    while op != op_final:
        op = input(menu)

        if op == '1':
            resetear_tabla()

        elif op == '2':
            nombre = input('Ingrese el nombre del producto: ')
            cantidad = int(input('Ingrese la cantidad: '))
            precio = int(input('Ingrese el precio: '))
            insertar_producto(nombre, cantidad, precio)

        elif op == '3':
            mostrar_productos()

        elif op == '4':
            nombre = input('Ingrese el nombre del producto: ')
            mostrar_producto_especifico(nombre)

        elif op == '5':
            id_producto = int(input('Ingrese el ID del producto que desea modificar: '))
            nuevos_atributos = {}
            nuevos_atributos['nombre'] = input('Nuevo nombre: ')
            nuevos_atributos['cantidad'] = int(input('Nueva cantidad (deje en blanco para mantener la actual): ') or -1)
            nuevos_atributos['precio'] = int(input('Nuevo precio (deje en blanco para mantener el actual): ') or -1)
            modificar_atributos(id_producto, {k: v for k, v in nuevos_atributos.items() if v != -1})

        elif op == op_final:
            print('\n' + '=' * 12)
            print('Hasta luego')
            print('=' * 12)
        else:
            error('Error. Ingresa un valor valido')

if __name__ == '__main__':
    main()
