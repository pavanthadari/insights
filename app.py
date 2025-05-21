from flask import Flask, render_template, request, jsonify
from modules.insight_engine import analyze_data
from modules.chat_engine import get_chat_response

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['datafile']
    insights, visuals, strategies, kpis, correlations, impact, automation = analyze_data(file)
    return render_template('dashboard.html', insights=insights, visuals=visuals, strategies=strategies,
                           kpis=kpis, correlations=correlations, impact=impact, automation=automation)

@app.route('/api/chat', methods=['POST'])
def chat():
    user_msg = request.json.get('message')
    response = get_chat_response(user_msg)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)