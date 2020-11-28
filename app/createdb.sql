create table users(
  id integer primary key,
  name varchar(255),
  email varchar(255) unique,
  password varchar(300),
  created_at timestamp
);

create table budget(
  id integer primary key,
  name varchar(255),
  amount float,
  created_at timestamp,
  user_id integer,
  FOREIGN KEY(user_id) REFERENCES users(id)
);

create table expense(
  id integer primary key,
  description text,
  amount float,
  category varchar(255),
  created_at timestamp,
  budget_id integer,
  FOREIGN KEY(budget_id) REFERENCES budget(id)
);

create table income(
  id integer primary key,
  description text,
  amount float,
  category varchar(255),
  created_at timestamp,
  budget_id integer,
  FOREIGN KEY(budget_id) REFERENCES budget(id)
);
