import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('cred.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()
# print(data)


def get_sales_data():
    """
    Get data
    """
    while True:
        print("Please enter sales data")
        print("Example: 10,20,30,40,50,60\n")
        data_str = input("Enter your data here: ")

        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print('Data OK')
            break
    return sales_data

def validate_data(values):
    """
    input validator
    """
    try:
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exaxly 6 values required. You provided {len(values)} values")
    except ValueError as e:
        print("======================================================")
        print(f"Invalid data {e} \n")
        print("======================================================")
        return False
    return True

def update_sales_worksheet(data):
    """
    update google workhsheet
    """
    print('Updating sales worksheet ... \n')
    sales_worksheet = SHEET.worksheet('sales')
    sales_worksheet.append_row(data)
    print('Updated succesfully \n')


data = get_sales_data()
sales_data = [int(num) for num in data]
update_sales_worksheet(sales_data)