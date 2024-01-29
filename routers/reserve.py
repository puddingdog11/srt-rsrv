from models.ticket import Ticket
from .main import app

@app.post("/reserve")
def post_reserve(ticket: Ticket):
    return ticket
