create or replace function get_count (p_customer_id int)
returns int
language plpgsql
as $$
declare 
    total_orders int;
begin 
    select count(*) into total_orders
    from orders 
    where customer_id = p_customer_id;

    return total_orders; 
end; 
$$;

select get_count(6);
-- //------------------------------------------------
create or replace function get_category (p_product_id int)
returns varchar(50)
language plpgsql
as $$
declare 
    cat_name varchar(50);
begin 
    select c.category_name into cat_name
    from products p
    left join categories c on p.category_id = c.category_id
    where p.product_id = p_product_id;

    return cat_name; 
end; 
$$;

select get_category(8);

-- //------------------------------------------

create or replace procedure add_cust (
    pro_customer_name varchar(20),
    pro_contact_name varchar(20),
    pro_address varchar(20)
)
language plpgsql
as $$
begin 
    insert into customers (customer_name, contact_name, address)
    values (pro_customer_name, pro_contact_name, pro_address);
end;
$$;
call add_cust('Rahmaismail', 'Rahmahh', '12 Nile St');
-- //--------------------------------------------
create or replace procedure update_category (
    p_product_id int,
    p_category_id int
)
language plpgsql
as $$
begin 
    update products
    set category_id = p_category_id
    where product_id = p_product_id;
end;
$$;
call update_category(8, 2);
-- //---------------------------------------
create or replace function prevent_delete_category()
returns trigger
language plpgsql
as $$
begin
   
    if exists (select * from products where category_id = old.category_id) then
        raise exception 'cannot delete category';
    end if;

    return old; 
end;
$$;

create trigger trg_prevent_delete_category
before delete on categories
for each row
execute function prevent_delete_category();
-- //--------------------------------------------------
create or replace view products_with_price as
select 
    product_id,
    product_name,
    price,
    case
        when price < 50 then 'cheap'
        when price between 50 and 100 then 'moderate'
        when price > 100 then 'expensive'
    end as price_label
from products;
select * from products_with_price;
-- //--------------------------------------------------------
create or replace view customer_order_cnt as
select 
    c.customer_id,
    c.customer_name,
    count(o.order_id) as total_orders
from customers c
left join orders o on c.customer_id = o.customer_id
group by c.customer_id, c.customer_name;
select * from customer_order_cnt;
-- //-----------------------------------------------------------
create index idx
on orders(customer_id);
-- //-------------------------------------------------

create unique index uni_idx
on categories(category_name);
-- //-----------------------------------------
    begin;
        insert into customers (customer_name, contact_name, address, city, postal_code, country)
        values ('rahmah', 'rahmaismail', '12 Nile St', 'Cairo', '12345', 'Egypt');

        insert into orders (customer_id, order_date)
        values (
            (select customer_id from customers where customer_name = 'rahmah'),
            current_date
        );

        rollback;
-- //--------------------------------------------------------
select *
from customers
where customer_id in (
    select o.customer_id
    from orders o
    join order_details od on o.order_id = od.order_id
    join products p on od.product_id = p.product_id
    where p.category_id = 2
);
-- //----------------------------------------------------------------
create or replace function calc_revenue(p_product_id int)
returns decimal(10,2)
language plpgsql
as $$
declare
    total_revenue decimal(10,2);
begin
    select coalesce(sum(od.quantity * p.price),0) into total_revenue
    from order_details od
    join products p on od.product_id = p.product_id
    where od.product_id = p_product_id;

    return total_revenue;
end;
$$;
select calc_revenue(8);
-- //----------------------------------------------
create or replace view top_customers_by_quantity as
select 
    c.customer_id,
    c.customer_name,
    sum(od.quantity) as total_quantity
from customers c
join orders o on c.customer_id = o.customer_id
join order_details od on o.order_id = od.order_id
group by c.customer_id, c.customer_name
order by total_quantity desc
limit 5;
select * from top_customers_by_quantity;
-- //------------------------------------------------
select *
from products
where product_id not in (
    select  product_id
    from order_details
);
-- //--------------------------------------------------------------
create role readonly;
grant select on customers, orders to readonly;

create user rahmah with password 'admin&&';
grant readonly to rahmah;

revoke readonly from rahmah;
//---------------------------------------