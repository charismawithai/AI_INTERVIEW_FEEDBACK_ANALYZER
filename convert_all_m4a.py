# import os
# from pydub import AudioSegment

# # List the folders you want to convert
# folders = ["females", "males"]

# # Optional: use full paths if folders are elsewhere
# # folders = [
# #     r"C:\...path...\females",
# #     r"C:\...path...\males"
# # ]

# for input_folder in folders:
#     output_folder = input_folder + "_wav"
#     os.makedirs(output_folder, exist_ok=True)
    
#     for fn in os.listdir(input_folder):
#         if fn.lower().endswith(".m4a"):
#             src = os.path.join(input_folder, fn)
#             dst = os.path.join(output_folder, os.path.splitext(fn)[0] + ".wav")
            
#             audio = AudioSegment.from_file(src, format="m4a")
#             audio.export(dst, format="wav")
#             print(f"✅ Converted {input_folder}/{fn} → {os.path.basename(dst)}")

# print("🎯 All folders converted!")
import os
import shutil

# ⚠️ Replace with the real folder path that contains ffmpeg.exe
ffmpeg_path = r"C:\Users\polot\Downloads\ffmpeg-7.1.1-essentials_build\ffmpeg-7.1.1-essentials_build\bin"
os.environ["PATH"] = ffmpeg_path + os.pathsep + os.environ["PATH"]

# Check if ffmpeg is found now
print("FFmpeg Path Found:", shutil.which("ffmpeg"))


