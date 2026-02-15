# WelpAi

**WelpAi** — это мощная и бесплатная библиотека для работы с искусственным интеллектом прямо из терминала или ваших Python-скриптов.

## Установка
```bash
pip install welpai .

Использование
 * Настройка модели:
   welpai set gpt-oss
 * Запрос через консоль:
   welpai ask "Твой вопрос здесь"
Для разработчиков
from welpai import WelpAi
ai = WelpAi()
response = ai.chat("Привет!")
print(response)
1.  Сборка: `python -m build`
2.  Установка: `pip install .`
3.  Тест: `welpai models`

