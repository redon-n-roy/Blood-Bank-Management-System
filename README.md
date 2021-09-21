# Blood Bank Management System

## Project Description

The main of the project was to design a Command Line Interface (CLI) for the blood bank where the users as wellas admin can perform various operations. The Wjole project is developed with the help of Python and MongoDB. There is also an added security of One Time Password (OTP) through the registered number. The program performs CRUD operations on the MongoDB from Python with the help of pymongo package. Also the program keeps running until the user wants to exit.

## Technologies Used

* Python 3.9.2
* MongoDB Server 5.0.0
* pymongo 3.12.0
* twilio 6.62.0

## Features

List of features ready and TODOs for future development

* Add donor
* Search donor
* List donors
* Update donor
* Delete donor

To-do

* Add email and enable 2FA based on email.

## Getting Started

>All the operations below are for Windows OS

* Make sure to install all the dependencies as listed above.
* Clone this repository to your local system.
```
git clone https://github.com/redon-n-roy/Blood-Bank-Management-System
```

## Usage

The following are the steps to get the program running:-

> You will need to add the Twilio credentials for the OTP features to work.

* Start the MongoDB daemon from the CMD using the `mongod` command.
* Move to the directory with the files in this repo.
* Run `python main.py` on the CMD in that folder.

## License

This project uses the [MIT](./LICENSC) license.
