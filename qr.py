import qrcode
from PIL import Image

# Generate QR code
def generate_qr(data, filename="qr_code.png"):
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code
        box_size=10,  # size of each box
        border=4,  # thickness of the border
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill="black", back_color="white")

    # Save the image to a file
    img.save(filename)
    print(f"QR Code saved as {filename}")

# Input data for the QR code
data = input("Enter the data or URL for the QR code: ")

# Generate and save the QR code
generate_qr(data)
