## Результати тестування 

Порівняння результатів, отриманих за допомогою методу Монте-Карло, з аналітичним розрахунком за допомогою функції quad з бібліотеки SciPy, показало високу ступінь збігу: 
- аналітичний результат - 0.6667
- методом Монте-Карло - 0.6652 

Різниця методом Монте-Карло склала  0.0015. Така незначна розбіжність свідчить про ефективність методу Монте-Карло для наближеного обчислення визначених інтегралів, особливо коли точне аналітичне обчислення є складним або неможливим.

Важливо зазначити, що точність методу Монте-Карло залежить від кількості використовуваних точок: зі збільшенням кількості точок точність результату збільшується. У нашому випадку, використання 1,000,000 точок дозволило досягти високої точності результатів.

## Висновки
Метод Монте-Карло демонструє свою універсальність та простоту в застосуванні до різноманітних задач обчислювальної математики і фізики, зокрема, до задач інтегрування. Цей метод є особливо цінним у випадках, коли необхідно обчислити інтеграли від складних або високовимірних функцій, де традиційні аналітичні чи чисельні методи можуть виявитися неефективними.

Отже, метод Монте-Карло підтвердив свою ефективність та надійність як інструмент для обчислення визначених інтегралів, пропонуючи при цьому гнучкість та доступність у використанні.