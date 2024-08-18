class FeedbackStore:
    def __init__(self):
        self.feedbacks = []
        self.counter = 1

    def add_feedback(self, name, comment):
        feedback = {
            'id': self.counter,
            'name': name,
            'comment': comment
        }
        self.feedbacks.append(feedback)
        self.counter += 1

    def get_all_feedbacks(self):
        return self.feedbacks

    def get_feedback_by_id(self, feedback_id):
        for feedback in self.feedbacks:
            if feedback['id'] == feedback_id:
                return feedback
        return None
