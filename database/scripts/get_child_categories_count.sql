/*
    Найти количество дочерних элементов первого уровня вложенности для
    категорий номенклатуры.
*/

select
    p.id, p.title, (
        select count(*)
        from Category as c
        where c.parentid = p.id
    )
from Category as p
group by title, p.id