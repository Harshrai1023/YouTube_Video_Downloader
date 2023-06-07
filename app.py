from flask import Flask, render_template, request
import pytube

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/download', methods=['POST'])
def download():
    video_url = request.form['url']
    try:
        url = pytube.YouTube(video_url)
        url.check_availability()
    except:
        return "Video not available"
    
    video = url.streams.get_highest_resolution()
    video.download('downloads/')
    return "Download completed"

if __name__ == '__main__':
    app.run(debug=True)
