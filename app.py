from flask import Flask, request, render_template
from tribe_data import find_best_tribe

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    traits = request.form.getlist('traits')
    best_tribe, description, all_scores, related = find_best_tribe(traits)
    return render_template('result.html', tribe=best_tribe, desc=description, scores=all_scores, related=related)
if __name__ == '__main__':
    app.run(debug=True)