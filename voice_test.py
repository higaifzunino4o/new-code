import os
import gtts
from pydub import AudioSegment

tts=gtts.gTTS(text="В целом, конечно, экономическая повестка сегодняшнего дня.", lang="ru")

tts.save("text1.wav")

sound = AudioSegment.from_mp3("text1.mp3")
sound.export("TELEGRAM_BOT/text1.wav", format="wav")