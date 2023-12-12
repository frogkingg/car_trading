from blockchain import Blockchain
from car_sharing import Owner, Car, Customer

def show_balance(cust_balance, owner_balance):
    print("Customer balance: %s" % (cust_balance,))
    print("Owner balance: %s" % (owner_balance,))

def show_rental_cost(cost):
    print("Rental cost: ", cost)

def start():
    blockchain = Blockchain()
    customer = Customer(50000)
    owner = Owner(50000)
    eth = 50

    show_balance(customer.balance, owner.balance)

    #1 Deploy Contract
    owner.deploy(eth, blockchain)

    #2 Book Car
    customer.request_book(eth, blockchain)

    #3 Add Car to Rent
    options = {'label0': 'BMJSER_alfa-romero giulia', 'value0': 13495,
                  'label1': 'YEORFT_audi 100 ls', 'value1': 13950,
                  'label2': 'FWIBH1_bmw 320i', 'value2': 16430,
                  'label3': 'KWMFOR_chevrolet impala', 'value3': 5155,
                  'label4': 'L3YIVX_dodge rampage', 'value4': 5572,
                  'label5': 'VO35Q7_honda civic', 'value5': 6475,
                  'label6': 'KAS1Q7_isuzu MU-X', 'value6': 6784,
                  'label7': 'ST9XPG_jaguar xj', 'value7': 3228,
                  'label8': 'JOMZA0_maxda rx3', 'value8': 5198}
    # car = "Ferrari"
    days_no = 1
    owner.add_car_to_rent(options['value2'], options['label2'])
    customer.pass_number_of_days(days_no)
    # No blockchain transaction needed here unless the car adding process involves financial transactions

    #4 Encrypt and Store Details
    owner.encrypt_and_store_details(blockchain)
    owner.allow_car_usage()

    #5 Access Car
    customer.access_car()
    # No blockchain transaction needed here unless access involves a financial transaction

    #6 End Car Rental
    customer.end_car_rental()

    #7 Withdraw Earnings and Retrieve Balance
    owner.withdraw_earnings()
    customer.retrieve_balance()

    show_rental_cost(options['value2']*days_no)
    show_balance(customer.balance, owner.balance)

if __name__ == '__main__':
    start()
