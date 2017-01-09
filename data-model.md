# User data

buit-in

- username
- password
- first name
- last name
- email

# Location

- Municipality
- Place

# Identified

extends user

requires that first name, last name and email is valid

requires Location app

- `user`: link to user
- `address`: street address
- `identity`: identity document
- `place`
- `postal_code`
- `user_type`: type of person: individual / organization 

# Subscriber data

extends identified

- `user`: link to legal user
- [boolean] `orgmember`: distinguishes between a organization member or just a subscriber/client
- [list of pairs of] `startsubs` and `endsubs`: list of start and end

# Organization data

- fullname
- `bankacc`: bank account
- ? [category/title] board members (all of them with inscription date)
    - `president`: associated with particular legal user
    - `treasurer`: associated with particular legal user
    - `secretary`: associated with particular legal user
    - [list] `others`: other members, able to add new custom ones. associated with particular user
- ? password storage goes here?


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
