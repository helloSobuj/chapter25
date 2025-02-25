![Banner](https://sobujhossen.com/wp-content/uploads/2025/02/easy-wifi-qr.png)

# WiFi QR Code Card Generator

This project creates a web application using Flask that generates a stylish WiFi QR code card.  Users input their WiFi network name (SSID), password, and security type, and the application generates a PNG image with a QR code that, when scanned by a phone, allows for easy WiFi connection. The QR code is embedded onto a pre-designed card image.

## Features

*   **Easy WiFi Connection:** Generates a QR code containing the WiFi credentials, simplifying the connection process for guests or when setting up new devices.
*   **Customizable Card:** Uses a template image (`card1.png`) for the card design, allowing for easy customization.  You can replace this image with your own design.
*   **Font Support:** Uses the Poppins font (`Poppins-SemiBold.ttf`) for the WiFi name display. Ensure this font is available in the `static` folder.
*   **Security Type Selection:** Supports WPA/WPA2, WEP, and Open security types.
*   **Downloadable Card:** Provides a download link for the generated card image.


## Technologies Used

*   **Python:** Core programming language.
*   **Flask:** Web framework for handling requests and responses.
*   **qrcode:** Library for generating QR codes.
*   **Pillow (PIL):** Library for image manipulation (adding QR code and text to the card).
*   **HTML/CSS:** For the user interface.


## Usage

1.  **Run the Flask app:**

    ```bash
    python app.py
    ```

2.  **Open your web browser and go to `http://127.0.0.1:5000/` (or the address shown in your terminal).**

3.  **Enter the WiFi name, password, and select the security type.**

4.  **Click "Generate Card".**

5.  **The generated card with the QR code will be displayed. You can download it by clicking the "Download Card" button.**

## Customization

*   **Card Design:** Replace `static/card1.png` with your own image. Ensure the image is appropriately sized for the QR code and text.
*   **Font:** You can change the font by replacing `static/Poppins-SemiBold.ttf` with another font file.  Make sure to update the font path in `app.py` if necessary.
*   **Styling:** Modify the CSS in `index.html` to customize the appearance of the web page.
*   **QR Code Size/Position:** Adjust the `box_size` in the `qrcode.QRCode` constructor and the `qr_x`, `qr_y` calculations in `app.py` to change the size and position of the QR code on the card.
*   **Text Position/Styling:** Update the `text_x`, `text_y`, and font parameters in `app.py` to change the position and style of the WiFi name text.

## Contributing

Contributions are welcome! Feel free to submit pull requests.
