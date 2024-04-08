class SupportTicket:
    def __init__(self, ticket_id, staff_id, name, email, description):
        self.ticket_id = ticket_id
        self.staff_id = staff_id
        self.name = name
        self.email = email
        self.description = description
        self.response = "Not Yet Provided"
        self.status = "Open"

    def __str__(self):
        return f"Ticket ID: {self.ticket_id}\nName: {self.name}\nStaff ID: {self.staff_id}\nEmail: {self.email}\nDescription: {self.description}\nResponse: {self.response}\nStatus: {self.status}"


class HelpdeskSystem:
    ticket_id = 2000
    open_tickets = 0
    closed_tickets = 0
    tickets = []

    def submit_ticket(self, staff_id, name, email, description):
        new_ticket = SupportTicket(HelpdeskSystem.ticket_id, staff_id, name, email, description)
        self.tickets.append(new_ticket)
        HelpdeskSystem.ticket_id += 1
        HelpdeskSystem.open_tickets += 1
        if "Password Change" in description:
            new_ticket.response = f"New Password: {staff_id[:2]}{name[:3]}"
            HelpdeskSystem.closed_tickets += 1
            HelpdeskSystem.open_tickets -= 1
            new_ticket.status = "Closed"
        return new_ticket

    def respond_to_ticket(self, ticket_id, response):
        for ticket in HelpdeskSystem.tickets:
            if ticket.ticket_id == ticket_id:
                ticket.response = response
                if ticket.status == "Open" and "Password Change" in ticket.description:
                    HelpdeskSystem.closed_tickets += 1
                    HelpdeskSystem.open_tickets -= 1
                    ticket.status = "Closed"
                elif ticket.status == "Closed":
                    HelpdeskSystem.open_tickets += 1
                    HelpdeskSystem.closed_tickets -= 1
                    ticket.status = "Reopened"

    def display_ticket(self, ticket_id):
        for ticket in HelpdeskSystem.tickets:
            if ticket.ticket_id == ticket_id:
                print(ticket)

    def display_statistics(self):
        print(
            f"Number of tickets submitted: {HelpdeskSystem.ticket_id - 2000}\nNumber of open tickets: {HelpdeskSystem.open_tickets}\nNumber of closed tickets: {HelpdeskSystem.closed_tickets}")


def main():
    helpdesk_system = HelpdeskSystem()

    # Submitting tickets
    ticket1 = helpdesk_system.submit_ticket("123456", "John Smith", "johnsmith@hotmail.com", "Password Change")
    ticket2 = helpdesk_system.submit_ticket("654321", "Jane Doe", "janedoe@gmail.com", "Network Connection Issue")
    ticket3 = helpdesk_system.submit_ticket("789012", "Bob Johnson", "bjohnson@yahoo.com", "Application Error")

    # Displaying ticket statistics
    helpdesk_system.display_statistics()

    # Resolving tickets
    helpdesk_system.respond_to_ticket(ticket1.ticket_id, "Your password has been changed.")
    helpdesk_system.respond_to_ticket(ticket2.ticket_id, "Your network connection issue has been resolved.")

    # Reopening a resolved ticket
    helpdesk_system.respond_to_ticket(ticket1.ticket_id, "Actually, I still need help.")

    # Displaying tickets
    helpdesk_system.display_ticket(ticket1.ticket_id)
    helpdesk_system.display_ticket(ticket2.ticket_id)
    helpdesk_system.display_ticket(ticket3.ticket_id)

    # Displaying ticket statistics again
    helpdesk_system.display_statistics()


main()
