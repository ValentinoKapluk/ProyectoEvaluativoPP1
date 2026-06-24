/*FUNCIONES*/
async function buscarProductoByNombre(query) {
    try {
        const response = await fetch(`${base_url}/productos?nombre=${query}`);
        const data = await response.json();
        return data
    } catch {
        const mensaje_error = "Algo salió mal";
        alert(mensaje_error)
    }
}
async function obtenerProductoById(id) {
    try {
        const response = await fetch(`${base_url}/productos/${id}`);
        const data = await response.json();
        return data
    } catch {
        const mensaje_error = "Algo salió mal";
        alert(mensaje_error)
    }
}
async function obtenerProductosAll() {
    try {
        const response = await fetch(`${base_url}/productos/all`);
        const data = await response.json();
        return data
    } catch {
        const mensaje_error = "Algo salió mal";
        alert(mensaje_error)
    }
}
function guardarFavoritos(producto) {
    const favoritos = JSON.parse(localStorage.getItem("favoritos") || "[]")

        let existe = false;
        favoritos.forEach(producto_fav => {
            if (producto_fav.id == producto.id) {
                existe = true;
                return;
            }
        });
        if (existe == false) {
            favoritos.push(producto)
            localStorage.setItem("favoritos", JSON.stringify(favoritos));
            console.log("guardado")
        }
        }
function sacarFavoritos(producto_id) {
    const favoritos = JSON.parse(localStorage.getItem("favoritos") || "[]")
    const producto_sacar_posicion = favoritos.findIndex((producto_fav) => {
        return producto_fav.id == producto_id;
    })
    favoritos.splice(producto_sacar_posicion, 1)
    localStorage.setItem("favoritos", JSON.stringify(favoritos));
    console.log("borrado")
    }
function mostrarProductos(lista) {
    const contenedor_productos = document.getElementById("productosContainer");
    contenedor_productos.innerHTML = "";
    lista.forEach((producto) => {
        contenedor_productos.innerHTML += `<div class="producto_container" data-id="${producto.id}" style="color:#fff; border: 3px solid #466eff; display:flex; justify-content:flex-start; width:600px; height:200px">
        <img src="${producto.imagen}" style="width:200px; object-fit: cover;">
        <div style="display:flex; align-items:center; padding:10px;">
        <ul>
        <li style="font-size:25px;">Producto: ${producto.nombre} (${producto.tipo_de_producto})</li>
        <li style="font-size:15px;;">Marca: ${producto.marca}</li>
        <li style="font-size:15px;">Precio: ${producto.precio}</li>
        <button class="boton-agregar" type="button" style="cursor:pointer; background-color:#466eff; color: #000; border: 0px solid black; margin-top: 20px;">❤️​ Agregar a Favoritos</button>
        </ul>
        </div>
        </div>`
    })
};
function mostrarFavoritos() {
    const favoritos_container = document.getElementById("favoritosContainer")
    favoritos_container.innerHTML = "";
    const favoritos = JSON.parse(localStorage.getItem("favoritos") || "[]")
    favoritos.forEach((producto) => {
        favoritos_container.innerHTML += `<div class="producto_container" data-id="${producto.id}" style="color:#000; border: 3px solid #466eff; display:flex; justify-content:flex-start; width:600px; height:200px;  background-color: #466eff;">
        <img src="${producto.imagen}" style="width:200px; object-fit: cover;">
        <div style="display:flex; align-items:center; padding:10px;">
        <ul>
        <li style="font-size:25px;">Producto: ${producto.nombre} (${producto.tipo_de_producto})</li>
        <li style="font-size:15px;;">Marca: ${producto.marca}</li>
        <li style="font-size:15px;">Precio: ${producto.precio}</li>
        <button class="boton-sacar" type="button" style="cursor:pointer; background-color:#000; color:#466eff; border: 0px solid white; margin-top: 20px;">​❌ ​Sacar de Favoritos</button>
        </ul>
        </div>
        </div>`
    })
}
function obtenerYmostrarFavoritos() {
    mostrarFavoritos()
    const favoritos_container = document.getElementById("favoritosContainer")
    favoritos_container.addEventListener("click", (event) => {
        const boton_sacar = event.target.closest(".boton-sacar")
        if (!boton_sacar) return;
        const container_especifico = boton_sacar.closest(".producto_container")
        const producto_id = Number(container_especifico.dataset.id)
        sacarFavoritos(producto_id);
})
}
async function obtenerYmostrarProductos() {
    const productos = await obtenerProductosAll()
    mostrarProductos(productos)

    const contenedor_productos = document.getElementById("productosContainer");

    contenedor_productos.addEventListener("click", async (event) => {
        const boton_agregar = event.target.closest(".boton-agregar")
        if (!boton_agregar) return;
        const container_especifico = boton_agregar.closest(".producto_container")
        const producto_id = Number(container_especifico.dataset.id)
        const producto = await obtenerProductoById(producto_id)
        const favoritos = JSON.parse(localStorage.getItem("favoritos") || "[]")
        guardarFavoritos(producto);
    })
}


/*VARIABLES*/
const buscador = document.getElementById("buscadorCaja");
const boton_buscador = document.getElementById("buscadorBoton");
const base_url = "http://127.0.0.1:8000";

/*CODIGO*/
obtenerYmostrarProductos()
    
boton_buscador.addEventListener("click", async () => {
    const query = buscador.value.trim();
    const productos_by_nombre = await buscarProductoByNombre(query)
    mostrarProductos(productos_by_nombre)
});

obtenerYmostrarFavoritos()