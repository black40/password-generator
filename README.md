# Password Generator (Kivy)

Графическое приложение для генерации надёжных паролей с гибкими настройками.

## Возможности
- Генерация паролей с длиной от 4 до 64 символов
- Выбор состава пароля: буквы, цифры, спецсимволы (чекбоксы)
- Копирование сгенерированного пароля в буфер обмена одной кнопкой
- Автоматический перенос длинных паролей по ширине окна
- Валидация длины и состава пароля
- Совместимость с Windows, Linux, macOS (Kivy)

## Установка
1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/black40/password-generator.git
   cd password-generator
   ```
2. Создайте виртуальное окружение и установите зависимости:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt  # или pip install .
   ```
   Или с помощью [uv](https://github.com/astral-sh/uv):
   ```bash
   uv pip install -r requirements.txt
   ```

## Запуск
```bash
make run
```
или
```bash
python main.py
```

## Тесты
Для запуска юнит-тестов:
```bash
make test
```
или
```bash
python -m unittest discover -s tests
```

## Проверка стиля
Для проверки и автоисправления кода с помощью Ruff:
```bash
make check
make fix
make format
```

## Структура проекта
- `app/gui.py` — основная логика генерации и GUI
- `app/gui.kv` — описание интерфейса Kivy
- `main.py` — точка входа
- `tests/` — юнит-тесты
- `pyproject.toml` — конфигурация зависимостей и инструментов

## Сборка standalone (опционально)
Для создания standalone-приложения используйте PyInstaller или Briefcase (см. документацию Kivy).

---

**Автор:** black40
