from basics import db,Puppy

db.create_all()

sam = Puppy('Sammy',3)
frank = Puppy('Franky',4)

db.session.add_all([sam,frank])

db.session.commit()

print(sam.id)
print(sam.name)
