from .Carrito import Carrito  # Asegúrate de ajustar el import según la ubicación de tu archivo Carrito

def total_carrito(request):
    total = 0
    carrito = Carrito(request)  # Instancia la clase Carrito con la request actual
    
    for key, value in carrito.carrito.items():
        total += value["acumulado"]
    
    return {"total_carrito": total}
