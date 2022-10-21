# Project 1: ILLUMINATION AND DELICATE...
def gettime():
    import datetime
    return datetime.datetime.now()


if __name__ == '__main__':

    c = int(input("Enter: \n 1.Bus Incoming \n 2.Bus Outgoing\n"))
    if c == 1:
        In = open("Bus Incoming.txt", "a")
        BusIncomingdata = input("Type the Bus Number!!\n").upper()
        # I.write(str([str(gettime())]) + ": " + BusIncomingdata + "\n")
        In.write(str("ENTERED:" + BusIncomingdata +
                 ": " + str([str(gettime())])) + "\n")
        In.close()
        # Case 1:Example of KA32EF1884..
        if BusIncomingdata == "KA32EF1884":
            In1 = open("KA32EF1884.txt", "a")
            In1.write(str("ENTERED:" + BusIncomingdata +
                      ": " + str([str(gettime())])) + "\n")
            In1.close()

            # Case 2:Example of KA12ER5858..
        if BusIncomingdata == "KA12ER5858":
            In1 = open("KA12ER5858.txt", "a")
            In1.write(str("ENTERED:" + BusIncomingdata +
                      ": " + str([str(gettime())])) + "\n")
            In1.close()
    # More cases can be inserted with our choice or as per the number of buses

    elif c == 2:
        Out = open("Bus Outgoing.txt", "a")
        BusOutgoingdata = (input("Type the Bus Number!!\n")).upper()
        Out.write(str("EXITED:" + BusOutgoingdata +
                  ": " + str([str(gettime())])) + "\n")
        Out.close()
        # Case 1:Example of KA32EF1884..
        if BusOutgoingdata == "KA32EF1884":
            Out1 = open("KA32EF1884.txt", "a")
            Out1.write(str("EXITED:" + BusOutgoingdata +
                       ": " + str([str(gettime())])) + "\n")
            Out1.close()

        # Case 2:Example of KA12ER5858..
        if BusOutgoingdata == "KA12ER5858":
            Out1 = open("KA12ER5858.txt", "a")
            Out1.write(str("EXITED:" + BusOutgoingdata +
                       ": " + str([str(gettime())])) + "\n")
            Out1.close()
    # More cases can be inserted with our choice or as per the number of buses
    else:
        print("Invalid Choice!!Please try again...")
        print("And Enter the bus number correctly\n")
