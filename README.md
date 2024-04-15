# TeamGreen project
An API for customers and staff to use and manage an online garden centre shop.

## About the project

This API can be used by customers to search and order products from the garden centre’s online shop and add product reviews. 
Garden centre staff can use the API to add and update stock, and to access and add customer information.

The API allows the following transactions:
- Customers can view all products available.
- Customers can search products by category.
- Customers can add products to a shopping basket.
- Customers can add reviews to products.
- Staff can add new products to the stocklist.
- Staff can add customers to the database.
- Staff can search for customers by email address.

### Software used
- We used Python to develop the app’s endpoints, connect to a database and design client interfaces for customers and staff.
- We used Flask web framework as our server.
- We used a range of Python libraries: Flask, requests, jsonify, my-sql-connector. 
- We built our database and tables in MySQL. 
- We used Git and Github for version control to collaborate as a team of 4 developers.

### Future updates
For future releases, we will add the following new features:
- Customers can view items in shopping basket and total cost.
- Customers can delete their account details.
- Customers can search by review rating.
- Customers can search for specific products. 
- Staff can delete discontinued products from stocklist.
- Staff can remove customer details for GDPR purposes. 
- Options for users to undo / edit actions.

## How to install and run the project
1.	Clone the TeamGreen repository to your local machine using the url [https://github.com/mcstastney/TeamGreen.git ](https://github.com/mcstastney/TeamGreen.git)
2.	Open the project files in Pycharm or Visual Studio Code
3.	From your Pycharm or Visual Studio Code terminal, install the project requirements by running: **pip install -r requirements.txt**
4.	Open **config.py** and add your SQL login details.
5.	Run the files in the following order:
- db_utils.py
- app.py
- main_customer.py or main_staff.py
6.	When main_customer.py or main_staff.py is running, navigate through the menu via the console.

## How to use the project
There are two main.py files: **Main_customer.py** and **Main_staff.py**.  Users can directly interact with the API by running the functions within the main.py files. 

Main_customer.py has been designed to be accessed directly by customers to use for retail shopping purposes. 

Main_staff.py has been designed to be accessed directly by staff to use for business administration purposes. 

### Functionality of Main_Staff.py and how to use it
When first running the Main_Staff.py file the terminal will display a menu of numbered options prompting the user to interact by making a choice and inputting a number

image 1

### Search all customer records
By selecting option 1 the user can view all customer records:

image 2

The records displayed are taken directly from the Garden Centre mySQL database ‘online_shop’  (the main python files work in conjunction with the db_utils file and config file to connect to and access the database directly).  

The customer details when retrieved in the terminal are displayed in a table format.  There are functions to determine how information from the database is presented.  

Staff members can easily and clearly view all customer records for any purpose such as marketing, future contact or promotional selling.  

### Search for customer by email address
Staff can search for an individual customer using their email address by selecting option 2 from the menu:

image 3

The entire customer record is displayed once the customer is located.

### Add customer records to the database
The API interface using the terminal is a quick and easy way for staff to be able to update customer records.  Option 3 on the menu allows the user to add customer records to the database ‘online_shop’.

By selecting option 3 the user will then be asked for several inputs needed to populate the customer record completely. The user inputs match the column headers of the table ‘customers’ within the database ‘online _shop’. The customer_ID column uses auto-increment in the SQL database so the user doesn’t have to input this. 

Once the final input is made, confirmation is made clear to the user through a statement displayed:

image 4

To check that the customers details have been added to the database, option 1 can be selected again to view the all customer records to check the addition has been made – this is not necessary but can be reassuring for the staff member to check.

image 5

(Added record is highlighted with yellow line)

### Adding product records to the database
The API interface using the terminal is a quick way for staff to update product records; this is important for managing stock levels. Option 4 allows the user to add product records to the database ‘online_shop’.

By selecting option 4, the user will then be asked for several inputs needed to populate the product record completely.  The user inputs match the column headers of the table ‘products’ within the database ‘online _shop’.  The product_ID column uses auto-increment in the SQL database so the user doesn’t have to input this.

Once the final input is made, confirmation is made clear to the user through a statement displayed:

image 6

### Quit the Main_Staff program at anytime	
Finally, the menu option zero allows the user to quit the program:

image 7

### Functionality of Main_Customer.py and how to use it
To be added

### Summary of structure and design principles
To be added

## Credits
### TeamGreen members
This team project is a collaboration between four developers:

**[Elisa McGarry](https://github.com/mcstastney)**
My ethos is: 'how can I design this to make life easier for people?' It's what initially inspired me to start learning web development; to improve the platforms I used for employee communications. 
It has sparked such joy in me, I've switched careers from Communications to coding.

Previous CFG degree projects:
- [Houseplant Picker](https://github.com/mcstastney/HouseplantPicker) – HTML, CSS and Javascript app to help users choose the perfect houseplant for each room in their home.
- [Gardener's Forecast API](https://github.com/mcstastney/GardenersForecastAPI) – Python console app to give seasonal gardening tips based on the user's personal goals and real-time local weather forecast.
- [Wildlife Counter](https://github.com/mcstastney/WildlifeCounter) – SQL database designed for a wildlife charity so volunteers can record local wildlife sightings.

In this TeamGreen assignment we’ve used GitHub and Git for version control and collaboration. 

**[Emma Jourzac](https://github.com/jourzy)**
I am a career switcher on a full-stack developer journey.  My background is in education, teaching Computing (however like the majority of Computing teachers in the UK I was not a subject specialist!).
So I did things a bit backwards - I taught a subject, and now I'm learning it! With over ten years encouraging young girls to consider a career in tech, I have made the jump myself.

Previous CFG degree projects:
- An app in JavaScript where users can find their perfect houseplant by filtering on criteria such as sunlight and room humidity.
- An app in Python where users can search for Yoga poses and add them to a Yoga practice, saved to a text file.
- A database for a therapist, assisting with diary management and bookings, recording session notes and client data, as well as keeping track of income and expenses.

In this assignment I will be using GitHub for version control, creating branches to work on adding functionality and creating pull requests so that my team can review and merge changes.

**[Katie Kennedy](https://github.com/KatieCodes365)**
I am a Marketing Executive developing my skills to become a software engineer. During my work as a project manager for a charity that helped disabled adults and children, I became interested in software development. 
When I led a project to make technology accessible for everyone, I became aware of the digital divide that exists. Seeing the challenges the people we supported faced and how tech could change their lives made me want to be part of tackling the divide by creating technology for everyone.

Previous CFG projects include:
- Travel Map project in JavaScript which produces a randomly recommended location for the user to travel to.
- Project in Python that uses a weather API to retrieve the latest weather conditions and then curate a music playlist for the user depending on the weather that day.
- Database for a gym, providing membership information and class and treatment data. Members can book a class or a treatment depending on their membership level. The gym can use the database to track income and retrieve members details.

In this assignment I aim to gain a better understanding of the standards and routines followed by professional software developers when using GitHub within a team.
Through hands-on experience and continuous learning, I seek to refine my abilities and contribute effectively to the field of technology.

**[Majella O'Mahony](https://github.com/MadgeMom)**

To be provided


## References
We are grateful to the following people / organisations for their tuition, resources and guidance. Without them, this project would not be possible.

- [Code First Girls](https://codefirstgirls.com/) and the whole CFG community
- Tech with Tim’s [Create A Python API in 12 Minutes video](https://www.youtube.com/watch?v=zsYIw6RXjfM)
- [PyNative](https://pynative.com/python/basics/) 

## License
[GNU General Public License v3.0](License)

## Evidence of Gti and Github skills

### Checking the status of a file

![Screenshot of a git status command showing a file that has been modified.](/assets/images/check_status.png?raw=true)

![Screenshot of a git status showing a file that has been modified](https://github.com/mcstastney/TeamGreen/assets/136608321/5a316040-e652-4a7b-b12e-c22c482b9187)


### Creating a branch

![Screenshot of a branch being created.](/assets/images/create_branch.png?raw=true)

![Screenshot of confirmation branch was created](https://github.com/mcstastney/TeamGreen/assets/136608321/94342215-2f4b-44fc-a425-0eda93016383)


### Adding files a branch

![Screenshot of a file being added to a branch.](/assets/images/add_file_branch1.png?raw=true)

NEED TO ADD AT LEAST ONE MORE HERE AS SAYS FILES PLURAL!!!!

### Adding commits with meaningful messages

![Screenshot of a commit with a meaningful message.](/assets/images/commit_message1.png?raw=true)

![Screenshot of a commit with a meaningful message](https://github.com/mcstastney/TeamGreen/assets/136608321/c2a0a087-a5b6-4392-9073-73eba853e273)

NEED TO ADD AT LEAST ONE MORE HERE AS SAYS COMMITS PLURAL!!!!

### Opening a pull request

![Screenshot of completion of PUSH request and signpost to Github to PULL request](https://github.com/mcstastney/TeamGreen/assets/136608321/3b43454c-2c73-4917-bce1-e002c760722c)

![Screenshot showing an open pull request.](/assets/images/pull_request3.png?raw=true)

### Merging and deploying to main branch

![Screenshot of a pull request being accepted and files deployed to main branch.](/assets/images/?????.png?raw=true)
