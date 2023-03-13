create table if not exists Category (
    id serial primary key,
    title varchar not null,
    parentId integer null,

    FOREIGN KEY(parentId) REFERENCES Category(id) ON DELETE CASCADE
);

create table if not exists Nomenclature (
    id serial primary key,
    title varchar not null,
    amount integer not null,
    price float not null,
    categoryId integer null,

    FOREIGN KEY(categoryId) REFERENCES Category(id) ON DELETE SET NULL
);

create table if not exists Client (
    id serial primary key,
    clientName varchar not null,
    address varchar not null
);


create table if not exists Orders (
    id serial primary key,
    clientId integer not null,

    FOREIGN KEY (clientId) REFERENCES Client(id) ON DELETE CASCADE
);


create table if not exists OrderItem (
    nomenclatureId integer not null,
    orderId integer not null,
    amount integer not null,

    FOREIGN KEY (nomenclatureId) REFERENCES Nomenclature(id),
    FOREIGN KEY (orderId) REFERENCES Orders(id)
)