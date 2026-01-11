create database gestor_gastos;
use gestor_gastos;

create table tipo_gasto (
    id int auto_increment primary key,
    categoria varchar(50) not null,
    cantidad float not null,
    descripcion varchar(70),
    fecha date
);

select * from tipo_gasto;

select * from tipo_gasto where categoria = "cafe";

delete from tipo_gasto where id = 4;

UPDATE tipo_gasto
SET categoria = "cafe", cantidad = 100000
WHERE id = 4;
