from audio_record import audio_record_10sec
from audio_transcript import transcribe_file
from save_transcript import save_transcript_text

def main():
    # 1. 録音処理を実行し、出力されたファイルパスを取得
    audio_file_path = audio_record_10sec()
    
    if not audio_file_path:
        print("録音処理に失敗したため、文字起こしを中止します。")
        return

    # 2. ファイルパスを渡して文字起こし
    text = transcribe_file(audio_file_path)
    print(f"文字起こし結果: {text}")
    
    # 3. テキストファイルへ追記保存
    save_transcript_text(text)

if __name__ == "__main__":
    main()