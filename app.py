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
        # Validar y guardar datos iniciales
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
        data = request.json
        result = {"cálculo": "Resultado basado en datos proporcionados"}
        file_path = os.path.join(GENERATED_FILES_DIR, "calculos_actuariales.xlsx")
        df = pd.DataFrame([result])
        df.to_excel(file_path, index=False)
        return jsonify({"message": "Cálculos actuariales generados", "file": file_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint 3: Generar anexos en Excel
@app.route('/generate-excel-annexes', methods=['POST'])
def generate_excel_annexes():
    try:
        file_path = os.path.join(GENERATED_FILES_DIR, "anexos_jubilacion.xlsx")
        # Crear archivo Excel con pandas
        df = pd.DataFrame({"Anexo 1": ["Datos ejemplo"]})
        df.to_excel(file_path, index=False)
        return jsonify({"message": "Anexos Excel generados", "file": file_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Endpoint 4: Revisar anexos en Excel
@app.route('/review-annexes', methods=['POST'])
def review_annexes():
    try:
        # Ruta donde están los anexos generados
        file_path = os.path.join(GENERATED_FILES_DIR, "anexos_jubilacion.xlsx")
        if os.path.exists(file_path):
            return jsonify({"message": "Anexos encontrados", "file": file_path})
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
        file_path = os.path.join(GENERATED_FILES_DIR, "asientos_contables.xlsx")
        # Crear archivo Excel con asientos contables
        df = pd.DataFrame({
            "Cuenta": ["Gasto Jubilación", "Pasivo Jubilación", "ORI"],
            "Débito": [1000, 0, 200],
            "Crédito": [0, 1200, 0]
        })
        df.to_excel(file_path, index=False)
        return jsonify({"message": "Asientos contables generados", "file": file_path})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
