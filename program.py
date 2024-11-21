import webbrowser
import time
import random
import sys
# import pyautogui -> why is this module not loading?


try:
    
    def run_for_duration(duration):
        print(f"Running for {duration} seconds...")

        start_time = time.time()

        # Open the initial UFC URL
        webbrowser.open(initial_url)
        time.sleep(2)


        while (time.time() - start_time) < duration:
            random_url = random.choice(url_list)
            webbrowser.open(random_url)
            print(f"Opened URL: {random_url}")
            time.sleep(2) 

        print(f"Stopping after {run_duration} seconds...")

    if __name__ == "__main__":
        run_duration = 5
        password = "PCName69"
        initial_url = "https://www.ufc.com/"
        url_list = ["https://hiphopdx.com/release-dates", "https://en.wikipedia.org/wiki/Fight_Club", "https://www.wwe.com/"]

        print("     New Python Program:     ")

        while True:
            input_password = input("Enter your Password: ")
            if len(input_password) >= 8 and (any(char.isalpha() for char in input_password) or any(char.isnumeric() for char in input_password)):
                if input_password == password:
                    run_for_duration(run_duration)
                    print("URLs opened successfully!")
                    break
            else:
                print("Incorrect password")
except KeyboardInterrupt:
    sys.exit(0)




