from flask import Flask, jsonify
import random
from time import sleep
from threading import Lock

app = Flask(__name__)

# Datos del puzzle
PUZZLE_TEXT = "Este es un mensaje secreto que debe ser reconstruido a partir de fragmentos aleatorios"
FRAGMENTS = [(i, word) for i, word in enumerate(PUZZLE_TEXT.split())]
FRAGMENTS_DICT = {i: {"id": i, "index": idx, "text": word} 
                 for i, (idx, word) in enumerate(FRAGMENTS, start=1)}
lock = Lock()

@app.route('/fragment')
def get_fragment():
    # Simular delay aleatorio
    sleep(random.uniform(0.1, 0.4))
    
    with lock:
        # Escoger un fragmento aleatorio que no se haya enviado aún
        available_ids = [id for id in FRAGMENTS_DICT if FRAGMENTS_DICT[id] is not None]
        if not available_ids:
            return jsonify({"error": "No hay más fragmentos disponibles"}), 404
        
        fragment_id = random.choice(available_ids)
        response = FRAGMENTS_DICT[fragment_id]
        FRAGMENTS_DICT[fragment_id] = None  # Marcar como enviado
    
    return jsonify(response)

@app.route('/solution')
def get_solution():
    return jsonify({
        "full_text": PUZZLE_TEXT,
        "fragments": [f[1] for f in sorted(FRAGMENTS, key=lambda x: x[0])]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)