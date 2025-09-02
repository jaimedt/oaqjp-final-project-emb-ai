from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector as ed

app = Flask("Emotion Detector")

@app.route("\emotionDetector")
def emotion_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    