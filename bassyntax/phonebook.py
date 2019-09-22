emails_list = {
    "adis": "adis@mail.com",
    "sarah": "sarah@mail.com" 
}

open = True

while open: 
    print("Valkommen till epostkatalogen!")
    choice = input("Lägg till (L), stäng (S) eller hämta (H)?   ").lower()

    if choice == 'h':
        email_name = input("Vems epost vill du leta efter?  ").lower()

        if email_name in emails_list:
            print(emails_list[email_name])
        else:
            print("Tyvarr fanns inte " + email_name + " i katalogen.")
    elif choice == 'l':
        name = input("Ange namn:    ").lower()
        epost = input("Ange epost:     ").lower()
        emails_list[name] = epost
        print("Lade till " + name + ": " + epost)
    elif choice == 's':
        print("Hej då!")
        break
    else:
        print("Välj H eller L nästa gång.")
