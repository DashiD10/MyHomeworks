-- Задание 1
-- Общее количество персонажей по статусу
SELECT ALIVE, count(*)
FROM MarvelCharacters
GROUP BY ALIVE;

-- Задание 2
-- Среднее количество появлений персонажей с разным цветом глаз
SELECT EYE as color, avg(APPEARANCES)
FROM MarvelCharacters
GROUP BY EYE;

-- Задание 3
-- Максимальное количество появлений у персонажей с определенным цветом волос
SELECT HAIR as color, max(APPEARANCES)
FROM MarvelCharacters
GROUP BY HAIR;

-- Задание 4
-- Минимальное количество появлений среди персонажей с известной и публичной личностью
SELECT identify, min(APPEARANCES)
FROM MarvelCharacters
WHERE identify = 'Public Identity'
GROUP BY identify;

-- Задание 5
-- Общее количество персонажей по полу
SELECT SEX as name, count(*)
FROM MarvelCharacters
GROUP BY SEX;

-- Задание 6
-- Средний год первого появления персонажей с различным типом личности
SELECT identify, avg(Year)
FROM MarvelCharacters
GROUP BY identify;

-- Задание 7
-- Количество персонажей с разным цветом глаз среди живых
SELECT EYE as color, count(*)
FROM MarvelCharacters
WHERE ALIVE = 'Living Characters'
GROUP BY EYE;

-- Задание 8
-- Максимальное и минимальное количество появлений среди персонажей с определенным цветом волос
SELECT HAIR as color, max(APPEARANCES), min(APPEARANCES)
FROM MarvelCharacters
GROUP BY HAIR;

-- Задание 9
-- Количество персонажей с различным типом личности среди умерших
SELECT identify, count(*)
FROM MarvelCharacters
WHERE ALIVE = 'Deceased Characters'
GROUP BY identify;

-- Задание 10
-- Средний год первого появления персонажей с различным цветом глаз
SELECT EYE as color, avg(Year)
FROM MarvelCharacters
GROUP BY EYE;

-- Задание 11
-- Персонаж с наибольшим количеством появлений
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE APPEARANCES = (SELECT max(APPEARANCES) FROM MarvelCharacters);

-- Задание 12
-- Персонажи, впервые появившиеся в том же году, что и персонаж с максимальными появлениями
SELECT name, Year
FROM MarvelCharacters
WHERE Year = (
    SELECT Year 
    FROM MarvelCharacters 
    WHERE APPEARANCES = (SELECT max(APPEARANCES) FROM MarvelCharacters)
);

-- Задание 13
-- Персонажи с наименьшим количеством появлений среди живых
SELECT name, APPEARANCES
FROM MarvelCharacters
WHERE ALIVE = 'Living Characters' 
AND APPEARANCES = (
    SELECT min(APPEARANCES) 
    FROM MarvelCharacters 
    WHERE ALIVE = 'Living Characters'
);

-- Задание 14
-- Персонажи с определенным цветом волос и максимальными появлениями среди такого цвета
SELECT name, HAIR as color, APPEARANCES
FROM MarvelCharacters
WHERE (HAIR, APPEARANCES) IN (
    SELECT HAIR, max(APPEARANCES)
    FROM MarvelCharacters
    GROUP BY HAIR
);

-- Задание 15
-- Персонажи с публичной личностью и наименьшим количеством появлений
SELECT name, identify, APPEARANCES
FROM MarvelCharacters
WHERE identify = 'Public Identity'
AND APPEARANCES = (
    SELECT min(APPEARANCES)
    FROM MarvelCharacters
    WHERE identify = 'Public Identity'
);






