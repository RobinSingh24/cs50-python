from datetime import date
import inflect
import sys
p = inflect.engine()

def main():

    input_date = input("Date of Birth: ")
    dob = Season(input_date)
    print(dob.minutes_passed())

class Season:

    def __init__(self,time):
        if not time:
            raise Exception("Invalid date")
        try:
            year, month, day = time.split('-')
            self.dob = date.fromisoformat(f"{year}-{month}-{day}")

        except ValueError:
            sys.exit('Invalid date')

    def minutes_passed(self):
        today = date.today()
        difference = round((today-self.dob).total_seconds()/60)
        return (p.number_to_words(difference, andword="").capitalize() + ' minutes')

if __name__ == "__main__":
    main()






