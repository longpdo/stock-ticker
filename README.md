<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/example.gif

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <!-- <a href="https://github.com/longpdo/stock-ticker">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">Stock-Ticker</h3>

  <p align="center">
    Real-time stock indices and tickers in your terminal
    <br />
    <a href="https://github.com/longpdo/stock-ticker/issues">Report Bug</a>
    ·
    <a href="https://github.com/longpdo/stock-ticker/issues">Request Feature</a>
    <br />
    <br />
    <a href="https://github.com/longpdo/stock-ticker/issues"><img src="https://badgen.net/github/open-issues/longpdo/stock-ticker" /></a>
    <a href="LICENSE"><img src="https://badgen.net/github/license/longpdo/stock-ticker" /></a>
  </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents
* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Contributing](#contributing)
* [License](#license)
* [Acknowledgements](#acknowledgements)

<!-- ABOUT THE PROJECT -->
## About The Project
[![Product Screenshot][product-screenshot]](https://github.com/longpdo/stock-ticker)

`stock-ticker.py` is a python script using the Yahoo Finance API v7 as a data source. Major stock indices and currencies are printed out by standard and is then followed by the stock symbols provided by the user. The script will run every 5 minutes.

### Built With
* [Python 3.7.6](https://www.python.org/downloads/)

<!-- GETTING STARTED -->
## Getting Started
To get a local copy up and running follow these simple steps.

### Prerequisites
* Python 3
```sh
# Install via brew on macOS
brew install python
```
For Linux and Windows refer to [this](https://realpython.com/installing-python/).

### Installation
1. Clone the repository
```sh
git clone https://github.com/longpdo/stock-ticker.git
```
2. Change directory into stock-ticker
```sh
cd stock-ticker
```
3. Install python requirements
```sh
pip3 install -r requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage
* Single stock symbol
```sh
python3 stock-ticker.py AAPL
```

* Multiple stock symbols
```sh
python3 stock-ticker.py FB AAPL AMZN NFLX GOOG
```

* Text file with multiple stock symbols
```sh
python3 stock-ticker.py watchlist.txt
```

* watchlist.txt: add your stock symbols line per line
```
FB
AAPL
AMZN
NFLX
GOOG
```

* To stop the script, use `ctrl-c` inside your terminal.

<!-- CONTRIBUTING -->
## Contributing
Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->
## License
Distributed under the MIT License. See `LICENSE` for more information.

<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* Yahoo Finance API v7
* [pandas](https://pandas.pydata.org/)
* [colorama](https://pypi.org/project/colorama/)
