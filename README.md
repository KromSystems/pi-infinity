# 🧮 pi-infinity

> Асинхронный вычислитель числа π (пи) на Python — быстро, эффективно, бесконечно.

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![License](https://img.shields.io/github/license/KromSystems/pi-infinity)
![Python](https://img.shields.io/badge/python-3.8+-blue.svg)

🚀 **pi-infinity** — это современный асинхронный Python-скрипт для высокоточного вычисления числа π с использованием формулы Bailey–Borwein–Plouffe (BBP), многопроцессорной обработки и постепенной записи результата в файл.

---

## 🔍 Особенности

- ✅ **Асинхронная запись** в файл с возможностью дозаписи
- ⚡ Использование `asyncio` и `ProcessPoolExecutor` для максимальной производительности
- 📈 Поддержка **высокой точности** через математическую формулу BBP
- 📁 Возможность продолжения вычислений после остановки
- 📦 Простая установка и запуск

---


```
Вычисляю часть от 0 до 100
Вычисляю часть от 100 до 200
Записываю 200 знаков в файл...
Запись завершена.
```

---

## 📦 Установка

```bash
git clone https://github.com/KromSystems/pi-infinity.git
cd pi-infinity
pip install aiofiles
```

---

## ▶️ Запуск

```bash
python pi-infinity.py
```

Результат будет сохранён в файл `pi_async.txt`.

---

## ⚙️ Настройки

Вы можете изменить количество вычисляемых знаков числа π в функции `main()`:

```python
await write_pi_to_file(filename, total_digits=1000, chunk_size=100)
```

- `total_digits` — общее количество знаков после запятой
- `chunk_size` — размер блока вычислений за один шаг

---

## 🤝 Участие в проекте

Любые улучшения, баг-репорты и идеи приветствуются! Создавайте Issues или Pull Requests.

---

## 📄 Лицензия

MIT License – см. [LICENSE](LICENSE)

---

## 💬 Автор

👤 **KromSystems**


✨ Вычисление числа π должно быть красивым, быстрым и понятным.  
С этим проектом оно таким и станет.  

---

### ❤️ Понравился проект? Поставь звездочку!  
⭐ [Star on GitHub](https://github.com/KromSystems/pi-infinity)
