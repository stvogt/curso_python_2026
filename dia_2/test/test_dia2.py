from canvasapi import Canvas

# === Configuration ===
API_URL = "https://udec.instructure.com"
API_KEY = "14354~MuweMPPZVAahAfmPn2Te6ZxuUXNPBP68UPr6PBQtw4fWUVTuFJvkzz7RyMwLN4Qx"
COURSE_ID = 76194

# === Connect to Canvas ===
canvas = Canvas(API_URL, API_KEY)
course = canvas.get_course(COURSE_ID)

# === Quiz settings ===
quiz = course.create_quiz({
    'title': 'Quiz Clase 3–4 (Nivel básico)',
    'description': 'Quiz corto y simple (contenido Clases 3 y 4).',
    'quiz_type': 'assignment',
    'published': True,
    'time_limit': 15,
    'shuffle_answers': True,
    # Chile (UTC-3). Inicio: 2026-01-20 16:00 CLT = 19:00 UTC
    'unlock_at': '2026-01-20T19:00:00Z',
    'due_at':    '2026-01-20T20:15:00Z',
    'lock_at':   '2026-01-23T20:15:00Z',
    'show_correct_answers': True,
    'show_correct_answers_at': '2026-01-21T20:15:00Z'
})

questions = [
    {
        'question_name': 'Funciones: valor devuelto',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>def doble(x):\n    return x * 2\n\nprint(doble(4))</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': '8', 'weight': 100},
            {'text': '4', 'weight': 0},
            {'text': 'None', 'weight': 0},
            {'text': 'Error', 'weight': 0}
        ]
    },
    {
        'question_name': 'Funciones: sin return',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>def f(x):\n    y = x + 1\n\nprint(f(3))</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'None', 'weight': 100},
            {'text': '4', 'weight': 0},
            {'text': '3', 'weight': 0},
            {'text': 'Error', 'weight': 0}
        ]
    },
    {
        'question_name': 'Concepto: return vs print',
        'question_text': '¿Cuál es la diferencia correcta entre <code>return</code> y <code>print</code> en una función?',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'return entrega un valor al programa; print solo muestra texto en pantalla', 'weight': 100},
            {'text': 'print devuelve un valor y return lo muestra', 'weight': 0},
            {'text': 'return y print hacen exactamente lo mismo', 'weight': 0},
            {'text': 'print es obligatorio dentro de una función', 'weight': 0}
        ]
    },
    {
        'question_name': 'Funciones con listas',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>def suma(lista):\n    s = 0\n    for x in lista:\n        s = s + x\n    return s\n\nprint(suma([1, 2, 3]))</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': '6', 'weight': 100},
            {'text': '3', 'weight': 0},
            {'text': '0', 'weight': 0},
            {'text': 'Error', 'weight': 0}
        ]
    },
    {
        'question_name': 'Diccionarios: acceso',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>d = {"Ana": 5.5}\nprint(d["Ana"])</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': '5.5', 'weight': 100},
            {'text': '"Ana"', 'weight': 0},
            {'text': 'Error', 'weight': 0},
            {'text': 'None', 'weight': 0}
        ]
    },
    {
        'question_name': 'Concepto: diccionarios',
        'question_text': '¿Para qué se usa principalmente un diccionario en Python?',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'Para asociar valores a nombres (claves)', 'weight': 100},
            {'text': 'Para recorrer datos en orden', 'weight': 0},
            {'text': 'Para reemplazar funciones', 'weight': 0},
            {'text': 'Para repetir código', 'weight': 0}
        ]
    },
    {
        'question_name': 'Módulos: math',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>import math\nprint(math.floor(3.9))</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': '3', 'weight': 100},
            {'text': '4', 'weight': 0},
            {'text': '3.9', 'weight': 0},
            {'text': 'Error', 'weight': 0}
        ]
    }
]

# === Upload questions ===
for question in questions:
    quiz.create_question(question=question)

print(f"Quiz '{quiz.title}' created with {len(questions)} questions.")

