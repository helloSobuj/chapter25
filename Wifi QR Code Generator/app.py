from flask import Flask, render_template, request
import qrcode
from PIL import Image, ImageDraw, ImageFont
import os

app = Flask(__name__)

# Ensure 'static' and 'templates' folders exist
if not os.path.exists('static'):
    os.makedirs('static')
if not os.path.exists('templates'):
    os.makedirs('templates')

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        wifi_name = request.form.get("wifi_name")
        wifi_password = request.form.get("wifi_password")
        security_type = request.form.get("security_type")  # Get security type

        # Generate QR code using the qrcode library directly in PNG format
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=7,  # Adjust box size for QR code size
            border=0,
        )

        # Construct the Wi-Fi data string (important for proper connection)
        wifi_data = f"WIFI:T:{security_type};S:{wifi_name};P:{wifi_password};;"
        qr.add_data(wifi_data)
        qr.make(fit=True)

        qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGBA")

        try:
            card_path = "static/card1.png"  # Make sure you have card1.png in static
            card = Image.open(card_path).convert("RGBA")
        except FileNotFoundError:
            return "Error: card1.png not found in the static folder", 500

        draw = ImageDraw.Draw(card)

        try:
            font_path = "static/Poppins-SemiBold.ttf"  # Or your font path
            font = ImageFont.truetype(font_path, 25)
        except IOError:
            return "Error: Poppins-SemiBold.ttf not found. Please install the font or provide the correct path.", 500

        bbox = draw.textbbox((0, 0), wifi_name, font=font)
        text_width = bbox[2] - bbox[0]
        text_x = (card.width - text_width) // 2
        text_y = 250

        draw.text((text_x, text_y), wifi_name, fill="#394ef4", font=font)

        qr_width, qr_height = qr_img.size
        qr_x = (card.width - qr_width) // 2
        qr_y = card.height - qr_height - 60

        card.paste(qr_img, (qr_x, qr_y), qr_img)

        output_path = "static/generated_card.png"
        card.save(output_path)

        return render_template("index.html", generated_card="generated_card.png")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)