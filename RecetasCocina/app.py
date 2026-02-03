from flask import Flask, render_template, request

app = Flask(__name__)

# Datos de ejemplo (simulan una base de datos)
recetas = [
    {
        "nombre": "Tacos al pastor",
        "descripcion": "Deliciosos tacos con carne adobada y piña."
    },
    {
        "nombre": "Enchiladas verdes",
        "descripcion": "Enchiladas rellenas de pollo con salsa verde."
    },
    {
        "nombre": "Pastel de chocolate",
        "descripcion": "Pastel esponjoso ideal para cualquier ocasión."
    }
]

@app.route("/")
def index():
    return render_template("index.html", recetas=recetas)

@app.route("/buscar")
def buscar():
    texto = request.args.get("q", "").lower()
    resultados = [
        r for r in recetas
        if texto in r["nombre"].lower()
    ]
    return render_template("index.html", recetas=resultados)

if __name__ == "__main__":
    app.run(debug=True)
