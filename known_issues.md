# Известные проблемы

## Баг №1: перепутаны is_even и is_odd

**Статус:** Open
**Категория:** Major

**Описание:**
Функции is_even и is_odd возвращают противоположный результат.
is_even возвращает True для нечётных чисел, is_odd — для чётных.

**Как воспроизвести:**
1. Запустить pytest -v
2. Упадут 4 теста:
   - TestParity::test_even
   - TestParity::test_odd
   - TestFilterEvenOdd::test_even
   - TestFilterEvenOdd::test_odd

**Ожидаемое поведение:**
is_even(4) -> True
is_odd(3)  -> True

**Фактическое поведение:**
is_even(4) -> False
is_odd(3)  -> False

**Причина:**
В is_even условие `n % 2 != 0`, в is_odd условие `n % 2 == 0`.