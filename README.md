# UK Driving Test Finder


This is a simple python script that integrates with Pushover (https://pushover.net/)


This requires a `.env` file with this structure in the same directory as the `TestFinder.py`: 
```
DRIVING_LICENSE_NUMBER = ''
DRIVING_TEST_REFERENCENUMBER = ''
POSTCODE = ''
API_TOKEN = ''
API_USER = ''
```

### Quick Start :


1. Head to https://pushover.net/ and make an account
2. Create an application, all the way at the bottom of dashboard
3. Copy the API key into the `API_TOKEN` Field on the `.env` file
4. Then create a subscription group from the application (in red below)
![image](https://github.com/user-attachments/assets/bd64d259-b425-4a37-8deb-7d13def68230)
5. Then share the link with whoever needs it.
6. Copy the Group Key from the Delivery Group Dashboard (in red below) into the `API_USER` Field on the `.env` file
![image](https://github.com/user-attachments/assets/c9573221-4ecb-40df-82ae-86d2e99209f6)
7. Run `TestFinder.py`
8. Hopefully Profit


### Contributions/Help

Open an issue with any help ill try to reply quickly.

If you notice any improvments that i can make to this, please open an issue and i will look at it. 
