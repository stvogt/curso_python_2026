# Curso: Python para Ciencias e Ingeniería
## Clase 1 — Fundamentos de Python y pensamiento computacional
**Fecha:** [completar]  
**Instructor/a:** [completar]

---

## Agenda (90 min)
- 0:00–0:05 Bienvenida y objetivos
- 0:05–0:20 ¿Qué es programar?
- 0:20–0:30 ¿Por qué Python?
- 0:30–0:40 Entorno de trabajo
- 0:40–1:05 Primer contacto con Python
- 1:05–1:20 Entrada y salida
- 1:20–1:30 Ejemplo final + cierre + tarea

---

## Objetivos de la clase
- Entender qué es programar y qué es un algoritmo
- Conocer por qué Python es útil en ciencias e ingeniería
- Ejecutar código básico: variables, tipos y operaciones
- Practicar entrada/salida y un programa sencillo

---

## 1. ¿Qué es programar? (10–15 min)
- Dar instrucciones **precisas** a un computador
- Lenguaje natural vs formal vs programación
- Algoritmo = receta paso a paso
- Pensamiento computacional = descomponer problemas

----

### Ejemplo rápido: promedio de notas
**Lenguaje natural:**
- Pedir 3 notas
- Sumar
- Dividir por 3
- Mostrar promedio

**Python (idea):**
```python
n1 = 5.0
n2 = 6.0
n3 = 4.0
prom = (n1 + n2 + n3) / 3
print(prom)
```

----

### Check de comprensión #1
- ¿Qué diferencia hay entre **instrucción** y **algoritmo**?
- ¿Por qué una receta es un buen ejemplo de algoritmo?

---

## 2. ¿Por qué Python? (5–10 min)
- Interpretado: ejecuta línea por línea
- Legible y expresivo
- Usado en ciencia de datos e ingeniería
- Gran ecosistema de librerías
- Comparación breve: Python vs Fortran/C/MATLAB (más legible y flexible)

---

## 3. Entorno de trabajo (10 min)
- Intérprete interactivo
- Scripts `.py`
- IDEs: VS Code, Spyder, Jupyter
- Tipos de error:
  - **Sintaxis**: forma incorrecta
  - **Lógico**: resultado incorrecto

---

## 4. Primer contacto con Python (20–25 min)
- Instrucciones y funciones básicas
- Variables y tipos
- Operaciones y precedencia

----

### Mini-demo 1: Hola mundo
**Objetivo:** ejecutar la primera instrucción.
```python
print("Hola mundo")
```
**Output esperado:**
```
Hola mundo
```

----

### 4.2 Variables y tipos
- Asignación: `variable = valor`
- Tipos comunes: `int`, `float`, `str`
- Tipado dinámico: el tipo depende del valor

----

### Mini-demo 2: type() con int/float/str
**Objetivo:** ver tipos básicos.
```python
x = 5
y = 2.0
nombre = "Ana"

print(type(x))
print(type(y))
print(type(nombre))
```
**Output esperado:**
```
<class 'int'>
<class 'float'>
<class 'str'>
```

----

### Check de comprensión #2
- ¿Qué tipo devuelve `type(3.0)`?
- ¿Qué diferencia hay entre `"5"` y `5`?

----

### 4.3 Operaciones y precedencia
- `+`, `-`, `*`, `/`, `**`
- Paréntesis cambian el orden
- Precedencia: potencia > multiplicación/división > suma/resta

----

### Mini-demo 3: operaciones + precedencia
**Objetivo:** practicar operaciones y prioridad.
```python
a = 10
b = 3

print(a + b)
print(a / b)
print(a ** b)
print(a + b * 2)
print((a + b) * 2)
```
**Output esperado:**
```
13
3.3333333333333335
1000
16
26
```

---

## Errores comunes #1
**Input devuelve str**
```python
a = input("a: ")
b = input("b: ")
print(a + 1)
```
**Error esperado:**
```
TypeError: can only concatenate str (not "int") to str
```
**Corrección:** convertir con `int()` o `float()`.

---

## 5. Entrada y salida (15 min)
- `input()` siempre retorna `str`
- Convertir: `int()`, `float()`
- `print()` con comas
- `f-strings` básicos

----

### Mini-demo 4: input y conversión
**Objetivo:** leer y sumar dos números.
```python
a = int(input("a: "))
b = float(input("b: "))

print("Suma:", a + b)
```
**Output esperado:**
```
Suma: 7.5
```

---

## Errores comunes #2
- `/` devuelve **float**
- `//` hace división **entera**
- Precedencia importa

```python
print(7 / 2)
print(7 // 2)
print(2 + 3 * 4)
```
**Output esperado:**
```
3.5
3
14
```

---

## Buenas prácticas
- Nombres claros: `promedio`, `nota1`
- Comentarios breves y útiles
- Probar paso a paso (incremental)

---

## Actividad rápida (3 min)
**Predice el output:**
```python
x = 2
x = x + 3
print(x ** 2)
```

----

### Respuesta (notes)
- `x` queda en 5
- `5 ** 2` es 25

---

## 6. Primer ejemplo útil (10–15 min)
**Programa:** promedio con nombre y 3 notas

----

### Mini-demo 5: programa promedio
**Objetivo:** integrar variables, input y formato.
```python
nombre = input("Nombre: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))
nota3 = float(input("Nota 3: "))

promedio = (nota1 + nota2 + nota3) / 3
print(f"{nombre}, tu promedio es {promedio:.2f}")
```
**Output esperado:**
```
Ana, tu promedio es 5.33
```

---

## Check de comprensión #3
- ¿Por qué usamos `float()` en las notas?
- ¿Qué hace `:.2f` en un f-string?

---

## 7. Cierre conceptual (5 min)
- Python se lee casi como inglés
- La computadora no interpreta intenciones
- Orden y nombres claros ayudan a evitar errores
- Probar en pasos pequeños ahorra tiempo

---

## Resumen + Tarea
**Resumen:**
- Programar = instrucciones + algoritmos
- Variables, tipos y operaciones
- Entrada/salida con `input()` y `print()`

**Tarea breve:**
- Pedir dos números
- Calcular suma, resta, producto y división
- Mostrar resultados claramente
