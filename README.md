# 2020201024_Assignment3b

Repo link: <https://github.com/ronitray95/2020201024_Assignment3a.git>

## Question 1

I am keeping all employee IDs in a dict and mapping them to their immediate superiors. Then I am just moving up the level to find their common supervisor.

Part B - Just added a loop. Line no. changes - `29-56`.

Assumptions:

- Assuming employee name as `string` type.
- For input, I am assuming the employee names are `space` separated and the number of employees is not provided.

## Question 2

Here, I have used regex to parse the date components. After that I am simply comparing all the components.

Part B - Line numbers changed - `25-38` and `56-81`. Only the regex part has been changed and some minor formatting for the date components. Using a `try-catch` fallthrough if the first regex fails. If the date format is provided a simple swapping procedure is performed.

Assumptions:

- Only IST date formats have been considered.
- Two dates may not be of same format.
- Date format is provided ONLY for abiguous dates.

## Question 3

After parsing the JSON, I am converting the times to datetime objects. Then I am looping and storing the free slots of all employees. The first overlapping interval whose duration is greater than the slot interval is printed.

Part B - I am storing and modifying the overlapping free slots of all employees one by one. At the end the first slot which is greater or equal to the duration is diplayed. Line numbers changed - `18-27` and `76-87`.

Assumptions:

- Assuming slot duration in hours with optional fractional part.
- Assuming all employee files are in same directory as `.py` file and are of the format `Employee{x}.txt`, `x` starting from 1.
