# Air Company -- By Derek & Masaki
![project for](https://img.shields.io/badge/DB__Project-Done-brightgreen.svg)
![theme](https://img.shields.io/badge/Black-Gold-yellow.svg)

**This is a final project for CSCI-SHU 213 Databases Class**

- Front-end: Bootstrap, Chart.JS
- Back-end: Python Flask, MySQL, Amazon RDS

### Customer use cases:

After logging in successfully a user(customer) may do any of the following use cases:
- View My flights: Provide various ways for the user to see flights information which he/she purchased.
The default should be showing for the upcoming flights. Optionally you may include a way for the user
to specify a range of dates, specify destination and/or source airport name or city name etc.
- Purchase tickets: Customer chooses a flight and purchase ticket for this flight. You may find it easier
to implement this along with a use case to search for flights.
- Search for flights: Search for upcoming flights based on source city/airport name, destination
city/airport name, date.
- Track My Spending: Default view will be total amount of money spent in the past year and a bar
chart showing month wise money spent for last 6 months. He/she will also have option to specify a
range of dates to view total amount of money spent within that range and a bar chart showing month
wise money spent within that range.
- Logout: The session is destroyed and a “goodbye” page or the login page is displayed.

### Booking agent use cases:
After logging in successfully a booking agent may do any of the following use cases:
- View My flights: Provide various ways for the booking agents to see flights information for which
he/she purchased on behalf of customers. The default should be showing for the upcoming flights.
Optionally you may include a way for the user to specify a range of dates, specify destination and/or
source airport name and/or city name etc to show all the flights for which he/she purchased tickets.
- Purchase tickets: Booking agent chooses a flight and purchases tickets for other customers giving
customer information. You may find it easier to implement this along with a use case to search for
flights.
- Search for flights: Search for upcoming flights based on source city/airport name, destination
city/airport name, date.
- View my commission: Default view will be total amount of commission received in the past 30 days
and the average commission he/she received per ticket booked in the past 30 days and total
number of tickets sold by him in the past 30 days. He/she will also have option to specify a range of
dates to view total amount of commission received and total numbers of tickets sold.
- View Top Customers: Top 5 customers based on number of tickets bought from the booking agent in
the past 6 months and top 5 customers based on amount of commission received in the last year. Show
a bar chart showing each of these 5 customers in x-axis and number of tickets bought in y-axis. Show
another bar chart showing each of these 5 customers in x-axis and amount commission received in yaxis.
- Logout: The session is destroyed and a “goodbye” page or the login page is displayed.

### Airline Staff use cases:
After logging in successfully an airline staff may do any of the following use cases:
- View My flights: Defaults will be showing all the upcoming flights operated by the airline he/she
works for the next 30 days. He/she will be able to see all the current/future/past flights operated by the
airline he/she works for based range of dates, source/destination airports/city etc. He/she will be able
to see all the customers of a particular flight.
- Create new flights: He or she creates a new flight, providing all the needed data, via forms. The
application should prevent unauthorized users from doing this action. Defaults will be showing all the
upcoming flights operated by the airline he/she works for the next 30 days.
- Change Status of flights: He or she changes a flight status (from upcoming to in progress, in progress
to delayed etc) via forms.
- Add airplane in the system: He or she adds a new airplane, providing all the needed data, via forms.
The application should prevent unauthorized users from doing this action. In the confirmation page,
she/he will be able to see all the airplanes owned by the airline he/she works for.
- Add new airport in the system: He or she adds a new airport, providing all the needed data, via
forms. The application should prevent unauthorized users from doing this action.
- View all the booking agents: Top 5 booking agents based on number of tickets sales for the past
month and past year. Top 5 booking agents based on the amount of commission received for the last
year.
- View frequent customers: Airline Staff will also be able to see the most frequent customer within
the last year. In addition, Airline Staff will be able to see a list of all flights a particular Customer has
taken only on that particular airline.
- View reports: Total amounts of ticket sold based on range of dates/last year/last month etc. Month
wise tickets sold in a bar chart.
- Comparison of Revenue earned: Draw a pie chart for showing total amount of revenue earned from
direct sales (when customer bought tickets without using a booking agent) and total amount of revenue
earned from indirect sales (when customer bought tickets using booking agents) in the last month and
last year.
- View Top destinations: Find the top 3 most popular destinations for last 3 months and last year.
- Logout: The session is destroyed and a “goodbye” page or the login page is displayed.
