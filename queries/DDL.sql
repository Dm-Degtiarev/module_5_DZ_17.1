CREATE TABLE public.customers_data (
	customer_id varchar(20) null,
	company_name varchar(200) null,
	contact_name varchar(200) null
);

CREATE TABLE public.employees_data (
	first_name varchar(50) null,
	last_name varchar(50) null,
	title varchar(50) null,
	birth_date date null,
	notes text null
);

CREATE TABLE public.orders_data (
	order_id int4 null,
	customer_id varchar(20) null,
	employee_id int4 null,
	order_date date null,
	ship_city varchar(150) null
);