'''
Uses an embedded NLP library to analyze user text and return the identified emotions
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as ed

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_detector():
    '''
    Call the NLP library via http call and return the formatted response
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    results = ed(text_to_analyze)
    if results['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    return f"For the given statement, the system response is 'anger': {results['anger']}, \
    'disgust': {results['disgust']}, 'fear': {results['fear']}, 'joy': {results['joy']} \
    and 'sadness': {results['sadness']}. The dominant emotion is \
    {results['dominant_emotion']}."

@app.route("/")
def render_index_page():
    '''
    Render the web app
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
