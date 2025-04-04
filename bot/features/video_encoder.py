import subprocess

async def encode_video(input_path: str, quality: str):
    output_path = f"encoded_{quality}.mp4"
    cmd = f"ffmpeg -i {input_path} -vf scale=1280:720 {output_path}"
    subprocess.run(cmd, shell=True, check=True)
    return output_path
