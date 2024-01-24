--PostgreSQL database
create schema if not exists "accounting"
    authorization postgres;
create schema if not exists "trading"
    authorization postgres;

drop table if exists accounting.accounts_owners;
drop table if exists trading.trade;
drop table if exists accounting.accounts;
drop table if exists trading.exchange_rate;

create table accounting.account
(
    account_id varchar(10) not null,
    account_name varchar(20) not null unique,
    account_description varchar(40),
    create_date timestamp default current_timestamp,
    update_date timestamp default current_timestamp,
    currency varchar(3) not null,
    currency_amount float4 default 0.0 not null,

    constraint account_pk primary key (account_id)
);

create table accounting.account_owner
(
    account_id varchar(10) not null unique,
    owner_name varchar(20) not null,
    owner_country_residence varchar(2) not null,
    birth_date timestamp not null,
    create_date timestamp default current_timestamp,
    update_date timestamp default current_timestamp,

    constraint accounts_owners_fk foreign key (account_id) references accounting.account (account_id)
);

create table trading.trade
(
    trade_id bigint not null,
    account_id varchar(10) not null,
    trade_type varchar(10) not null,
    trade_amount float4 not null,
    trade_currency varchar(3) not null,
    effective_date timestamp default current_timestamp,
    update_date timestamp default current_timestamp,

    constraint trades_pk primary key (trade_id),
    constraint trades_fk foreign key (account_id) references accounting.account (account_id)
);

create table trading.exchange_rate
(
    from_currency varchar(3) not null,
    to_currency varchar(3) not null,
    rate float4 not null,
    effective_date timestamp default current_timestamp,
    update_date timestamp default current_timestamp,

    constraint exchange_rates_un unique (from_currency, to_currency, effective_date)
);

  create or replace procedure accounting.ins_account(in_account_id varchar, in_account_name varchar, in_account_description varchar, in_currency varchar)
  language plpgsql
  as $$
  	declare
    begin
      insert into accounting.account (
        account_id,
        account_name,
        account_description,
        currency )
      values (
        in_account_id,
        in_account_name,
        in_account_description,
        in_currency );
    end; $$

