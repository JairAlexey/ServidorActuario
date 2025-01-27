# Sistema de Cálculos Actuariales API

API REST desarrollada en Flask para gestionar cálculos actuariales, generar informes y asientos contables.

## Descripción

Este sistema proporciona una API que permite:
- Gestionar datos iniciales
- Realizar cálculos actuariales
- Generar anexos en Excel
- Revisar documentación
- Generar informes en PDF
- Crear asientos contables

## Requisitos
python
pip install -r requirements.txt

Dependencias principales:
- Flask
- pandas
- fpdf

## Estructura de Archivos

Los archivos generados se guardan automáticamente en:

~/Desktop/Archivos_Generados_GPT/


## Endpoints Disponibles

### 1. Verificación del Servidor
- **URL**: `/`
- **Método**: `GET`
- **Descripción**: Verifica que el servidor está funcionando

### 2. Datos Iniciales
- **URL**: `/submit-initial-data`
- **Método**: `POST`
- **Descripción**: Recibe y almacena los datos iniciales
- **Salida**: JSON con la ruta del archivo guardado

### 3. Cálculos Actuariales
- **URL**: `/generate-actuarial-calculations`
- **Método**: `POST`
- **Descripción**: Genera cálculos actuariales basados en los datos proporcionados
- **Salida**: Excel con los cálculos

### 4. Anexos Excel
- **URL**: `/generate-excel-annexes`
- **Método**: `POST`
- **Descripción**: Genera anexos en formato Excel
- **Salida**: Archivo Excel con anexos

### 5. Revisión de Anexos
- **URL**: `/review-annexes`
- **Método**: `POST`
- **Descripción**: Verifica la existencia de anexos generados

### 6. Informe Final
- **URL**: `/generate-final-report`
- **Método**: `POST`
- **Descripción**: Genera un informe final en PDF
- **Salida**: Archivo PDF con el informe

### 7. Asientos Contables
- **URL**: `/generate-accounting-entries`
- **Método**: `POST`
- **Descripción**: Genera asientos contables en Excel
- **Salida**: Archivo Excel con los asientos contables

## Ejecución

Para ejecutar el servidor:

bash
python app.py

El servidor se iniciará en `http://0.0.0.0:5000`

## Manejo de Errores

Todos los endpoints incluyen manejo de errores y devolverán:
- Código 200: Para operaciones exitosas
- Código 500: Para errores internos del servidor
- Código 404: Para recursos no encontrados

## Seguridad

Se recomienda implementar medidas de seguridad adicionales antes de usar en producción:
- Autenticación
- HTTPS
- Validación de datos
- Control de acceso

## Contribución

Para contribuir al proyecto:
1. Fork del repositorio
2. Crear una rama para nuevas características
3. Enviar pull request

## Licencia

[Añadir tipo de licencia]