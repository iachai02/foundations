# SQL Curriculum

Two phases: LeetCode SQL 50 → DataLemur. Do not skip.
Problems build on each other — basic SELECT before window functions, always.

Note on dialect: Problems are in MySQL on LeetCode. After each problem, I'll note the Postgres and/or SQL Server equivalent if the syntax differs. Both dialects matter.

Legend: ✅ done | 🔁 in SRS queue | ⬜ not started

---

## Phase 1 — LeetCode SQL 50

### Section 1: SELECT

| # | Problem | Key Concept | LC # | Status |
|---|---------|-------------|------|--------|
| 1 | Recyclable and Low Fat Products | WHERE with AND | 1757 | ⬜ |
| 2 | Find Customer Referee | NULL handling (IS NULL, <> vs !=) | 584 | ⬜ |
| 3 | Big Countries | OR vs UNION performance | 595 | ⬜ |
| 4 | Article Views I | Self-join basics | 1148 | ⬜ |
| 5 | Invalid Tweets | String functions (LENGTH/LEN) | 1683 | ⬜ |

---

### Section 2: Basic Joins

| # | Problem | Key Concept | LC # | Status |
|---|---------|-------------|------|--------|
| 6 | Replace Employee ID With Unique Identifier | LEFT JOIN, NULL in result | 1378 | ⬜ |
| 7 | Product Sales Analysis I | INNER JOIN, multi-table | 1068 | ⬜ |
| 8 | Customer Who Visited but Did Not Make Any Transactions | LEFT JOIN + IS NULL anti-join | 1581 | ⬜ |
| 9 | Rising Temperature | Self-join with date comparison | 197 | ⬜ |
| 10 | Average Time of Process per Machine | Self-join + aggregation | 1661 | ⬜ |
| 11 | Employee Bonus | LEFT JOIN + NULL filtering | 577 | ⬜ |
| 12 | Students and Examinations | CROSS JOIN + LEFT JOIN + COUNT | 1280 | ⬜ |
| 13 | Managers with at Least 5 Direct Reports | Self-join + HAVING | 570 | ⬜ |
| 14 | Confirmation Rate | LEFT JOIN + AVG + CASE | 1934 | ⬜ |

---

### Section 3: Basic Aggregate Functions

| # | Problem | Key Concept | LC # | Status |
|---|---------|-------------|------|--------|
| 15 | Not Boring Movies | WHERE + ORDER BY | 620 | ⬜ |
| 16 | Average Selling Price | Weighted average with JOIN | 1251 | ⬜ |
| 17 | Project Employees I | AVG with JOIN | 1075 | ⬜ |
| 18 | Percentage of Users Attended a Contest | COUNT + subquery | 1633 | ⬜ |
| 19 | Queries Quality and Percentage | AVG + CASE inside aggregate | 1211 | ⬜ |
| 20 | Monthly Transactions I | GROUP BY multiple columns + CASE | 1193 | ⬜ |
| 21 | Immediate Food Delivery II | Conditional aggregation | 1174 | ⬜ |
| 22 | Game Play Analysis IV | Subquery + DATE arithmetic | 550 | ⬜ |

---

### Section 4: Sorting and Grouping

| # | Problem | Key Concept | LC # | Status |
|---|---------|-------------|------|--------|
| 23 | Number of Unique Subjects Taught by Each Teacher | COUNT DISTINCT | 2356 | ⬜ |
| 24 | User Activity for the Past 30 Days I | DATE filtering + COUNT DISTINCT | 1141 | ⬜ |
| 25 | Product Sales Analysis III | Subquery in WHERE | 1070 | ⬜ |
| 26 | Classes More Than 5 Students | HAVING | 596 | ⬜ |
| 27 | Find Followers Count | GROUP BY + ORDER BY | 1729 | ⬜ |
| 28 | Biggest Single Number | MAX with HAVING | 619 | ⬜ |
| 29 | Customers Who Bought All Products | COUNT DISTINCT + HAVING = total | 1045 | ⬜ |

---

### Section 5: Advanced Select and Joins

| # | Problem | Key Concept | LC # | Status |
|---|---------|-------------|------|--------|
| 30 | The Number of Employees Which Report to Each Employee | Self-join + aggregate | 1731 | ⬜ |
| 31 | Primary Department for Each Employee | CASE + GROUP BY edge case | 1789 | ⬜ |
| 32 | Triangle Judgement | CASE expression | 610 | ⬜ |
| 33 | Consecutive Numbers | Self-join ×3 or LAG/LEAD | 180 | ⬜ |
| 34 | Product Price at a Given Date | Subquery + MAX date | 1164 | ⬜ |
| 35 | Last Person to Fit in the Bus | Running sum + subquery | 1204 | ⬜ |
| 36 | Count Salary Categories | UNION ALL + CASE | 1907 | ⬜ |

---

### Section 6: Subqueries

