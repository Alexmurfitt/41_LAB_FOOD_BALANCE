-- 📊 CONSULTAS AVANZADAS PARA NUTRIAPP

-- 1. Ver los alimentos registrados ordenados por kcal:
SELECT nombre, kcal, proteinas, carbohidratos, grasas
FROM alimentos
ORDER BY kcal DESC;

-- 2. Consultar los micronutrientes de un alimento específico:
SELECT a.nombre AS alimento, m.nombre AS micronutriente, m.cantidad_mg
FROM alimentos a
JOIN micronutrientes m ON a.id = m.alimento_id
WHERE a.nombre = 'Avena';

-- 3. Resumen nutricional de una comida específica:
SELECT c.nombre, c.fecha, a.nombre AS alimento, ca.cantidad_g, ca.total_kcal, ca.total_protein, ca.total_carbs, ca.total_fat
FROM comidas c
JOIN comida_alimentos ca ON c.id = ca.comida_id
JOIN alimentos a ON a.id = ca.alimento_id
WHERE c.nombre = 'Comida 1';

-- 4. Totales diarios por fecha:
SELECT c.fecha,
       SUM(ca.total_kcal) AS kcal,
       SUM(ca.total_protein) AS proteinas,
       SUM(ca.total_carbs) AS carbohidratos,
       SUM(ca.total_fat) AS grasas
FROM comidas c
JOIN comida_alimentos ca ON c.id = ca.comida_id
GROUP BY c.fecha
ORDER BY c.fecha DESC;

-- 5. Totales semanales (agrupado por semana ISO):
SELECT WEEK(c.fecha, 1) AS semana,
       YEAR(c.fecha) AS anio,
       SUM(ca.total_kcal) AS kcal,
       SUM(ca.total_protein) AS proteinas,
       SUM(ca.total_carbs) AS carbohidratos,
       SUM(ca.total_fat) AS grasas
FROM comidas c
JOIN comida_alimentos ca ON c.id = ca.comida_id
GROUP BY anio, semana
ORDER BY anio DESC, semana DESC;

-- 6. Alimentos más ricos en proteínas:
SELECT nombre, proteinas
FROM alimentos
ORDER BY proteinas DESC
LIMIT 10;

-- 7. Comparar macros de un día con objetivos:
SELECT o.fecha,
       o.kcal AS obj_kcal, SUM(ca.total_kcal) AS real_kcal,
       o.proteinas AS obj_prot, SUM(ca.total_protein) AS real_prot,
       o.carbohidratos AS obj_carb, SUM(ca.total_carbs) AS real_carb,
       o.grasas AS obj_fat, SUM(ca.total_fat) AS real_fat
FROM objetivos o
JOIN comidas c ON o.fecha = c.fecha
JOIN comida_alimentos ca ON c.id = ca.comida_id
WHERE o.fecha = '2025-04-06'
GROUP BY o.fecha;

-- 8. Alimentos según etiqueta:
SELECT c.etiqueta, SUM(ca.total_kcal) AS kcal, SUM(ca.total_protein) AS proteinas
FROM comidas c
JOIN comida_alimentos ca ON c.id = ca.comida_id
GROUP BY c.etiqueta
ORDER BY kcal DESC;

-- 9. Buscar alimentos ricos en un micronutriente:
SELECT a.nombre, m.nombre AS micro, m.cantidad_mg
FROM micronutrientes m
JOIN alimentos a ON a.id = m.alimento_id
WHERE m.nombre LIKE '%hierro%'
ORDER BY m.cantidad_mg DESC;

-- 10. Crear vista de resumen diario (opcional):
CREATE VIEW resumen_diario AS
SELECT c.fecha,
       SUM(ca.total_kcal) AS kcal,
       SUM(ca.total_protein) AS proteinas,
       SUM(ca.total_carbs) AS carbohidratos,
       SUM(ca.total_fat) AS grasas
FROM comidas c
JOIN comida_alimentos ca ON c.id = ca.comida_id
GROUP BY c.fecha;
