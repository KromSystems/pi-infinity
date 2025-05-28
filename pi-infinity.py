import asyncio
import os
from concurrent.futures import ProcessPoolExecutor
import time

# BBP formula для вычисления n-го шестнадцатеричного знака числа π
def bbp_term(n: int) -> float:
    return (1 / 16**n) * (
        4 / (8*n + 1) -
        2 / (8*n + 4) -
        1 / (8*n + 5) -
        1 / (8*n + 6)
    )

def compute_pi_chunk(start, end):
    pi = 0.0
    for n in range(start, end):
        pi += bbp_term(n)
    return pi

async def write_pi_to_file(filename: str, digits_per_run: int = 1000, delay: int = 10):
    loop = asyncio.get_event_loop()
    executor = ProcessPoolExecutor()

    iteration = 0
    total_runtime = 0
    start_time = time.time()

    while total_runtime < 2 * 60 * 60:  # 2 часа
        start = iteration * digits_per_run
        end = start + digits_per_run

        print(f"[{iteration}] Вычисляю {digits_per_run} знаков от {start} до {end}")
        result = await loop.run_in_executor(executor, compute_pi_chunk, start, end)

        hex_pi = format(result, ".50f")
        decimal_part = str(hex_pi).replace("3.", "").replace(".", "")[:digits_per_run]

        with open(filename, "a") as f:
            if os.path.getsize(filename) == 0:
                f.write("3.\n")
            f.write(decimal_part + "\n")

        print(f"[{iteration}] Сохранено {digits_per_run} знаков.")
        iteration += 1

        # Небольшая пауза, чтобы не перегружать CPU
        await asyncio.sleep(delay)

        total_runtime = time.time() - start_time

    print("Вычисление завершено за 2 часа.")

async def main():
    filename = "pi_async.txt"
    await write_pi_to_file(filename)

if __name__ == "__main__":
    asyncio.run(main())
