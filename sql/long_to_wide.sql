DROP TABLE IF EXISTS tmp_table;
CREATE TABLE tmp_table (
	tag TEXT,
	verkehrsart TEXT,
	kante TEXT,
	n_zuege INT
);

INSERT INTO tmp_table (tag, verkehrsart, kante, n_zuege)
VALUES
('montag', 'fv', '(a,b)', 10),
('montag', 'nv', '(a,b)', 20),
('montag', 'gv', '(a,b)', 30),
('dienstag', 'fv', '(a,b)', 1),
('dienstag', 'nv', '(a,b)', 5),
('dienstag', 'gv', '(a,b)', 9);

select
	tag,
	kante,
	case when verkehrsart = 'fv' then n_zuege end as n_zuege_fv,
	case when verkehrsart = 'nv' then n_zuege end as n_zuege_nv,
	case when verkehrsart = 'gv' then n_zuege end as n_zuege_gv
from tmp_table;

select
	tag,
	kante,
	max(case when verkehrsart = 'fv' then n_zuege end) as n_zuege_fv,
	max(case when verkehrsart = 'nv' then n_zuege end) as n_zuege_nv,
	max(case when verkehrsart = 'gv' then n_zuege end) as n_zuege_gv
from tmp_table
group by tag, kante;


------

DROP TABLE IF EXISTS tmp_table;
CREATE TABLE tmp_table (
	tag TEXT,
	modellzug_id INT,
	kante TEXT
);

INSERT INTO tmp_table (tag, modellzug_id, kante)
VALUES
('montag', 1, '(a,b)'),
('montag', 1, '(a,b)'),
('montag', 8, '(a,b)'),
('dienstag', 1, '(a,b)'),
('dienstag', 8, '(a,b)'),
('dienstag', 8, '(a,b)');

SELECT * FROM tmp_table;

select
	tag,
	kante,
	case when modellzug_id IN (1, 2) then 1 end as n_zuege_fv,
	case when modellzug_id IN (8, 9) then 1 end as n_zuege_nv
from tmp_table;

select
	tag,
	kante,
	SUM(case when modellzug_id IN (8, 9) then 1 end) as n_zuege_nv,
	SUM(case when modellzug_id IN (1, 2) then 1 end) as n_zuege_fv
from tmp_table
group by tag, kante;

select
	tag,
	kante,
	MAX(case when modellzug_id IN (8, 9) then COUNT(*) end) as n_zuege_nv,
	MAX(case when modellzug_id IN (1, 2) then COUNT(*) end) as n_zuege_fv
from tmp_table
group by tag, kante, modellzug_id;


