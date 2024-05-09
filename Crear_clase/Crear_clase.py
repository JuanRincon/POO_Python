# Uso de Get y set

# Creamos una clase
class producto:

    def __init__(self, costo):
        self._costo=costo

        # Invocamos un método de la propia clase
        self._precioventa=self._calculaPVenta()
        
    # Este método se cinsidera privado
    def _calculaPVenta(self):
        return self._costo*1.30
    
    # Creamos el getter para el atributo precioventa
    def getPrecioVenta(self):
        return self._precioventa
    
    # Creamos el setter para el atributo costo
    def setCosto(self, valor):
        
        # Podemos colocar codigo de seguridad
        if(valor>0):
            self._costo=valor
            self._precioventa=self._calculaPVenta()
        else:
            print("Valor invalido")
            self._costo=0
            
    # Creamos el getter del atributo costo
    def getCosto(self):
        return self._costo
    
    # Usamos __repr__ para facilitarnos la impresión
    def __repr__(self):
        return f'Costo=${self._costo}, Precio venta=${self._precioventa}'
    
# Creamos el objeto
manzana=producto(12.5)

# imprimimos
print(manzana)

# Obtenemos el precio de venta
pv=manzana.getPrecioVenta()
print('El impuesto es $', pv*0.16)

# Modificamos el costo
manzana.setCosto(11.10)

# Obtenemos el costo
print(manzana.getCosto())

# Imprimimos el objeto
print(manzana)
