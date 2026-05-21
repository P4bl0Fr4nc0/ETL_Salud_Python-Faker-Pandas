CREATE DATABASE Salud;
Use Salud;

Select * From expedientes_salud;

Select * From expedientes_salud WHERE Nivel_Prioridad = 'Alta';

SELECT
    Institucion,

    COUNT(*) AS Total_Expedientes,

    MIN(Dias_Espera) AS Espera_Minima,

    MAX(Dias_Espera) AS Espera_Maxima,

    ROUND(AVG(Dias_Espera),2) AS Espera_Promedio

FROM expedientes_salud

GROUP BY Institucion

ORDER BY Espera_Promedio DESC;