import datetime

import schedule


def cuckoo(mes, quiet):
    sleep = list(map(int, quiet.split('-')))

    dt = datetime.datetime.now()
    i = datetime.datetime.timetuple(dt)[3]
    if not sleep[0] <= i <= sleep[1]:
        i = i % 12 if i % 12 else 12
        print(mes * i)


message = input()
silence = input()
schedule.every().hour.at(":00").do(cuckoo, message, silence)

while True:
    schedule.run_pending()
