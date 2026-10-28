def save_transcript_text(text: str, output_path: str = "transcript_log.txt") -> None:
    """文字起こしされたテキストをファイルに追記（上書きなし）保存する"""
    with open(output_path, mode="a", encoding="utf-8") as f:
        f.write(text + "\n")