# songplayer
Flask Music Player
This is a simple Flask web application that allows users to upload and play music files. It uses SQLite database to store the metadata of the uploaded songs along with their binary data.

Setup
To run this application, follow these steps:

Clone the repository or download the source code.
Install the required Python packages using pip install -r requirements.txt.
Start the server by running python app.py.
Usage
Once the server is running, open a web browser and navigate to http://localhost:5000/. You will see the home page of the application which displays a list of all the uploaded songs.

To upload a new song, click on the "Upload Song" button on the top right corner of the page. This will take you to the upload form where you can select the song file and fill in the song details such as title, artist and album.

To play a song, click on the "Play" button next to the song in the list. This will take you to a new page where you can listen to the song.

To search for a song, enter the search query in the search box on the top right corner of the home page and click on the "Search" button.

To download a song, click on the "Download" button next to the song in the list.

To delete a song, click on the "Delete" button next to the song in the list and confirm the deletion.

License
This project is licensed under the MIT License. See the LICENSE file for more details.
