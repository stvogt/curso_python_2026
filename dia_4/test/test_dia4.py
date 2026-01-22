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
    'title': 'Quiz Clase 8 (IO + pathlib + Pandas — Nivel básico)',
    'description': 'Quiz corto y simple (contenido de IO/pathlib y Pandas visto en Clase 7–8).',
    'quiz_type': 'assignment',
    'published': True,
    'time_limit': 15,
    'shuffle_answers': True,
    # Chile (UTC-3). Inicio: 2026-01-23 16:00 CLT = 19:00 UTC
    'unlock_at': '2026-01-23T19:00:00Z',
    'due_at':    '2026-01-23T20:15:00Z',
    'lock_at':   '2026-01-24T20:15:00Z',
    'show_correct_answers': True,
    'show_correct_answers_at': '2026-01-23T20:15:00Z'
})

questions = [
    {
        'question_name': 'pathlib: unir rutas',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>from pathlib import Path\n\ndata_dir = Path("data")\npath = data_dir / "survey.csv"\nprint(path)</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'data/survey.csv', 'weight': 100},
            {'text': 'data + survey.csv', 'weight': 0},
            {'text': 'survey.csv/data', 'weight': 0},
            {'text': 'Error', 'weight': 0}
        ]
    },
    {
        'question_name': 'pathlib: exists',
        'question_text': '¿Qué devuelve este código (en general)?<br><br><pre><code>from pathlib import Path\n\np = Path("data") / "geology_samples.csv"\nprint(p.exists())</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'Imprime True si el archivo existe, y False si no existe', 'weight': 100},
            {'text': 'Imprime siempre True', 'weight': 0},
            {'text': 'Imprime siempre False', 'weight': 0},
            {'text': 'Imprime el contenido del archivo', 'weight': 0}
        ]
    },
    {
        'question_name': 'IO: modo append',
        'question_text': '¿Qué modo de apertura agrega texto al final del archivo?<br><br><pre><code>with open("log.txt", ___) as f:\n    f.write("nueva linea\\n")</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': '"a"', 'weight': 100},
            {'text': '"w"', 'weight': 0},
            {'text': '"r"', 'weight': 0},
            {'text': '"rb"', 'weight': 0}
        ]
    },
    {
        'question_name': 'IO: sobrescritura vs append',
        'question_text': '¿Qué ocurre si ejecutas este código dos veces?<br><br><pre><code>with open("resumen.txt", "w") as f:\n    f.write("Hola\\n")</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'El archivo se sobrescribe; al final queda una sola línea "Hola"', 'weight': 100},
            {'text': 'Se agregan dos líneas "Hola" (se duplica)', 'weight': 0},
            {'text': 'Da error porque el archivo ya existe', 'weight': 0},
            {'text': 'No escribe nada hasta llamar f.close() manualmente', 'weight': 0}
        ]
    },
    {
        'question_name': 'Pandas: read_csv',
        'question_text': '¿Qué hace este código?<br><br><pre><code>import pandas as pd\n\ndf = pd.read_csv("data/survey.csv")\nprint(type(df))</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'Carga un CSV y df es un DataFrame (pandas.core.frame.DataFrame)', 'weight': 100},
            {'text': 'df es una lista de diccionarios', 'weight': 0},
            {'text': 'df es un diccionario', 'weight': 0},
            {'text': 'df es un string con todo el CSV', 'weight': 0}
        ]
    },
    {
        'question_name': 'Pandas: seleccionar columna',
        'question_text': '¿Qué imprime este código?<br><br><pre><code>import pandas as pd\n\ndf = pd.DataFrame({"a": [1, 2, 3], "b": [10, 20, 30]})\nprint(df["b"].mean())</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': '20.0', 'weight': 100},
            {'text': '10.0', 'weight': 0},
            {'text': '30.0', 'weight': 0},
            {'text': 'Error', 'weight': 0}
        ]
    },
    {
        'question_name': 'Pandas: plot desde DataFrame',
        'question_text': '¿Cuál línea genera un gráfico de línea OD vs tiempo usando un DataFrame <code>df</code>?<br><br><pre><code># columnas: "time_h" y "od600"\n# Queremos y=od600, x=time_h</code></pre>',
        'question_type': 'multiple_choice_question',
        'points_possible': 1,
        'answers': [
            {'text': 'df.plot(kind="line", x="time_h", y="od600")', 'weight': 100},
            {'text': 'df.plot_line(x="time_h", y="od600")', 'weight': 0},
            {'text': 'plt.plot(df, "time_h", "od600")', 'weight': 0},
            {'text': 'df.plot(x="od600", y="time_h")', 'weight': 0}
        ]
    },
]

# === Upload questions ===
for question in questions:
    quiz.create_question(question=question)

