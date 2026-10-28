#標準モジュール
import time

#外部モジュール
import ffmpeg

# 録音時間（秒）
DURATION = 10

# 出力ファイル名
OUTPUT_FILE = "python-audio-output.wav"


def audio_record_10sec() -> str:
    """マイクから音声を10秒間録音して WAV ファイルに保存し、ファイルパスを返す。"""
    try:
        print(f"{DURATION}秒間、マイクからの録音を開始します...")

        (
            ffmpeg.input(":0", format="avfoundation", t=DURATION)
            .output(OUTPUT_FILE, acodec="pcm_s16le", ar="44100", ac=1)
            .run(overwrite_output=True)
        )

        print(f"録音が完了しました。{OUTPUT_FILE}に保存されました。")
        return OUTPUT_FILE

    except ffmpeg.Error as error:
        stderr = error.stderr
        if stderr:
            print(f"FFmpeg エラーが発生しました: {stderr.decode()}")
        else:
            print(f"FFmpeg エラーが発生しました: {error}")
        return ""
    except Exception as error:
        print(f"予期せぬエラーが発生しました: {error}")
        return ""