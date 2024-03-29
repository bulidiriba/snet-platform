import addressbook3_pb2 as pb

import sys

# Iterates though all people in the AddressBook and prints info about them

def ListPeople(address_book):
	for person in address_book.people:
		print("Person ID: ", person.id)
		print("Name: ", person.name)
		if person.HasField('email'):
			print("Email address: ", person.email)

		for phone_number in person.phones:
			if phone_number.type == pb.Person.MOBILE:
				print("mobile phone #", )
			elif phone_number.type == pb.Person.HOME:
				print("Home phone #")
			elif phone_number.type == pb.Person.WORK:
				print("Work phone #")
			print(phone_number.number)

# Main Procedure: Reads the entire address book from a file and prints all
# the information inside

if len(sys.argv) != 2:
	print("Usage: ", sys.argv[0], "ADDRESS_BOOK_FILE")
	sys.exit(-1)

address_book = pb.AddressBook()

# Read the existing address Book
f = open(sys.argv[1], "rb")
address_book.ParseFromString(f.read())
f.close()

ListPeople(address_book)