# 2020201024_Assignment3a

Repo link: <https://github.com/ronitray95/2020201024_Assignment3a.git>

## Question 1

I am keeping all employee IDs in a dict and mapping them to their immediate superiors. Then I am just moving up the level to find their common supervisor.

Assumptions:

- Assuming employee name as `str`.

## Question 2

Here, I have used regex to parse the date components. After that I am simply comparing all the components.

Assumptions:

- Only IST date formats have been considered.

## Question 3

After parsing the JSON, I am converting the times to datetime objects. Then I am looping between the free slots of both employees. The first overlapping interval whose duration is greater than the slot interval is printed.

Assumptions:

- Assuming slot duration in hours with optional fractional part.
