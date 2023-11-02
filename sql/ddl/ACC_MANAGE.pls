create or replace PACKAGE            ACC_MANAGE AS 

    PROCEDURE INS_ACCOUNT (in_account_id VARCHAR2, in_account_name VARCHAR2, in_account_description VARCHAR2, in_currency VARCHAR2);
    
    
END ACC_MANAGE;