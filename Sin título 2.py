import shelve

def abrirArch(ruta):    
    return shelve.open(ruta)

ruta=("nuevoarchivo.dat")
abrirArch(ruta)