| # | Problem | Key Concept | LC # | Status |
|---|---------|-------------|------|--------|
| 37 | Employees Whose Manager Left the Company | NOT IN / NOT EXISTS | 1978 | ⬜ |
| 38 | Exchange Seats | CASE + MOD | 626 | ⬜ |
| 39 | Movie Rating | UNION + subquery | 1341 | ⬜ |
| 40 | Restaurant Growth | Window function (SUM OVER) | 1321 | ⬜ |
| 41 | Friend Requests II: Who Has the Most Friends | UNION ALL + GROUP BY | 602 | ⬜ |
| 42 | Investments in 2016 | Correlated subquery | 585 | ⬜ |
| 43 | Department Top Three Salaries | Window function (DENSE_RANK) | 185 | ⬜ |

---

### Section 7: Advanced String Functions / Regex / Clause

| # | Problem | Key Concept | LC # | Status |
|---|---------|-------------|------|--------|
| 44 | Fix Names in a Table | CONCAT + UPPER + LOWER + SUBSTRING | 1667 | ⬜ |
| 45 | Patients With a Condition | LIKE with pattern | 1527 | ⬜ |
| 46 | Delete Duplicate Emails | DELETE with self-join | 196 | ⬜ |
| 47 | Second Highest Salary | LIMIT/OFFSET or subquery | 176 | ⬜ |
| 48 | Group Sold Products By The Date | GROUP_CONCAT / STRING_AGG | 1484 | ⬜ |
| 49 | List the Products Ordered in a Period | WHERE + GROUP BY + HAVING | 1327 | ⬜ |
| 50 | Find Users With Valid E-Mails | REGEXP / LIKE | 1517 | ⬜ |

---

## Phase 2 — DataLemur (Medium+)

Start after completing SQL 50. Focus on company-tagged problems.
Priority order: window functions → CTEs → complex joins → optimization.

Source: https://datalemur.com/

| # | Problem | Company | Key Concept | Status |
|---|---------|---------|-------------|--------|
| 51 | Page With No Likes | Facebook | LEFT JOIN anti-join | ⬜ |
| 52 | Unfinished Parts | Tesla | LEFT JOIN + IS NULL | ⬜ |
| 53 | Laptop vs Mobile Viewership | New York Times | CASE + SUM | ⬜ |
| 54 | Average Post Hiatus | Facebook | DATE_DIFF + GROUP BY | ⬜ |
| 55 | Teams Power Users | Microsoft | COUNT + DATE filter | ⬜ |
| 56 | Duplicate Job Listings | Linkedin | COUNT + HAVING | ⬜ |
| 57 | Cities With Completed Trades | Robinhood | JOIN + GROUP BY | ⬜ |
| 58 | Average Review Ratings | Amazon | GROUP BY month + AVG | ⬜ |
| 59 | App Click-Through Rate | Facebook | CASE + SUM + division | ⬜ |
| 60 | Second Day Confirmation | TikTok | self-join + DATE diff | ⬜ |
| 61 | User's Third Transaction | Uber | ROW_NUMBER window fn | ⬜ |
| 62 | Sending vs. Opening Snaps | Snapchat | CASE + SUM + GROUP BY | ⬜ |
| 63 | Tweets' Rolling Averages | Twitter | AVG OVER (sliding window) | ⬜ |
| 64 | Highest-Grossing Items | Amazon | RANK + PARTITION BY | ⬜ |
| 65 | Top 5 Artists | Spotify | DENSE_RANK + CTE | ⬜ |
| 66 | Signup Activation Rate | TikTok | Correlated subquery | ⬜ |
| 67 | Vacation Destinations | Airbnb | CTE + multi-step filter | ⬜ |
| 68 | Active User Retention | Facebook | LAG + self-join | ⬜ |
| 69 | FAANG Stock Min-Max | Google | MIN/MAX + PARTITION BY | ⬜ |
| 70 | Median Google Search Frequency | Google | PERCENTILE_CONT / MEDIAN | ⬜ |

---

## Key Concepts Tracker

### Window Functions (priority #1)
- [ ] ROW_NUMBER — unique rank per partition
- [ ] RANK — same rank for ties, gaps after
- [ ] DENSE_RANK — same rank for ties, no gaps
- [ ] LAG / LEAD — access previous/next row
- [ ] SUM OVER — running total
- [ ] AVG OVER (sliding) — rolling average with ROWS BETWEEN
- [ ] PARTITION BY vs ORDER BY in OVER clause
- [ ] ROWS BETWEEN vs RANGE BETWEEN

### CTEs
- [ ] Basic WITH clause
- [ ] Chained CTEs
- [ ] Recursive CTEs (hierarchy / graph traversal)

### Postgres vs SQL Server Differences
- DATE functions: `DATE_TRUNC` (PG) vs `DATETRUNC`/`DATEPART` (SS)
- String agg: `STRING_AGG` (both, but syntax differs)
- Top N: `LIMIT` (PG) vs `TOP` (SS)
- Regex: `~` operator (PG) vs `LIKE` / no native regex (SS)
- Upsert: `ON CONFLICT` (PG) vs `MERGE` (SS)
