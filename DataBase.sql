create database gestor_gastos;
use gestor_gastos;

create table tipo_gasto (
    id int auto_increment primary key,
    categoria varchar(50) not null,
    cantidad float not null
);
