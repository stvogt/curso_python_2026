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
    'title': 'Quiz 19.01 Día 1',
    'description': 'Quiz corto (contenido Clases 1 y 2).',
    'quiz_type': 'assignment',
    'published': True,
    'time_limit': 15,
    'shuffle_answers': True,
    # Chile (UTC-3). Inicio: 2026-01-19 16:00 CLT = 19:00 UTC
    'unlock_at': '2026-01-19T19:00:00Z',
    'due_at':    '2026-01-19T20:15:00Z',
    'lock_at':   '2026-01-23T20:15:00Z',
    'show_correct_answers': True,
    'show_correct_answers_at': '2026-01-20T20:15:00Z'
})

questions = [
    {
        'question_name': 'Precedencia de operadores',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>resultado = 2 + 3 * 4 ** 2\nprint(resultado)</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': '50', 'weight': 100},
            {'text': '56', 'weight': 0},
            {'text': '80', 'weight': 0},
            {'text': '146', 'weight': 0}
        ]
    },
    {
        'question_name': 'f-strings (formato)',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>nombre = "Ana"\nedad = 20\nprint(f"{nombre}-{edad}")</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'Ana-20', 'weight': 100},
            {'text': 'nombre-edad', 'weight': 0},
            {'text': 'Anaedad', 'weight': 0},
            {'text': 'Error', 'weight': 0}
        ]
    },
    {
        'question_name': 'if / else (umbral)',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>nota = 60\nif nota >= 60:\n    print("aprueba")\nelse:\n    print("repite")</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'aprueba', 'weight': 100},
            {'text': 'repite', 'weight': 0},
            {'text': 'No imprime nada', 'weight': 0},
            {'text': 'Error de indentación', 'weight': 0}
        ]
    },
    {
        'question_name': 'Condiciones lógicas con and (bordes)',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>t = 25.0\nif (t >= 20.0) and (t <= 25.0):\n    print("en rango")\nelse:\n    print("fuera")</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'en rango', 'weight': 100},
            {'text': 'fuera', 'weight': 0},
            {'text': 'No imprime nada', 'weight': 0},
            {'text': 'Error', 'weight': 0}
        ]
    },
    {
        'question_name': 'Uso de not',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>p = 0\ndentro = (p >= 0) and (p <= 100)\nif not (dentro):\n    print("fuera")\nelse:\n    print("ok")</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'ok', 'weight': 100},
            {'text': 'fuera', 'weight': 0},
            {'text': 'No imprime nada', 'weight': 0},
            {'text': 'Error', 'weight': 0}
        ]
    },
    {
        'question_name': 'Listas: indexing y len()',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>a = [10, 20, 30]\nprint(a[len(a) - 1])</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': '30', 'weight': 100},
            {'text': '10', 'weight': 0},
            {'text': '20', 'weight': 0},
            {'text': 'Error', 'weight': 0}
        ]
    },
    {
        'question_name': 'for: acumulador (suma)',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>vals = [1, 2, 3]\nsuma = 0\nfor v in vals:\n    suma = suma + v\nprint(suma)</code></pre>',
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
        'question_name': 'Expresiones booleanas válidas',
        'question_text': 'Sea <code>x = 5</code>. ¿Cuáles de estas expresiones son <strong>True</strong>?<br><br>Selecciona todas las correctas.',
        'question_type': 'multiple_answers_question',
        'points_possible': 1,
        'answers': [
            {'text': '(x > 3) and (x < 10)', 'weight': 100},
            {'text': '(x == 5) or (x < 0)', 'weight': 100},
            {'text': 'not (x >= 5)', 'weight': -50},
            {'text': '(x != 5) and (x <= 5)', 'weight': -50}
        ]
    }
]

# === Upload questions ===
for question in questions:
    quiz.create_question(question=question)

print(f"Quiz '{quiz.title}' created with {len(questions)} questions.")

