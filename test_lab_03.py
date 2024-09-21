import pytest
import sys
from importlib import reload

@pytest.mark.parametrize("run_lab03", [("20", "5")], indirect=True)
def test_gems_per_player(run_lab03) -> None:
    assert "4" in run_lab03

@pytest.mark.parametrize("run_lab03", [("9", "4")], indirect=True)
def test_remainder(run_lab03) -> None:
    assert "1" in run_lab03

@pytest.mark.parametrize("run_lab03", [("23", "2"), ("7", "3")], indirect=True)
def test_formatting(run_lab03) -> None:
    table_lines = run_lab03.strip().split("\n")
    for line in table_lines[-4:]:
        assert len(line) == 19, "Table formatting doesn't match exactly"

@pytest.fixture
def run_lab03(request, capsys, monkeypatch):
    global lab03
    try:
        inputs = iter(request.param)
        monkeypatch.setattr("builtins.input", lambda _: next(inputs))
        if "lab03" not in sys.modules:
            import lab03
        else:
            reload(lab03)

        out, err = capsys.readouterr()
        assert err == "", err

        return out

    except ImportError as e:
        assert False, "lab03.py not found, check your filename!"