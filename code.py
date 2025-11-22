Image Encryption Tool
Overview
This project provides a graphical user interface (GUI) for encrypting and decrypting images using different methods. Built with Python, Tkinter, NumPy, and Pillow (PIL), it allows users to upload an image, apply encryption techniques with a chosen key, and view both the original and processed images side by side.
Features
- Upload images in formats such as PNG, JPG, JPEG, and BMP.
- Choose from multiple encryption methods:
- XOR: Applies bitwise XOR with a key.
- Swap: Rearranges RGB channels.
- Negate: Inverts pixel values.
- Add: Adds or subtracts a key value.
- Multiply: Multiplies or divides pixel values by a factor.
- Enter a custom key for encryption and decryption.
- View original and encrypted/decrypted images simultaneously.
- Save encrypted images to disk.
How It Works
The program processes the image as a NumPy array and applies the selected encryption method. Decryption reverses the transformation using the same key. The GUI displays the original image on the left and the processed image on the right.
Usage
- Clone the repository:
git clone https://github.com/your-username/image-encryption.git
- Navigate to the project directory:
cd image-encryption
- Install dependencies:
pip install pillow numpy
- Run the program:
python image_encryptor.py


Example Workflow
- Upload an image.
- Select an encryption method (e.g., XOR).
- Enter a key (e.g., 123).
- Click Encrypt to view the encrypted image.
- Click Decrypt to restore the original.
- Save the encrypted image if desired.
Requirements
- Python 3.x
- Pillow
- NumPy
- Tkinter (comes pre-installed with Python)
