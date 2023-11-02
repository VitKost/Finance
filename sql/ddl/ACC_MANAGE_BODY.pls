create or replace PACKAGE BODY            ACC_MANAGE AS

  PROCEDURE INS_ACCOUNT (in_account_id VARCHAR2, in_account_name VARCHAR2, in_account_description VARCHAR2, in_currency VARCHAR2) IS
    BEGIN
      insert into ACCOUNTS (
        account_id,
        account_name,
        account_description,
        currency ) 
      values (
        in_account_id,
        in_account_name,
        in_account_description,
        in_currency );
      exception
        when others then
          raise_application_error (-20010, 'Error ' || sqlerrm);
    END;

END ACC_MANAGE;