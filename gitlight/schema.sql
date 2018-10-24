drop table if exists user;
create table user (
  user_id integer primary key autoincrement,
  username text not null,
);

drop table if exists repositories;
create table repositories (
  user_id integer primary key autoincrement,
  repository_name text not null,
);

drop table if exists pullrequests;
create table pullrequests (
  pr_id integer primary key autoincrement,
  author_id integer not null,
  text text not null,
  pub_date integer not null,
  src_repo integer not null,`
  dst_repo integer not null,`
);
