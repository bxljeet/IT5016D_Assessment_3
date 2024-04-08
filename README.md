 Helpdesk System
 
This is a Python program that simulates a basic helpdesk system. The program includes two classes, SupportTicket and HelpdeskSystem.

SupportTicket Class
The SupportTicket class represents a single support ticket submitted by a user. It has the following attributes:

ticket_id: A unique identifier for the ticket
staff_id: The ID of the staff member who is handling the ticket
name: The name of the user who submitted the ticket
email: The email address of the user who submitted the ticket
description: A brief description of the issue being reported
response: The response provided by the staff member
status: The status of the ticket, either "Open" or "Closed"
The class also has a __str__ method that returns a string representation of the ticket's attributes.

HelpdeskSystem Class
The HelpdeskSystem class represents the entire helpdesk system. It has the following attributes:

ticket_id: A static variable that keeps track of the next available ticket ID
open_tickets: The number of currently open tickets
closed_tickets: The number of closed tickets
tickets: A list that contains all submitted tickets
The class has the following methods:

submit_ticket
This method creates a new SupportTicket object with the given parameters, adds it to the tickets list, and increments the ticket_id and open_tickets counters. If the ticket's description contains the string "Password Change", it sets the ticket's response to a new password generated from the staff ID and user name, and sets the ticket's status to "Closed". It then returns the new SupportTicket object.

respond_to_ticket
This method searches for the ticket with the given ticket ID and updates its response attribute with the provided response. If the ticket's status is "Open" and its description contains the string "Password Change", it sets the ticket's status to "Closed" and updates the open_tickets and closed_tickets counters accordingly. If the ticket's status is "Closed", it sets the status to "Reopened" and updates the open_tickets and closed_tickets counters accordingly.

display_ticket
This method searches for the ticket with the given ticket ID and prints its string representation.

display_statistics
This method prints the total number of tickets submitted, the number of open tickets, and the number of closed tickets.

Main Function
The main function creates a new HelpdeskSystem object and uses it to submit three support tickets, display the ticket statistics, resolve two tickets, reopen one ticket, display all three tickets, and display the ticket statistics again.
