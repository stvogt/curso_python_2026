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
    'title': 'Quiz Clase 6 (Matplotlib — Nivel básico)',
    'description': 'Quiz corto y simple (contenido Matplotlib visto en Clase 6).',
    'quiz_type': 'assignment',
    'published': True,
    'time_limit': 15,
    'shuffle_answers': True,
    # Chile (UTC-3). Inicio: 2026-01-22 16:00 CLT = 19:00 UTC
    'unlock_at': '2026-01-22T19:00:00Z',
    'due_at':    '2026-01-22T20:15:00Z',
    'lock_at':   '2026-01-23T20:15:00Z',
    'show_correct_answers': True,
    'show_correct_answers_at': '2026-01-22T20:15:00Z'
})

questions = [
    {
        'question_name': 'Import básico de pyplot',
        'question_text': '¿Cuál es la forma más común de importar Matplotlib para graficar con <code>plt</code>?<br><br>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'import matplotlib.pyplot as plt', 'weight': 100},
            {'text': 'import matplotlib as plt', 'weight': 0},
            {'text': 'from matplotlib import pyplot', 'weight': 0},
            {'text': 'import pyplot as matplotlib', 'weight': 0}
        ]
    },
    {
        'question_name': 'Línea: plot',
        'question_text': '¿Qué función se usa típicamente para hacer un gráfico de línea con Matplotlib?<br><br>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'plt.plot(x, y)', 'weight': 100},
            {'text': 'plt.scatter(x, y)', 'weight': 0},
            {'text': 'plt.bar(x, y)', 'weight': 0},
            {'text': 'plt.hist(x)', 'weight': 0}
        ]
    },
    {
        'question_name': 'Puntos: scatter',
        'question_text': '¿Qué función se usa para graficar puntos (dispersión) y ver relación entre dos variables?<br><br>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'plt.scatter(x, y)', 'weight': 100},
            {'text': 'plt.plot(x, y)', 'weight': 0},
            {'text': 'plt.bar(x, y)', 'weight': 0},
            {'text': 'plt.hist(y)', 'weight': 0}
        ]
    },
    {
        'question_name': 'Etiquetas de ejes',
        'question_text': '¿Qué par de funciones agrega etiquetas a los ejes X e Y?<br><br>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'plt.xlabel("X"); plt.ylabel("Y")', 'weight': 100},
            {'text': 'plt.xname("X"); plt.yname("Y")', 'weight': 0},
            {'text': 'plt.xaxis("X"); plt.yaxis("Y")', 'weight': 0},
            {'text': 'plt.axis("X", "Y")', 'weight': 0}
        ]
    },
    {
        'question_name': 'Leyenda: legend',
        'question_text': 'Para que <code>plt.legend()</code> muestre una leyenda, ¿qué debe existir en los gráficos?<br><br>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'Cada curva debe tener <code>label=...</code> en <code>plt.plot</code> (o similar)', 'weight': 100},
            {'text': 'Debes usar obligatoriamente <code>plt.grid(True)</code>', 'weight': 0},
            {'text': 'Debes llamar <code>plt.show()</code> antes de graficar', 'weight': 0},
            {'text': 'La leyenda aparece siempre automáticamente', 'weight': 0}
        ]
    },
    {
    'question_name': 'Scatter: cambio de marcador',
    'question_text': '¿Cuál de las siguientes líneas cambia el **marcador** a círculos al graficar puntos con Matplotlib?<br><br>',
    'question_type': 'multiple_choice_question',
    'points_possible': 1,
    'answers': [
        {'text': 'plt.scatter(x, y, marker="o")', 'weight': 100},
        {'text': 'plt.scatter(x, y, mark="o")', 'weight': 0},
        {'text': 'plt.scatter(x, y, style="o")', 'weight': 0},
        {'text': 'plt.scatter(x, y, symbol="o")', 'weight': 0}
    ]
},
    {
    'question_name': 'Subplots: sintaxis básica',
    'question_text': '¿Cuál de las siguientes opciones crea correctamente una figura con **1 fila y 2 columnas** de subplots en Matplotlib?<br><br>',
    'question_type': 'multiple_choice_question',
    'points_possible': 1,
    'answers': [
        {'text': 'fig, ejes = plt.subplots(1, 2)', 'weight': 100},
        {'text': 'fig = plt.subplot(2, 1)', 'weight': 0},
        {'text': 'plt.subplots = (1, 1)', 'weight': 0},
        {'text': 'fig, ejes = plt.subplot(2, 2)', 'weight': 0}
    ]
},

]

# === Upload questions ===
for question in questions:
    quiz.create_question(question=question)

