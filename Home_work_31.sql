-- Лысые злодеи 90-х годов
SELECT name, first_appearance, APPEARANCES
FROM MarvelCharacters
WHERE HAIR = 'Bald' AND align = 'Bad Characters' 
AND year BETWEEN 1990 AND 1999;

-- Герои с тайной идентичностью и необычными глазами
SELECT name, year, EYE 
FROM MarvelCharacters
WHERE identify = 'Secret Identity' AND EYE NOT IN ('Blue Eyes', 'Brown Eyes', 'Green Eyes') AND year IS NOT NULL;

-- Персонажи с изменяющимся цветом волос
SELECT name, hair 
FROM MarvelCharacters
WHERE hair = 'Variable Hair';

-- Женские персонажи с редким цветом глаз
SELECT name, EYE 
FROM MarvelCharacters
WHERE SEX = 'Female Characters' 
AND EYE IN ('Gold Eyes', 'Amber Eyes');

-- Персонажи без двойной идентичности, сортированные по году появления
SELECT name, first_appearance 
FROM MarvelCharacters
WHERE identify = 'No Dual Identity' 
ORDER BY year DESC;

-- Герои и злодеи с необычными прическами
SELECT name, align, hair 
FROM MarvelCharacters
WHERE hair NOT IN ('Brown Hair', 'Black Hair', 'Blond Hair', 'Red Hair')
AND align IN ('Good Characters', 'Bad Characters');

-- Персонажи, появившиеся в определённое десятилетие
SELECT name, first_appearance 
FROM MarvelCharacters
WHERE year BETWEEN 1960 AND 1969;

-- Персонажи с уникальным сочетанием цвета глаз и волос
SELECT name, eye, hair 
FROM MarvelCharacters
WHERE eye = 'Yellow Eyes' 
AND hair = 'Red Hair';

-- Персонажи с ограниченным количеством появлений
SELECT name, appearances 
FROM MarvelCharacters
WHERE appearances < 10;

-- Персонажи с наибольшим количеством появлений
SELECT name, appearances 
FROM MarvelCharacters
ORDER BY appearances DESC 
LIMIT 5;