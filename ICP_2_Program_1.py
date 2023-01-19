class Name:

    def Fullname(self, FirstName, LastName):
        print(first_name + ' ' + last_name)

    def string_alternative(self):
        old_str = input("Enter a string: ")
        new_str = ""
        for i in range(len(old_str)):
            if i % 2 == 0:
                new_str = new_str + old_str[i]
        print(new_str)


first_name = input("Enter FirstName: ")
last_name = input("Enter LastName: ")


def main():
    Objname = Name()
    Objname.Fullname(first_name, last_name)
    Objname.string_alternative()


if __name__ == "__main__":
    main()




