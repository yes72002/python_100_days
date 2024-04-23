from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap5
from PIL import Image
import numpy as np

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

def rgb_to_hex(r, g, b):
    return '#{:02x}{:02x}{:02x}'. format(r, g, b)

# @app.route('/')
@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'

        uploaded_file = request.files['file']

        if uploaded_file.filename == '':
            return 'No selected file'

        # If file exists and filename is not empty, then save the file
        if uploaded_file:
            # Read image data from the uploaded file
            image = Image.open(uploaded_file)

            # Convert the image to a NumPy array
            image_array = np.array(image)
            # Convert the three-dimensional array to a two-dimensional array
            flat_image_array = image_array.reshape(-1, image_array.shape[-1])
            # Count the occurrence of colors
            color_counts = np.unique(flat_image_array, axis=0, return_counts=True)
            # Find the color with the most occurrences
            most_common_color_index = np.argmax(color_counts[1])
            most_common_color = color_counts[0][most_common_color_index]
            # print(f"most_common_color = {most_common_color}")

            # Convert RGB to hex
            r = most_common_color[0]
            g = most_common_color[1]
            b = most_common_color[2]
            most_common_color_hex = rgb_to_hex(r, g, b)
            print(f"most_common_color_hex = {most_common_color_hex}")
            return render_template('index.html', most_common_color_hex=most_common_color_hex)
    else:
        return render_template("index.html", most_common_color_hex="#fbdf00")


if __name__ == "__main__":
    app.run(debug=True, port=5003)
