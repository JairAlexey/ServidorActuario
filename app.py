from flask import Flask, request, jsonify
import os
import pandas as pd
from fpdf import FPDF

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar directorio para guardar archivos
GENERATED_FILES_DIR = os.path.expanduser("~/Desktop/Archivos_Generados_GPT")
os.makedirs(GENERATED_FILES_DIR, exist_ok=True)

# Ruta para verificar que el servidor está funcionando
@app.route('/', methods=['GET'])
def home():
    return "¡El servidor está funcionando correctamente!"

# Endpoint 1: Recibir datos iniciales
@app.route('/submit-initial-data', methods=['POST'])
def submit_initial_data():
    try:
        data = request.json
        if not all(k in data for k in ["normativa", "empresa", "ejercicio", "saldo_jubilacion", "saldo_desahucio"]):
            return jsonify({"error": "Faltan datos necesarios en la solicitud"}), 400

        # Guardar los datos iniciales en un archivo JSON
        file_path = os.path.join(GENERATED_FILES_DIR, "datos_iniciales.json")
        with open(file_path, 'w') as f:
            f.write(str(data))

        return jsonify({"message": "Datos iniciales recibidos y guardados", "file": file_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint 2: Generar cálculos actuariales
@app.route('/generate-actuarial-calculations', methods=['POST'])
def generate_actuarial_calculations():
    try:
        # Leer datos iniciales
        input_file = os.path.join(GENERATED_FILES_DIR, "datos_iniciales.json")
        if not os.path.exists(input_file):
            return jsonify({"error": "Datos iniciales no encontrados"}), 404

        # Procesar los cálculos actuariales (simulado)
        result = [
            {"concepto": "Cálculo 1", "resultado": 150000},
            {"concepto": "Cálculo 2", "resultado": 75000}
        ]

        # Guardar los cálculos en un archivo Excel
        file_path = os.path.join(GENERATED_FILES_DIR, "calculos_actuariales.xlsx")
        df = pd.DataFrame(result)
        df.to_excel(file_path, index=False)

        return jsonify({"message": "Cálculos actuariales generados", "file": file_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint 3: Generar anexos en Excel
@app.route('/generate-excel-annexes', methods=['POST'])
def generate_excel_annexes():
    try:
        # Generar archivos Excel con los anexos
        jub_file = os.path.join(GENERATED_FILES_DIR, "anexos_jubilacion.xlsx")
        des_file = os.path.join(GENERATED_FILES_DIR, "anexos_desahucio.xlsx")

        # Ejemplo: Datos para jubilación
        jub_data = {
            "Anexo 1": ["Resultado 1", "Resultado 2"],
            "Anexo 2": ["Detalle 1", "Detalle 2"],
            "Anexo 3": ["Salida 1", "Salida 2"]
        }
        pd.DataFrame(jub_data).to_excel(jub_file, index=False)

        # Ejemplo: Datos para desahucio
        des_data = {
            "Anexo 1": ["Resultado A", "Resultado B"],
            "Anexo 2": ["Detalle A", "Detalle B"],
            "Anexo 3": ["Salida A", "Salida B"]
        }
        pd.DataFrame(des_data).to_excel(des_file, index=False)

        return jsonify({"message": "Anexos Excel generados", "files": [jub_file, des_file]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint 4: Revisar anexos en Excel
@app.route('/review-annexes', methods=['POST'])
def review_annexes():
    try:
        # Verificar la existencia de los anexos
        jub_file = os.path.join(GENERATED_FILES_DIR, "anexos_jubilacion.xlsx")
        des_file = os.path.join(GENERATED_FILES_DIR, "anexos_desahucio.xlsx")

        if os.path.exists(jub_file) and os.path.exists(des_file):
            return jsonify({
                "message": "Anexos disponibles para revisión",
                "files": [jub_file, des_file]
            })
        else:
            return jsonify({"error": "Anexos no encontrados"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint 5: Generar informe final en PDF
@app.route('/generate-final-report', methods=['POST'])
def generate_final_report():
    try:
        file_path = os.path.join(GENERATED_FILES_DIR, "informe_final.pdf")
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt="Informe Final Actuarial", ln=True, align='C')
        pdf.output(file_path)

        return jsonify({"message": "Informe final generado", "file": file_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint 6: Generar asientos contables
@app.route('/generate-accounting-entries', methods=['POST'])
def generate_accounting_entries():
    try:
        # Generar archivo Excel con asientos contables
        file_path = os.path.join(GENERATED_FILES_DIR, "asientos_contables.xlsx")
        df = pd.DataFrame({
            "Cuenta": ["Gasto Jubilación", "Pasivo Jubilación", "ORI"],
            "Débito": [150000, 0, 20000],
            "Crédito": [0, 150000, 0]
        })
        df.to_excel(file_path, index=False)

        return jsonify({"message": "Asientos contables generados", "file": file_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
