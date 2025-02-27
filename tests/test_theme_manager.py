from themecor import ThemeManager


def test_theme_manager_initialization():
    theme_manager = ThemeManager()
    assert theme_manager.console is not None
    assert theme_manager.typer is not None


def test_theme_manager_info_log(capsys):
    theme_manager = ThemeManager()
    theme_manager.info("Test message")
    captured = capsys.readouterr()
    assert "Test message" in captured.out


def test_theme_manager_success_log(capsys):
    theme_manager = ThemeManager()
    theme_manager.success("Test message")
    captured = capsys.readouterr()
    assert "Test message" in captured.out
