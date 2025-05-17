from PySide6.QtCore import (
    Qt,
    QMimeData,
    QSize,
    QPoint,
)
from PySide6.QtGui import (
    QDragMoveEvent,
    QDragEnterEvent,
    QDropEvent,
    QFont,
    QFontInfo,
    QPainter,
    QFontMetrics,
    QMouseEvent,
    QFontDatabase,
)
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QHBoxLayout,
    QVBoxLayout,
    QListWidget,
    QLabel,
    QLineEdit,
    QFrame,
)

class VerticalLabel(QLabel):

    def __init__(self, *args) -> None:
        super().__init__(*args)
        # self.setSizePolicy(
        #     QSizePolicy.Fixed,
        #     QSizePolicy.Preferred,
        # )

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.translate(0, self.height())
        painter.rotate(-90)
        # calculate the size of the font
        fm = QFontMetrics(painter.font())
        xoffset = int(fm.boundingRect(self.text()).width() / 2)
        yoffset = int(fm.boundingRect(self.text()).height() / 2)
        x = int(self.width() / 2) + yoffset - 3  # 3 is a fudge factor for lower characters
        y = int(self.height() / 2) - xoffset
        # because we rotated the label, x affects the vertical placement, and y affects the horizontal
        painter.drawText(y, x, self.text())
        painter.end()

    def minimumSizeHint(self):
        size = QLabel.minimumSizeHint(self)
        return QSize(size.height(), size.width())

    def sizeHint(self):
        size = QLabel.sizeHint(self)
        return QSize(size.height(), size.width())
