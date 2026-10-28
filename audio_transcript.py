import mlx_whisper
from pydub import AudioSegment
import numpy as np

# 音声ファイルを指定して文字起こし
audio_file_path = "python-audio-output.wav"

def transcribe_file(file_path: str) -> str:
    """音声ファイルパスを指定して文字起こし結果(文字列)を返す"""
    result = mlx_whisper.transcribe(
        file_path, 
        path_or_hf_repo="mlx-community/whisper-base-mlx"
    )
    return result["text"]