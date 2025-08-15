import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QFileDialog, QLineEdit, QVBoxLayout, QMessageBox
from PyQt5.QtGui import QPixmap
from background_remove import remove_bg
from customize_product import apply_customization

from utils import ensure_dir
import os
from PIL import Image

PREVIEW_DIR = "outputs/previews"
FINAL_DIR = "outputs/final_designs"
ensure_dir(PREVIEW_DIR)
ensure_dir(FINAL_DIR)

class ProductCustomizerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Product Customizer")
        self.setGeometry(100, 100, 600, 600)
        self.layout = QVBoxLayout()

        self.upload_btn = QPushButton("Upload Product Image")
        self.upload_btn.clicked.connect(self.upload_image)
        self.layout.addWidget(self.upload_btn)

        self.prompt_input = QLineEdit()
        self.prompt_input.setPlaceholderText("Enter customization prompt here...")
        self.layout.addWidget(self.prompt_input)

        self.run_btn = QPushButton("Customize Product")
        self.run_btn.clicked.connect(self.customize)
        self.layout.addWidget(self.run_btn)

        self.preview_label = QLabel("Preview will appear here")
        self.layout.addWidget(self.preview_label)

        self.setLayout(self.layout)
        self.input_image_path = None

    def upload_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Product Image", "", "Images (*.png *.jpg *.jpeg)")
        if file_name:
            self.input_image_path = file_name
            pixmap = QPixmap(file_name).scaled(400, 400)
            self.preview_label.setPixmap(pixmap)

    def customize(self):
        if not self.input_image_path or not self.prompt_input.text():
            QMessageBox.warning(self, "Error", "Please upload an image and enter a prompt!")
            return
        
        bg_removed_path = os.path.join(PREVIEW_DIR, "bg_removed.png")
        final_image_path = os.path.join(FINAL_DIR, "customized.png")

        # Remove background
        remove_bg(self.input_image_path, bg_removed_path)

        # Apply AI customization
        apply_customization(bg_removed_path, self.prompt_input.text(), final_image_path)

        pixmap = QPixmap(final_image_path).scaled(400, 400)
        self.preview_label.setPixmap(pixmap)
        QMessageBox.information(self, "Done", f"Customized product saved to {final_image_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ProductCustomizerApp()
    window.show()
    sys.exit(app.exec_())
