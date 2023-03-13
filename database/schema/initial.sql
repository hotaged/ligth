create table if not exists Stuff (
    id serial primary key,
    title varchar not null,
    amount integer not null,
    price float not null
);

create table if not exists Category (
    id serial primary key,
    title varchar not null
);

create table if not exists Client (
    id serial primary key,
    name varchar not null,
    address varchar not null
);

create table if not exists Orders (
    id serial primary key,
    clientId integer not null,

    FOREIGN KEY (clientId) REFERENCES Client(id) ON DELETE CASCADE
)