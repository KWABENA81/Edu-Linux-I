from collections import defaultdict

from Customer import Customer


class CustomerNotAllowedException(Exception):
    info = ""
    msg = ""

    def __init__(self, info, msg):
        self.info = info
        self.msg = msg


def create_obj(line):
    customer = Customer()
    for x in range(0, len(line)):
        if x == 0:
            customer.setLname(line[0].strip())
        elif x == 1:
            f_name = line[1].strip()
            if '.' in f_name:
                title = f_name.split('. ')
                customer.setTitle(title[0])
                customer.setFname(title[1])
            else:
                #   create customer not allowed object
                raise CustomerNotAllowedException(line, ': customer not allowed')
    return customer


def read_file():
    file_path = 'FairDealCustomerData.csv'
    file_reader = open(file_path)
    cust_list = []
    try:
        for line in file_reader.readlines():
            sline = line.replace('\n', '').split(',', maxsplit=3)
            s_line = create_obj(sline)
            cust_list.append(s_line)
    finally:
        file_reader.close()
    return cust_list


def main():
    customers = read_file()
    print('Customers:')
    for c in range(len(customers)):
        print(customers[c].getTitle(), customers[c].getFname(), customers[c].getLname())
    print('\nNumber of Customers:', len(customers))


if __name__ == "__main__":
    main()
