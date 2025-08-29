import requests, json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url = url, json = payload, headers = header)
    predicted_emotions = json.loads(response.text)['emotionPredictions'][0]['emotion']
    dominant_emotion = [key for key in predicted_emotions 
    if predicted_emotions[key] == max(predicted_emotions.values())][0]
    predicted_emotions['dominant_emotion'] = dominant_emotion
    return predicted_emotions