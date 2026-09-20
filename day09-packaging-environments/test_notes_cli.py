from notes_cli import count_notes, main


def test_count_notes(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("buy milk\nwalk dog\n\nfinish homework\n")
    assert count_notes(path) == 3


def test_count_notes_ignores_blank_lines(tmp_path):
    path = tmp_path / "notes.txt"
    path.write_text("\n\none\n\n")
    assert count_notes(path) == 1


def test_main_prints_count(tmp_path, capsys):
    path = tmp_path / "notes.txt"
    path.write_text("one\ntwo\n")
    main([str(path)])
    captured = capsys.readouterr()
    assert "2 notes found" in captured.out
