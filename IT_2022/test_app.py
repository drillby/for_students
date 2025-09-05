import pytest
from PyQt5.QtCore import Qt

from app.main import MainWindow


@pytest.fixture
def window(qtbot):
    w = MainWindow()
    qtbot.addWidget(w)
    w.show()
    return w


def test_elements_visible_and_enabled(window):
    assert window.input_field.isVisible()
    assert window.show_button.isVisible()
    assert window.display_label.isVisible()
    assert window.input_field.isEnabled()
    assert window.show_button.isEnabled()


def test_placeholder_text(window):
    assert window.input_field.placeholderText() == "Enter text here..."


def test_text_flow_click(window, qtbot):
    window.input_field.setText("Ahoj")
    from PyQt5.QtCore import Qt

    qtbot.mouseClick(window.show_button, Qt.LeftButton)
    assert window.display_label.text() == "Ahoj"


def test_direct_call(window):
    window.input_field.setText("Přímo")
    window.show_text()
    assert window.display_label.text() == "Přímo"


def test_layout_and_size(window):
    assert window.layout is not None
    assert window.sizeHint().width() >= 200
    assert window.input_field.sizeHint().height() > 0
