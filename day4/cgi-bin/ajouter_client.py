#!/usr/bin/env python3
import cgi
import cgitb
import logging
import sys
import os

# Enable CGI debugging
cgitb.enable()

# Configure logging to output to a file
logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Log start of script
logging.info("Starting ajouter_client.py script")

# Add the path to the main project folder where client.py and db.py are located
sys.path.insert(0, r'D:\PYT\DAY4')

# Import modules and log any import errors
try:
    from client import Client
    from db import ajouter_client_bd
    logging.info("Modules imported successfully")
except ImportError as e:
    logging.error(f"Error importing modules: {e}")

# Get data from the form, using default values to handle missing fields
form = cgi.FieldStorage()
nom = form.getvalue('nom', 'Inconnu')  # Default to 'Inconnu' if not provided
email = form.getvalue('email', '')     # Default to empty string if not provided
telephone = form.getvalue('telephone', '')  # Default to empty string if not provided
categorie = form.getvalue('categorie', 'Autre').capitalize()  # Default to 'Autre' if not provided
employes = form.getvalue('employes', '1')

# Log received form data
logging.debug(f"Form data received: nom={nom}, email={email}, telephone={telephone}, categorie={categorie}, employes={employes}")

# Convert 'employes' to an integer and handle any conversion errors
try:
    employes = int(employes)
    logging.info(f"Converted employes to integer: {employes}")
except ValueError:
    logging.warning(f"Value for employes is not a valid integer: {employes}, defaulting to 1")
    employes = 1

# Determine the price per employee based on the category
prix_par_employe = 7 if categorie in ["SEO", "Web"] else 5
logging.debug(f"Price per employee determined: {prix_par_employe}")

# Create the client and add to the database
try:
    client = Client(nom, email, telephone, categorie, employes, prix_par_employe)
    ajouter_client_bd(client)
    logging.info(f"Client {nom} added successfully to the database")
except Exception as e:
    logging.error(f"Error adding client to the database: {e}")

# Send an HTML confirmation response
print("Content-Type: text/html")
print()
print("<html><body>")
print(f"<h1>Client {nom} ajouté avec succès au CRM !</h1>")
print("</body></html>")
