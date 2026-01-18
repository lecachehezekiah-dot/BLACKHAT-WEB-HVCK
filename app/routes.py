from flask import Blueprint, render_template, request, jsonify
from .models.ai_model import AIModel
from .services.hacking_tools import run_hacking_tool
from .services.sandbox import execute_in_sandbox

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = AIModel.generate_response(user_input)
        return jsonify({'response': response})
    return render_template('chat.html')
