from flask import Flask
import urllib.parse

app = Flask(__name__)

# 🔴 CHANGE THESE
SHOP_WHATSAPP = "917888650410"
GOOGLE_REVIEW = "https://www.google.co.in/maps/place/SHARDA+CLOTH+STORE/@30.3181785,76.3929729,17z/data=!4m8!3m7!1s0x3910298b7cc8435b:0x254e4dae5eddb8c4!8m2!3d30.3181785!4d76.3955478!9m1!1b1!16s%2Fg%2F11tp7d7_1x?entry=ttu&g_ep=EgoyMDI2MDQwMS4wIKXMDSoASAFQAw%3D%3D"

@app.route("/")
def home():
    message = "Hi i need help regarding clothes"

    encoded_msg = urllib.parse.quote(message)

    whatsapp_url = f"https://wa.me/{SHOP_WHATSAPP}?text={encoded_msg}"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Sharda Cloth Shop</title>
    </head>
    <body style="text-align:center; margin-top:50px;">

        <h2>Welcome to Sharda Cloth Shop 👕</h2>
        <p>Click below to continue</p>

        <br>

        <a href="{whatsapp_url}" target="_blank">
            <button style="padding:10px 20px;">Send WhatsApp Message</button>
        </a>

        <br><br>

        <a href="{GOOGLE_REVIEW}" target="_blank">
            <button style="padding:10px 20px;">Give Google Review ⭐</button>
        </a>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)