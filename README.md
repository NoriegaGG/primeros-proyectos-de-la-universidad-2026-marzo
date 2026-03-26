# primeros-proyectos-de-la-universidad-2026-marzo
# Colección de Programas Python - Noriega Angel

## 📋 Descripción General

Colección de programas educativos desarrollados en Python que demuestran conceptos fundamentales de programación como:
- Cálculo matemático y ecuaciones
- Entrada/salida de datos
- Condicionales (if/else)
- Operaciones aritméticas
- Uso de módulos (math, datetime)
- Formato de salida

Estos programas fueron desarrollados como parte de mi aprendizaje en Python y demuestran aplicaciones prácticas de conceptos de programación en contextos reales.

---

## 🚀 Programas Incluidos

### 1. **ProgramaEjemploEcuacionesNoriega_Angel.py**
**Descripción:** Calcula el resultado de una ecuación matemática compleja con potencias y raíces cuadradas.

**Fórmula:**
```
z = [(x+3)² + x + √(x+5)] / (x^(2/3) + 1)
```

**Características:**
- Input de valor x
- Cálculo de potencias y raíces
- Visualización detallada de cálculos intermedios
- Formato de salida personalizado

**Ejemplo de uso:**
```bash
python ProgramaEjemploEcuacionesNoriega_Angel.py
Ingrese x: 10
responde si o no si quieres ver a detalle la ecuacion: si
```

---

### 2. **ProgramaPropuesto1TerrenoNoriega_Angel.py**
**Descripción:** Calcula el área total de un terreno que puede tener forma rectangular o rectangular + triangular.

**Características:**
- Input de datos del terreno
- Cálculo de área rectangular
- Cálculo de área triangular (opcional)
- Área total combinada
- Validación de entrada del usuario

**Ejemplo de uso:**
```bash
python ProgramaPropuesto1TerrenoNoriega_Angel.py
querido ingeniero/a por favor ingrese su nombre: Juan
ingrese el lado A del terreno: 50
ingrese el lado B del terreno: 30
querido ingeniero/a el area total del terreno es: 1500.00 unidades cuadradas
```

---

### 3. **ProgramaPropuesto2PiezaNoriega_Angel.py**
**Descripción:** Calcula el área sombreada de una pieza mecánica (cuadrado con círculo inscrito).

**Fórmula:**
```
Área Sombreada = Área Cuadrado - Área Círculo
```

**Características:**
- Cálculo de área cuadrada
- Cálculo de área circular
- Uso del módulo `math`
- Aplicación práctica en ingeniería

**Ejemplo de uso:**
```bash
python ProgramaPropuesto2PiezaNoriega_Angel.py
Estimado Sr. mecanico, por favor ingrese su nombre: Carlos
ingrese el lado A del cuadrado: 20
```

---

### 4. **ProgramaEjemploVentasNoriega_Angel.py**
**Descripción:** Programa de punto de venta que calcula montos con descuentos y emite boleta.

**Características:**
- Entrada de datos del producto
- Cálculo de monto bruto
- Aplicación de descuentos
- Generación de boleta
- Registro de fecha y hora con `datetime`

**Ejemplo de uso:**
```bash
python ProgramaEjemploVentasNoriega_Angel.py
Ingrese el nombre del producto: Laptop
Ingrese el precio del producto: 2500
Ingrese la cantidad del producto: 2
Ingrese el descuento: 10
```

**Salida:**
```
========= Resumen de la compra =========
El monto bruto de la compra es: 5000 soles
El monto del descuento es: 500 soles
El monto a pagar es: 4500 soles
Fecha de la compra: 2026-03-26 14:30:45
```

---

### 5. **ProgramaPropuestoPromedioNoriega_Angel.py**
**Descripción:** Calcula el promedio final de un alumno basado en evaluaciones ponderadas.

**Ponderaciones:**
- Consolidado 1: 20%
- Examen Parcial: 25%
- Consolidado 2: 20%
- Examen Final: 35%

**Características:**
- Input de todas las calificaciones
- Cálculo de promedio ponderado
- Resumen de calificaciones
- Formato profesional de salida

**Ejemplo de uso:**
```bash
python ProgramaPropuestoPromedioNoriega_Angel.py
Ingrese el nombre del alumno: Maria
Ingrese el consolidado 1: 15
Ingrese el examen parcial: 16
Ingrese el consolidado 2: 14
Ingrese el examen final: 17

========= Resumen del alumno =========
El promedio final de Maria es: 15.65
```

---

## 📋 Requisitos

- **Python 3.6+**
- Módulos estándar (incluidos en Python):
  - `math` - para operaciones matemáticas
  - `datetime` - para manejo de fechas

No hay dependencias externas. Todos los programas usan solo la librería estándar de Python.

---

## 💻 Instalación

### Requisitos previos:
1. Tener Python 3.6 o superior instalado
2. Verificar instalación:
   ```bash
   python --version
   ```

### Pasos:
1. Clona este repositorio:
   ```bash
   git clone https://github.com/NoriegaGGsoy/mis-programas-python.git
   ```

2. Accede al directorio:
   ```bash
   cd mis-programas-python
   ```

3. ¡Listo! No necesitas instalar dependencias adicionales.

---

## 🏃 Cómo usar

Ejecuta cualquier programa con:

```bash
python nombre_del_programa.py
```

Ejemplo:
```bash
python ProgramaEjemploEcuacionesNoriega_Angel.py
```

Luego sigue las instrucciones que aparecen en pantalla.

---

## 📁 Estructura del Proyecto

```
mis-programas-python/
├── README.md
├── ProgramaEjemploEcuacionesNoriega_Angel.py
├── ProgramaPropuesto1TerrenoNoriega_Angel.py
├── ProgramaPropuesto2PiezaNoriega_Angel.py
├── ProgramaEjemploVentasNoriega_Angel.py
└── ProgramaPropuestoPromedioNoriega_Angel.py
```

---

## 🎯 Conceptos Demostrados

| Concepto | Programas |
|----------|-----------|
| Variables y tipos de datos | Todos |
| Input/Output (print, input) | Todos |
| Condicionales (if/else) | 1, 2, 4, 5 |
| Operaciones aritméticas | Todos |
| Módulo `math` | 1, 3 |
| Módulo `datetime` | 4 |
| Formato de strings (f-strings) | Todos |
| Funciones nativas (pow, sqrt, len) | 1, 3 |

---

## 📚 Aprendizajes Clave

Estos programas demuestran:

✅ **Pensamiento lógico** - Resolución de problemas paso a paso  
✅ **Manejo de entrada/salida** - Interacción con el usuario  
✅ **Operaciones matemáticas** - Cálculos complejos  
✅ **Control de flujo** - Uso de condicionales  
✅ **Uso de librerías** - Módulos math y datetime  
✅ **Formato de salida** - Presentación clara de resultados  

---

## 🔧 Posibles Mejoras Futuras

- [ ] Agregar validación de entrada más robusta
- [ ] Crear interfaz gráfica (tkinter)
- [ ] Agregar manejo de excepciones (try/except)
- [ ] Crear pruebas unitarias
- [ ] Agregar más ejemplos de uso
- [ ] Documentación en código con docstrings

---

## 📝 Licencia

Estos programas están disponibles para uso educativo.

---

## 👨‍💻 Autor

**Angel Noriega**

---

## 📧 Contacto

Si tienes preguntas o sugerencias, no dudes en contactarme.

---

## 🙏 Notas

Estos programas fueron desarrollados como parte de mi aprendizaje en Python. Cada programa representa una aplicación práctica de conceptos fundamentales de programación.

¡Gracias por revisar mis proyectos! 🚀
