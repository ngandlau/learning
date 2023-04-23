## GroupBy vs Window Functions

```sql
SELECT 
    customer_id, 
    SUM(revenue)
FROM table
GROUP BY customer_id;

SELECT 
    customer_id,
    SUM(revenue) OVER (PARTITION BY customer_id)
FROM table;
```

GroupBy collapses $N_i$ rows of group $i$ to a single row. Window functions preserves all rows. That allows you to take other columns with you: 

```sql
-- doesnt work, can only select columns that are in group by
SELECT customer_id, first_name, last_name, SUM(revenue) GROUP BY customer_id;
-- works
SELECT customer_id, first_name, last_name, SUM(revenue) OVER (PARTITION BY customer_id); 
```

## Cumulative Sum

```
SELECT
    customer_id,
    SUM(revenue) OVER (PARTITION BY customer_id
                       ORDER BY purchase_date
                       RANGE BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW)
                    -- ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
FROM table;
```

ROWS/RANGE/GROUPS depends on the behavior that you want.

Suppose the customer ordered two times on the same day:
    * Do you want the cumulative sum over each day? Then RANGE is what you want.
    * Do you want the cumulative sum over each purchase? Then ROWS is what you want.

RANGE produces:

|purchase_id|customer_id| purchase_date| revenue | cum_revenue |
|-|-|-|-|
|1|1|2023-01-01|10€|15€
|2|1|2023-01-01|5€|15€
|3|1|2023-01-02|20€|35€

ROWS produces:

|purchase_id|customer_id| purchase_date| revenue | cum_revenue |
|-|-|-|-|
|1|1|2023-01-01|10€|10€
|2|1|2023-01-01|5€|15€
|3|1|2023-01-02|20€|35€



