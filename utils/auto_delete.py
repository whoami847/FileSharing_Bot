import asyncio
import os

async def delete_file(file_path: str, delay: int):
    await asyncio.sleep(delay)
    if os.path.exists(file_path):
        os.remove(file_path)
