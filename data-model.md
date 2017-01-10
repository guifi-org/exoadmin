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

# Subscriber data

extends identified

- [boolean] is subscription active? (is redundant, but helps to do a quick filter)
- `user`: link to Identified user
- [boolean] `org_member`: distinguishes between a organization member or just a subscriber/client
- [list of pairs of] `start_subs` and `end_subs`: list of start and end

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

# Activity data

- Lists of activities

# ? Compensation activity (idea)

- node URL
- `hours` work hours valor numèric: hores de feina (que pels informes es convertiran a 30 euros segons fundació)
text: descripció de la feina (detall)
valor numèric: € d'inversió
text: descripció de l'inversió en € (detall)
usuaris participants

# Professional data

- ? invoicing data

# IPs

- id - assigned to (circuit)
- address
- type: (IPv4, IPv6)

# Tasks

- User can register
