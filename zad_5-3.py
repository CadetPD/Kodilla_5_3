
from faker import Faker
fake = Faker('pl_PL')

class BaseContact:
    def __init__(self, first_name, last_name, priv_mobile, e_mail):
        self.first_name, self.last_name, self.priv_mobile, self.e_mail= first_name, last_name, priv_mobile, e_mail
    
    @property
    def label_lenght(self):
        return len(self.last_name) + len(self.first_name) + 1

    def __str__(self):
        return f"\nImię i nazwisko: {self.first_name} {self.last_name} \nNumer prywatny: {self.priv_mobile} \nAdres email: {self.e_mail}"

    def contact(self):
        return f"\nWybieram numer {self.priv_mobile} i dzwonię do {self.first_name} {self.last_name}.\n ---"

class BusinessContact(BaseContact):
    def __init__(self, occupation, company, work_mobile, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.occupation, self.company, self.work_mobile = occupation, company, work_mobile

    @property
    def label_lenght(self):
        return len(self.last_name) + len(self.first_name) + 1  
        
    def __str__(self):
        return f"\nImię i nazwisko: {self.first_name} {self.last_name} \nFirma: {self.company} \nStanowisko: {self.occupation} \nNumer służbowy: {self.work_mobile} \n{self.e_mail}"

    def contact(self):
        return f"\nWybieram numer {self.work_mobile} i dzwonię do {self.first_name} {self.last_name}.\n ---"

def create_contacts(num, card_type):
    cards = []
    for i in range(num):
        if card_type == 1:
            cards.append(BaseContact(first_name = fake.first_name(), last_name = fake.last_name(), priv_mobile = fake.phone_number(), e_mail=fake.email())) 
        elif card_type == 2:
            cards.append(BusinessContact(first_name = fake.first_name(), last_name = fake.last_name(), priv_mobile = fake.phone_number(), occupation = fake.job(), company = fake.company(), work_mobile = fake.phone_number(), e_mail=fake.email()))
    return cards

cards = create_contacts(3,2)

for card in cards:
    print(card, f"\nlabel_lenght: {card.label_lenght}")
    print(card.contact())
    