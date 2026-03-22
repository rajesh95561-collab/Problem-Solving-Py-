import requests
class IRCTC:
    def __init__(self):
        user_input = input("""How would you like to proceed?
        1. Enter 1 to check live train status.
        2. Enter 2 to check PNR
        3. Enter 3 to check train schedule
        """)
        if user_input == "1":
            print("Demo: Live train status feature not implemented yet.")
        elif user_input == "2":
            print("Demo: PNR feature not implemented yet.")
        elif user_input == "3":
            self.train_scedule()
        else:
            print("wrong input")
            self.__init__()
    def train_scedule(self):
        train_number = input("Enter train number: ")
        self.fetch_data(train_number)
    def fetch_data(self,train_number):
        data = requests.get("https://indianrailapi.com/api/v2/TrainSchedule/apikey/30c382602bfa67c8a7c580e6cfe2becb/TrainNumber/{}".format(train_number))
        data = data.json()
        print(data["Route"])
        for item in data["Route"]:
            print(item["StationName"])
train = IRCTC()
