# Silent Auction Program

Welcome to the Silent Auction Program! This is a simple Python script to manage a silent auction where multiple bidders can place their bids, and the highest bidder wins.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [How to Use](#how-to-use)
- [Features](#features)
- [Contributing](#contributing)

## Introduction

The Silent Auction Program allows users to conduct a secret auction where participants can place their bids without others knowing. The program collects bids and determines the highest bidder at the end of the auction.

## Installation

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/sujaljoshi7/Silent-Auction.git
    cd silent-auction
    ```

2. **Ensure you have Python installed:**

    This script requires Python 3. You can download it from [python.org](https://www.python.org/).

3. **Ensure you have the `art` file in the same directory:**

    Make sure the `art.py` file containing the logo is in the same directory as the main script.

## How to Use

1. **Run the Program:**

    To start the program, simply run the Python script:

    ```bash
    python silent_auction.py
    ```

2. **Input the Required Information:**

    - The program will display a welcome message and prompt users to enter their name and bid amount.
    - Users will be asked if there are any other bidders. If yes, the next bidder can place their bid.
    - If no, the program will determine the highest bidder and announce the winner.

3. **Example:**

    ```bash
    Welcome to the secret auction program
    What is your name? Alice
    What is your bid amount? ₹500
    Are there any other bidders? Type 'yes' or 'no': yes
    What is your name? Bob
    What is your bid amount? ₹600
    Are there any other bidders? Type 'yes' or 'no': no
    The winner is Bob with a bid of ₹600.
    ```

## Features

- Allows multiple users to place their bids secretly.
- Determines and announces the highest bidder.
- Simple and easy-to-use text-based interface.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository.
2. Create your feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -am 'Add some feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Create a new Pull Request.

---

**Note:** Ensure you have the `art.py` file in the same directory as the main script to display the logo. This script does not use any other external modules beyond the Python standard library.
