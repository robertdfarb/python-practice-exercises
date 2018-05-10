def main():

    birthdays = {'Albert Einstain': '02/01/1921',
                'Robert Farber':  '03/01/2004',
                'Benjamin Franklin' : '01/01/2018'}

    print ("Welcome to the Birthday Dictionary, we know the Birthdays of:")

    for birthday in birthdays.keys():
        print (birthday)

    name = input("Who's birthday do you want to lookup? ")

    if name in birthdays:
        print ("{name}'s birthday is {bd}".format(name = name, bd = birthdays[name]))
    else:
        print("Sorry we couldn't find that birthday!")

if __name__ =='__main__':
    main()

