Name : Rujuta Vivek Vaidya
Email : rvaidya2@binghamton.edu
Language : Python (python3)
Tested on remote.cs.binghamton.edu - YES

How to compile and execute the program:
1. Run the genpasswd.py file if you want to create a userid and password.
Command : python3 genpasswd.py

You will be prompted to enter your id and password.
Validation will be performed.

Note: I have added an id-password in the hashpasswd file if you would like to use that.
Userid: rujuta
Password: helloworld@123

2. Run the server as:
Command: python3 serv.py < port number>

3. Run the client on another terminal as:
Command: python3 cli.py < domain-name (remote(01-07).cs.binghamton.edu)> < port number>
You will be prompted to enter id and password and they will be validated.


4. Other files:
- certificate.py : used to generate the certificates using python
- cert.pem and key.pem : certificates
- hashpasswd : store userid, password and date/timestamp


Please feel free to reach out to me in case of any queries regarding my code.
