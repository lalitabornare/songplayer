from flask import Flask, render_template, request, redirect, url_for, send_file, Response
from io import BytesIO
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    album = db.Column(db.String(100), nullable=False)
    filename = db.Column(db.String(100), nullable=False)
    data = db.Column(db.LargeBinary)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    songs = Song.query.all()
    return render_template('index.html', songs=songs)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        title = request.form['title']
        artist = request.form['artist']
        album = request.form['album']

        if file.filename.endswith('.mp3'):
            upload = Song(title=title, artist=artist, album=album, filename=file.filename, data=file.read())
            db.session.add(upload)
            db.session.commit()

        return redirect(url_for('index'))
    return render_template('upload.html')


@app.route('/delete/<int:song_id>', methods=['POST'])
def delete(song_id):
    upload = Song.query.filter_by(id=song_id).first()
    db.session.delete(upload)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form['query']
        songs = Song.query.filter(
            Song.title.ilike(f'%{search_term}%') |
            Song.artist.ilike(f'%{search_term}%') |
            Song.album.ilike(f'%{search_term}%')
        ).all()
        return render_template('search.html', songs=songs)
    return redirect(url_for('index'))


@app.route('/play/<int:song_id>')
def play(song_id):
    upload = Song.query.filter_by(id=song_id).first()
    return Response(upload.data, mimetype='audio/mp3')


@app.route('/download/<int:song_id>')
def download(song_id):
    upload = Song.query.filter_by(id=song_id).first()
    return send_file(BytesIO(upload.data), download_name=upload.title, mimetype='audio/mp3', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)

