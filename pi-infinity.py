import asyncio
from concurrent.futures import ProcessPoolExecutor
import os

# Формула Bailey–Borwein–Plouffe (BBP) для вычисления n-го шестнадцатеричного знака числа π
def bbp_term(n: int) -> float:
    return (1 / 16**n) * (
        4 / (8*n + 1) -
        2 / (8*n + 4) -
        1 / (8*n + 5) -
        1 / (8*n + 6)
    )

def compute_pi_chunk(start, end):
    """Вычисление части числа Пи с помощью BBP"""
    print(f"Вычисляю часть от {start} до {end}")
    pi = 0.0
    for n in range(start, end):
        pi += bbp_term(n)
    return pi

async def write_pi_to_file(filename: str, total_digits: int = 10_000, chunk_size: int = 100):
    """
    Асинхронная функция для записи числа Пи в файл
    """
    loop = asyncio.get_event_loop()
    file_exists = os.path.exists(filename)

    with open(filename, "a") as f:
        if not file_exists or os.path.getsize(filename) == 0:
            f.write("3.\n")  # Записываем начальные цифры

    async with aiofiles.open(filename, "a") as f:
        tasks = []
        for i in range(0, total_digits, chunk_size):
            start = i
            end = i + chunk_size
            tasks.append(loop.run_in_executor(None, compute_pi_chunk, start, end))

        results = await asyncio.gather(*tasks)

        full_pi = sum(results)
        hex_pi = format(full_pi, ".50f")  # Приближение к десятичному представлению

        # Убираем "3." из начала
        decimal_part = str(hex_pi).replace("3.", "").replace(".", "")[:total_digits]

        print(f"Записываю {len(decimal_part)} знаков в файл...")
        await f.write(decimal_part + "\n")
        print("Запись завершена.")

async def main():
    filename = "pi_async.txt"
    await write_pi_to_file(filename, total_digits=1000, chunk_size=100)

if __name__ == "__main__":
    try:
        import aiofiles
    except ImportError:
        raise SystemExit("Установите aiofiles: pip install aiofiles")

    asyncio.run(main())
