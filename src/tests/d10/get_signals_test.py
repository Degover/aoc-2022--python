from src.d10.get_signals import *
from src.tests.utils.file_stub import FileStub
from src.tests.d10.example import example


def test_getSignals_WithExample_ShouldBeCorrect():
    file_stub = FileStub()
    file_stub.set_array(example)

    result = list(get_signals(file_stub))

    sample = [
        value for value in result if value[1] in [20, 60, 100, 140, 180, 220]]

    assert sample == [(21, 20), (19, 60), (18, 100),
                      (21, 140), (16, 180), (18, 220)]
