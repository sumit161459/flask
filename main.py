from flask import Flask, request, jsonify
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)
summarizer = pipeline("summarization")


@app.route('/')
def hellp_world():
    return 'Hello, World!'


@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    youtube_video = data['text']
    video_id = youtube_video.split("=")[1]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    corpus = " "
    for i in transcript:
        corpus += ' '+i['text']
    # max_length = data.get('max_length', 100)
    summary = summarizer(corpus)[0]['summary_text']
    return jsonify({'summary': summary})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="5000", debug=True)
