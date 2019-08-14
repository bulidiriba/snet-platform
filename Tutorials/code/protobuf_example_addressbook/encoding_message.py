import addressbook3_pb2 as pb
import sys


def PromptForAddress(person):
	person.id = int(input("Enter person ID number: "))
	person.name = input("Enter name: ")

	email = input("Enter email address (blank for none): ")
	if email != "":
		person.email = email

	while True:
		pnumber = input("Enter a phone number (or leave blank to finish): ")
		if pnumber == "":
			break

		phone_number = person.phones.add()
		phone_number.number = pnumber

		type = input("Is this a mobile, home, or work phone? ")
		if type == "mobile":
			phone_number.type = pb.Person.MOBILE
		elif type == "home":
			phone_number.type = pb.Person.HOME
		elif type == "work":
			phone_number.type = pb.Person.WORK
		else:
			print("unknown phone type leaving as default value")


# Main procedure: Reads the entire address book from a file
# adds one person based on user input, then writes it back out to the same file

if len(sys.argv) != 2:
	print("usage: ", sys.argv[0], "ADDRESS_BOOK_FILE")
	sys.exit(-1)

address_book = pb.AddressBook()

# Read the existing address book.
try:
	f = open(sys.argv[1], "rb")
	address_book.ParseFromString(f.read())
	f.close()
except IOError:
	print(sys.argv[1] + ": Could not open file. creating a new one.")

# Add an address
PromptForAddress(address_book.people.add())


# Write the new address book back to disk
f = open(sys.argv[1], "ab")
f.write(address_book.SerializeToString())
f.close()
