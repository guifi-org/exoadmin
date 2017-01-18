Note: *default type is string*

# User data

buit-in

- username
- password
- first name
- last name
- email

# Location

- Municipality that contains `municipality`
- Place that contains `place` and a foreign key to Municipality

# Identified

extends User

TODO: requires that first name, last name and email is valid

requires Location

- `user`: link to User
- `address`: street address
- `identity`: identity document
- `place`: links to Location
- `postal_code`
- [choice] `user_type`: type of person: individual / organization 
- `payment_means`: different ways to pay
- `IBAN`: bank account number in case that payment means is direct debit

# Service

- `name`: name of service
- `description`: description of service

# Subscriber data

extends identified
info: user can have different subscriptions even of the same type. Manager should check that it makes sense

- [boolean] is subscription active? (is redundant, but helps to do a quick filter)
- `user`: link to Identified user
- `service`: link to Service
- `interface`: list of Interfaces
- [date] `start_subs`: start subscription of service
- [date] `end_subs`: end subscription of service (optional)
- `notes`: add notes related to this service-user

# IP

- [ipv4/ipv6 field] address (IPv4, IPv6)

# Interface protocol

- `name`: name of the interface protocol

# Interface

- `IP`: link to IP
- `proto`: link to interface protocol
- `local address`
- `remote address`

# sandbox start here

# ? Action -> ledger?

- `name`: name of action

# ? Activity -> ledger?

- `title`
- ? user or users?
- [date] `date`:
- [number] hours
- `notes`: add notes related to hours
- [number] money
- `notes`: add notes related to money
- map to project?

# Organization data

- fullname
- `bankacc`: bank account
- ? [category/title] board members (all of them with inscription date)
    - `president`: associated with particular legal user
    - `treasurer`: associated with particular legal user
    - `secretary`: associated with particular legal user
    - [list] `others`: other members, able to add new custom ones. associated with particular user
- ? password storage goes here?

# End of average clarity


# ? Compensation activity (idea)

- node URL
- `hours` work hours valor numèric: hores de feina (que pels informes es convertiran a 30 euros segons fundació)
text: descripció de la feina (detall)
valor numèric: € d'inversió
text: descripció de l'inversió en € (detall)
usuaris participants

# Professional data

- ? invoicing data

# Tasks

- User can register
