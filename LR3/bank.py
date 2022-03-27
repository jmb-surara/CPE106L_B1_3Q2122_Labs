"""
Author: Julian Marc B. Surara
Filename: bank.py
Program Description: The application generates a string of account names in order. 
"""

import pickle
import random
from savingsaccount import SavingsAccount


class Bank:
    """A bank is represented by this class as a collection
    of savings accounts. A file name is also connected
    with the bank, allowing accounts to be transferred to
    and from permanent file storage."""

    """A dictionary of accounts and a file name make up the
    state of the bank. A file name for the bank has not yet
    been established if the file name is None."""

    def __init__(self, fileName=None):
        """To hold the accounts, a new dictionary is created.
        If a file name is specified, the accounts are loaded
        from a pickled account file."""
        self.accounts = {}
        self.fileName = fileName
        if fileName != None:
            fileObj = open(fileName, 'rb')
            while True:
                try:
                    account = pickle.load(fileObj)
                    self.add(account)
                except Exception:
                    fileObj.close()
                    break

    def __str__(self):
        """Returns the string representation of the bank."""

        # using the sorted method sorting the dictionary
        # by values's name
        return "\n".join([str(v) for (k, v) in
                          sorted(self.accounts.items(),
                                 key=lambda cv: cv[1].getName())])

    def makeKey(self, name, pin):
        """Returns a key for the account."""
        return name + "/" + pin

    def add(self, account):
        """Adds the account to the bank."""
        key = self.makeKey(account.getName(), account.getPin())
        self.accounts[key] = account

    def remove(self, name, pin):
        """Removes the account from the bank and
        and returns it, or None if the account does
        not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.pop(key, None)

    def get(self, name, pin):
        """Returns the account from the bank,
        or returns None if the account does
        not exist."""
        key = self.makeKey(name, pin)
        return self.accounts.get(key, None)

    def computeInterest(self):
        """Computes and returns the interest on
        all accounts."""
        total = 0
        for account in self.accounts.values():
            total += account.computeInterest()
        return total

    def getKeys(self):
        """Returns a sorted list of keys."""
        # Exercise
        return []

    def save(self, fileName=None):
        """Saves pickled accounts to a file. The parameter
        allows the user to change file names."""
        if fileName != None:
            self.fileName = fileName
        elif self.fileName == None:
            return
        fileObj = open(self.fileName, 'wb')
        for account in self.accounts.values():
            pickle.dump(account, fileObj)
        fileObj.close()

# Functions for testing


def createBank(numAccounts=1):
    """Returns a new bank with the given number of
    accounts."""
    names = ("Julian", "Marc", "Charles", "Ivan", "Matthew",
             "Rebekah", "John", "Cedrick")
    bank = Bank()
    upperPin = numAccounts + 1000
    for pinNumber in range(1000, upperPin):
        name = random.choice(names)
        balance = float(random.randint(100, 1000))
        bank.add(SavingsAccount(name, str(pinNumber), balance))
    return bank


def testAccount():
    """Test function for savings account."""
    account = SavingsAccount("Rebekah", "1000", 500.00)
    print(account)
    print(account.deposit(100))
    print("Expect 600:", account.getBalance())
    print(account.deposit(-50))
    print("Expect 600:", account.getBalance())
    print(account.withdraw(100))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(-50))
    print("Expect 500:", account.getBalance())
    print(account.withdraw(100000))
    print("Expect 500:", account.getBalance())


def main(number=5, fileName=None):
    """Creates and prints a bank, either from
    the optional file name argument or from the optional
    number."""
    testAccount()

    print("\n----------Account Details------------\n")
    if fileName:
        bank = Bank(fileName)
    else:
        bank = createBank(number)
        print(bank)


if __name__ == "__main__":
    main()
