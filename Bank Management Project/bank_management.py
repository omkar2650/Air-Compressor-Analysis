def menu():
    print("*****Welcome*****\n")
    print("Create a bank account\n")


def new_acc():
    with open("bank.json", "a") as file:
        for i in range(0, 1):
            name = input("Enter your Name: \n")
            file.write("name: " + name + "\n")
            date_of_birth = input("Enter your date of birth: \n")
            file.write("DOB: " + date_of_birth + "\n")
            citizenship_number = input("citizenship number: \n")
            file.write("citizenship number: " + citizenship_number + "\n")
            address = input("Enter your address: \n")
            file.write("address: " + address + " \n")
            phone_number = input("Enter your phone number: \n")
            file.write("phone_number: " + phone_number + " \n")
            amount = input("Enter the amount to deposit: \n")
            file.write("amount: " + amount + " \n")
            print("Select the type of account: \n"
                  "1.saving \n"
                  "2.current \n"
                  "3.Fixed for one year \n"
                  "4.Fixed for two year  \n"
                  "5.Fixed for three year \n")

            type_of_account = input("Enter the type of account: \n")
            file.write("type of account: " + type_of_account + " \n\n")

# def view_list():
    # print("")


menu()
new_acc()
# view_list()
