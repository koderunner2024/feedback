from flask import Flask, render_template, request, redirect, url_for
from feedback_store import FeedbackStore

app = Flask(__name__)
feedback_store = FeedbackStore()

@app.route('/')
def index():
    feedbacks = feedback_store.get_all_feedbacks()
    return render_template('index.html', feedbacks=feedbacks)

@app.route('/submit', methods=['POST'])
def submit_feedback():
    name = request.form['name']
    comment = request.form['comment']
    feedback_store.add_feedback(name, comment)
    return redirect(url_for('index'))

@app.route('/feedback/<int:id>')
def feedback_detail(id):
    feedback = feedback_store.get_feedback_by_id(id)
    if feedback:
        return render_template('feedback.html', feedback=feedback)
    return "Feedback not found", 404

if __name__ == '__main__':
    app.run(debug=True)
