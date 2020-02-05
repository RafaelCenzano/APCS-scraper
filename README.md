# APCS scraper

Python app to scrape and remove links that return 404

#### Requirements

[Use a virtualenv to create an isolated enviorment](https://virtualenv.pypa.io/en/latest/)

Run the make command to install requirements

```
make
```

or with pip manually

```
pip3 install -r requirements.txt
```

## Running the program

Will run and display all 404 on README urls

```
python3 run.py test.md
```

You can add `hide` or `delete` as another argument to commment out or delete 404 urls

#### What happens when something goes wrong

Report the failed test [here](https://github.com/RafaelCenzano/APCS-scraper/issues)!

## Authors

* [**Rafael Cenzano**](https://rafaelcenzano.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
This Readme was created with pystarter

```
pip3 install pystarter
```