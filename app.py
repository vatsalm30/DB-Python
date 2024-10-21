import os
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename

# Create Flask App
app = Flask(__name__, template_folder='static')

# Set the folder to store uploaded files
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Allowed file extensions
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Function to check file extension
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Route to render the form (for testing purposes)
@app.route('/')
def form():
    return render_template('index.html')  # Ensure index.html is the form code provided earlier

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    try:
        # Collect form data
        collection = request.form.get('collection')
        title = request.form.get('title')
        price = float(request.form.get('price'))

        # Process the main product image
        if 'item' not in request.files:
            return jsonify({'error': 'No product image file uploaded'}), 400
        
        item_file = request.files['item']
        if item_file and allowed_file(item_file.filename):
            item_filename = secure_filename(item_file.filename)
            item_file.save(os.path.join(app.config['UPLOAD_FOLDER'], item_filename))
            item_url = f"/static/uploads/{item_filename}"
        else:
            return jsonify({'error': 'Invalid product image file'}), 400

        # Process available colors and images
        available_colors = []
        colors = request.form.getlist('color[]')
        images = request.files.getlist('imgs[]')
        if len(colors) > 0 and len(images) > 0:
            for i, color in enumerate(colors):
                color_images = []
                for j in range(i * len(images) // len(colors), (i + 1) * len(images) // len(colors)):
                    img_file = images[j]
                    if img_file and allowed_file(img_file.filename):
                        img_filename = secure_filename(img_file.filename)
                        img_file.save(os.path.join(app.config['UPLOAD_FOLDER'], img_filename))
                        img_url = f"/static/uploads/{img_filename}"
                        color_images.append({"img": img_url})
                    else:
                        return jsonify({'error': 'Invalid color image file'}), 400

                available_colors.append({"color": color, "imgs": color_images})

        # Process available sizes
        available_sizes = [{"size": int(size)} for size in request.form.getlist('size[]')]

        # Create the product dictionary
        product = {
            "collection": collection,
            "item": item_url,  # main product image link
            "price": price,
            "title": title,
            "availableColors": available_colors,
            "availableSizes": available_sizes
        }

        # Return the processed product as a JSON response
        return jsonify({'product': product}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
