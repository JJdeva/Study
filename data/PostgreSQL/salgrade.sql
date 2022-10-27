CREATE TABLE if not exists scott.BONUS
(
    ENAME VARCHAR(10),
    JOB VARCHAR(9),
    SAL numeric,
    COMM numeric
) ;

CREATE TABLE if not exists scott.SALGRADE
( 
    GRADE numeric not null CONSTRAINT PK_SALGRADE PRIMARY KEY,
    LOSAL numeric,
    HISAL numeric 
);

INSERT INTO scott.SALGRADE VALUES 
    (1,700,1200),
    (2,1201,1400),
    (3,1401,2000),
    (4,2001,3000),
    (5,3001,9999);