
/*
    2.1. Получение информации о сумме товаров заказанных под каждого клиента
    (Наименование клиента, сумма)
*/

select c.clientname, COALESCE(sum(n.price * i.amount), 0) as total
from client c
left join orders o on c.id = o.clientid
left join orderitem i on i.orderid = o.id
left join nomenclature n on n.id = i.nomenclatureid
group by c.clientname
