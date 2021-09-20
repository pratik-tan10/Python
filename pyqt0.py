import sys
from PyQt5.QtWidgets import QApplication, QDialog
 
app = QApplication(sys.argv)
 
window = QDialog()
window.setGeometry(500, 300, 300, 200)
window.setWindowTitle('GUI Window')
window.show()
 
sys.exit(app.exec_())
