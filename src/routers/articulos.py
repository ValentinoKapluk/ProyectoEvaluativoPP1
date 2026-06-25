#IMPORTS
from fastapi import APIRouter
from fastapi import Path, Query, Body
from fastapi import HTTPException
from schemas.articulos import ProductoSchema
from schemas.articulos import ProductoUpdateSchema
from typing import Annotated
router = APIRouter()

#BASE DE DATOS
productos = [
    {"id":1, "nombre":"Guitarra Electrica","tipo_de_producto":"Instrumento", "marca":"Mirrs","precio": 1500000,"imagen":"https://heavenstorage.blob.core.windows.net/storageheavenimagenes/717aa2b5-554f-4767-979d-3dbbfb895e9d/images/v2/MIRRS/41712_xlarge.jpg?sp=r&st=2025-06-19T02:11:26Z&se=2035-06-19T10:11:26Z&spr=https&sv=2024-11-04&sr=c&sig=JTrpEXutEZPdfvCaeQXMhkVlHyRxzKHHZRKwJAxxoq8%3D"},
    {"id":2, "nombre": "Teclado","tipo_de_producto":"Instrumento", "marca":"Yamaha","precio": 1250000,"imagen":"https://tiendafeedback.com.ar/74065-large_default/teclado-yamaha-psre383-5-octavas-sensitivo-.webp"},
    {"id":3, "nombre": "Paquete de Cuerdas","tipo_de_producto":"Accesorio", "marca":"Elixir","precio": 30000,"imagen":"https://hendrix.com.ar/wp-content/uploads/2025/02/ELIXIR-16027.png"},
    {"id":4, "nombre": "Capo de Guitarra","tipo_de_producto":"Accesorio", "marca":"Capos","precio": 10000,"imagen":"https://musicshaker.com.ar/wp-content/uploads/2022/06/D_903811-MLA47206123608_082021-F.jpg"},
    {"id":5, "nombre": "Batería","tipo_de_producto":"Instrumento", "marca":"Tama","precio":1500000,"imagen":"https://acdn-us.mitiendanube.com/stores/001/647/449/products/facd6e5e-226a-4c89-93df-d47bb9300937-107149856fa126f62317412874306561-1024-1024.webp"},
    {"id":6, "nombre": "Batería Electrica","tipo_de_producto":"Instrumento", "marca":"Yamaha","precio":2000000,"imagen":"https://acdn-us.mitiendanube.com/stores/006/021/291/products/d_nq_np_800742-mla81770850358_012025-f-9705d8411e975e5bee17531921796173-1024-1024.webp"},
    {"id":7, "nombre": "Baquetas","tipo_de_producto":"Accesorio", "marca":"Vic Firth","precio":20000,"imagen":"https://tiendafeedback.com.ar/60601-large_default/palillos-vic-firth-5b-american-classic-baquetas-punta-madera-.jpg"},
    {"id":8, "nombre": "Guitarra Electrica","tipo_de_producto":"Instrumento", "marca":"Fender","precio":2000000,"imagen":"https://dcdn-us.mitiendanube.com/stores/001/040/912/products/014-4502-5001-b323e79bbfc7f233c615981106592656-1024-1024.webp"},
    {"id":9, "nombre": "Guitarra Acustica","tipo_de_producto":"Instrumento", "marca":"Fender","precio":800000,"imagen":"https://acdn-us.mitiendanube.com/stores/003/928/657/products/img-1-deda4c885cf8d416c017038625329991-1024-1024.jpg"},
    {"id":10, "nombre": "Teclado","tipo_de_producto":"Instrumento", "marca":"Casio","precio":1000000,"imagen":"https://images.fravega.com/f1000/a58157052a547ef130f9d818d5ab2888.jpg"},
]




#PATH OPERATIONS
#Mostrar todos los productos
@router.get("/productos/all", response_model=list[ProductoSchema])
async def productos_all() -> list[ProductoSchema]:
    return productos

#Mostrar producto especifico por id
@router.get("/productos/{id}",  response_model=ProductoSchema)
async def obtener_producto_by_id(id: Annotated[int, Path(gt=0, lt=1000)]) -> ProductoSchema:
    for producto in productos:
        if id == producto["id"]:
            return producto
    raise HTTPException(
        status_code=404, detail="No se encontro el producto buscado")

#Mostrar productos filtrados por nombre
@router.get("/productos", response_model=list[ProductoSchema])
async def productos_by_nombre(nombre: Annotated[str, Query(min_length=1, max_length=50)]) -> list[ProductoSchema]:
    mostrar_productos = []
    for producto in productos:
        if nombre == producto["nombre"]:
            mostrar_productos.append(producto)
    return mostrar_productos

#Agregar un nuevo producto a productos
@router.post("/productos/nuevo", response_model=ProductoSchema)
async def nuevo_producto(producto:ProductoSchema) -> ProductoSchema:
    existe = False
    for productoBD in productos:
        if productoBD["id"] == producto.id:
            existe = True
            raise HTTPException(status_code=400, detail="El producto a agregar ya existe")
            break
        else:
            existe = False
    if existe == False:
        productos.append(dict(producto))
        return producto

#Actualizar un producto
@router.put("/productos/actualizar",  response_model=ProductoSchema)
async def actualizar_producto(
    producto_id: Annotated[int, Body(gt=0)], 
    producto_editado: ProductoUpdateSchema) -> ProductoSchema:
    for producto in productos:
        if producto["id"] == producto_id:
            producto["nombre"] = producto_editado.nombre
            producto["tipo_de_producto"] = producto_editado.tipo_de_producto
            producto["marca"] = producto_editado.marca
            producto["precio"] = producto_editado.precio
            producto["imagen"] = producto_editado.imagen
            return producto
    raise HTTPException(status_code=404, detail="No se encontro el producto buscado")

#Borrar producto de productos
@router.delete("/productos/borrar", response_model= ProductoSchema)
async def borrar_producto(producto_id: Annotated[int, Body(gt=0)]) -> ProductoSchema:
    for producto in productos:
        if producto["id"] == producto_id:
            productos.remove(producto)
            return producto
    raise HTTPException(status_code=404, detail="No se encontro el producto buscado")


