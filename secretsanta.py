import os
import smtplib
from random import seed
from random import randint

EMAIL_ADDRESS = 'myemailaddress@email.com'
EMAIL_PASSWORD = 'myemailpassword123'


def sendEmail(toEmail, secretSanta)
    with smtplib.SMTP('smtp.office365.com', 587) as smtp:
        smtp.ehlo() #identify with the mail server
        smtp.starttls() #encrypt traffic
        smtp.ehlo()

        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

        subject = 'Your Secret Santa! '
        body = 'Your secret santa is .... ' + secretSanta

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(EMAIL_ADDRESS, toEmail, msg)
    
def get_contacts(filename):

    names = []
    senderEmails = []
    senderNames = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            senderNames.append(a_contact.split()[0])
            senderEmails.append(a_contact.split()[1])
    return names, senderNames, senderEmails

def generate_random(name, names) :
    seed()
    rand = randint(0, len(names)-1)
    while name == names[rand] :
        rand = randint(0, len(names)-1)
        
    return rand
    
def main() :
    names, senderNames, senderEmails = get_contacts('emails.txt')
    for name in senderNames :
        seed(1)
        index = generate_random(name, names)
        fromName = name;
        toName = names[index]
        fromEmail = senderEmails[senderNames.index(fromName)]
        toEmail = senderEmails[senderNames.index(toName)]
        print(fromName + " (" + fromEmail + ") ---> " + toName + " (" + toEmail + ")")
        names.remove(names[index])


if __name__ == '__main__' :
    main()
