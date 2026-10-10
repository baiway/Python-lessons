#include <iostream>
#include <string>

class BankAccount {
public:
    // Public: anyone can use these
    std::string owner;

    BankAccount(std::string owner, double balance, int pin)
        : owner(owner), balance(balance), pin(pin) {}

    void deposit(double amount) {
        if (amount <= 0) {
            std::cout << "Deposits must be positive!\n";
            return;
        }
        balance += amount;
    }

    double get_balance() const {
        return balance;
    }

    bool check_pin(int attempt) const {
        return attempt == pin;
    }

protected:
    // Protected: only this class and its subclasses can use these
    double balance;

private:
    // Private: only this class can use these
    int pin;
};

class SavingsAccount : public BankAccount {
public:
    SavingsAccount(std::string owner, double balance, int pin, double interest_rate)
        : BankAccount(owner, balance, pin), interest_rate(interest_rate) {}

    void add_interest() {
        balance += balance * interest_rate;  // fine: `balance` is protected
        // pin = 0;                          // error: `pin` is private to BankAccount
    }

private:
    double interest_rate;
};

int main() {
    SavingsAccount account("Ada", 100.0, 1234, 0.05);
    account.deposit(50.0);
    account.add_interest();

    std::cout << account.owner << "'s balance is £" << account.get_balance() << "\n";
    std::cout << "Is the PIN 1234? " << std::boolalpha << account.check_pin(1234) << "\n";

    // account.balance = 1000000.0;  // error: `balance` is protected
    // std::cout << account.pin;     // error: `pin` is private

    return 0;
}
