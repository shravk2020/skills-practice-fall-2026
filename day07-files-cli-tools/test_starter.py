import json
from starter import parse_args, load_records, summarize, main


def test_parse_args_reads_positional_input_path():
    args = parse_args(["data.json"])
    assert args.input_path == "data.json"


def test_load_records_json(tmp_path):
    path = tmp_path / "data.json"
    path.write_text(json.dumps([{"category": "bug"}, {"category": "feature"}]))
    records = load_records(path)
    assert records == [{"category": "bug"}, {"category": "feature"}]


def test_load_records_csv(tmp_path):
    path = tmp_path / "data.csv"
    path.write_text("category,priority\nbug,1\nfeature,2\n")
    records = load_records(path)
    assert records == [
        {"category": "bug", "priority": "1"},
        {"category": "feature", "priority": "2"},
    ]


def test_summarize():
    records = [{"category": "bug"}, {"category": "bug"}, {"category": "feature"}]
    assert summarize(records) == {"bug": 2, "feature": 1}


def test_summarize_empty():
    assert summarize([]) == {}


def test_main_prints_sorted_summary(tmp_path, capsys):
    path = tmp_path / "data.json"
    path.write_text(json.dumps([
        {"category": "feature"}, {"category": "bug"}, {"category": "bug"},
    ]))
    main([str(path)])
    captured = capsys.readouterr()
    assert captured.out.strip().splitlines() == ["bug: 2", "feature: 1"]
