from django.shortcuts import render,HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Contact

        
@api_view(['POST'])
def identify_contact(request):
    email = request.data.get('email')
    phoneNumber = request.data.get('phoneNumber')

    
    contacts = Contact.objects.all()  # Checks if a contact already exists with provided email or phoneNumber
    contact = None

    if email in [contact.email for contact in contacts]:
        contact = Contact.objects.filter(email=email).first()
    elif phoneNumber in [contact.phoneNumber for contact in contacts]:
        contact = Contact.objects.filter(phoneNumber=phoneNumber).first()

    if not contact:  # Checks if contact is None
       
        contact = Contact.objects.create(email=email, phoneNumber=phoneNumber) # Create a new primary contact
        return Response({
            "contact": {
                "primaryContactId": contact.id,
                "emails": [contact.email],
                "phoneNumbers": [contact.phoneNumber],  
                "secondaryContactIds": []
            }
        })

    # we gather information about the primary contact
    primary_contact_id = contact.id
    emails = {contact.email}
    phone_numbers = {contact.phoneNumber}
    secondary_contact_ids = set()
    
    
    if (email and email != contact.email) or (phoneNumber and phoneNumber != contact.phoneNumber): # Checks if provided email or phoneNumber is different from the existing contact
      
        existing_secondary_contact = Contact.objects.filter(email=email, phoneNumber=phoneNumber, linkPrecedence='secondary').first()# Checks if a secondary contact already exists with the same email and phoneNumber
        if not existing_secondary_contact:
            # Create a new secondary contact
            new_contact = Contact.objects.create(email=email, phoneNumber=phoneNumber, linkedId=contact, linkPrecedence='secondary')
            secondary_contact_ids.add(new_contact.id)

      
        contact.linkPrecedence = 'secondary'  # Updates the existing contact to become a secondary contact
        contact.save()

   
    linked_contacts = Contact.objects.filter(linkedId=contact.id) # Check for linked contacts and gather their information
    for linked_contact in linked_contacts:
        emails.add(linked_contact.email)
        phone_numbers.add(linked_contact.phoneNumber)
        secondary_contact_ids.add(linked_contact.id)

    return Response({
        "contact": {
            "primaryContactId": primary_contact_id,
            "emails": list(emails),
            "phoneNumbers": list(phone_numbers),
            "secondaryContactIds": list(secondary_contact_ids)
        }
    })


def index(request):
    return HttpResponse("<h1>Hello there! Welcome to my API</h1>")



