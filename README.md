# CIDM-Final Project
Unable to Deploy... Sad Day.

## Reflections

### 
The journey through developing the CIS Degree Program Management System has been a blend of challenges, learning, and iterative improvements but unfortunatley I came up short with the final project as I was unable to deploy it.

All in all this project was a great experiance, but I must say in my humbling opinion I had a hard time following the book and I took matters into my own hands and did my own research and implented some of the things required for the project that were expressed different in the book, I hope my effort is acknowledged in the final grade. 

Thank you Dr. Babb for an incredible course in which I will take these new skills that I have learned into the real word. Web/Application Developement is something that I am passionate about and this class has proved to me that there so much more to learn in this revolutionary field.

Below will be a brief outline of the steps I took in exact order to deploy and where I found myself in a hole that I could not dig myself out of.


### STEPS 
- Created an account on Digital Ocean and created a 'Droplet'

- Generated an SSH Key via Command Prompt Terminal and connected via SSH using command 'ssh root@146.190.124.97' - My IP that Digital Ocean gave me

- Continued through prompt which inlcuded incorperating my private SSH key and completed the set up.

- Updated and Upgraded the need packages using command lines 'sudo apt update' & 'sudo apt upgrade'. I also Installed Python and the necessary tools needed to deploy the virtual enviroment.

- Created a new user account for you using the commands 'sudo adduser babb' for the username and 'cidm6325' for the password. I also assigned you to Room Number 70 to add some information to your profile.

- Cloned my git repository into the terminal 

- Installed the virtual enviroment using commands 'apt install python3-virtualenv'
  
- After this I was able to connect to my virtual enviroment as if I was connected in it through VS Code by changing directories and running the command 'source venv/Scripts/activate'

- I ran the command "ls" to make sure I was seeing all my files associated with the project, in which I was able to.

- The next step I did was try to install the requirements.txt to move forward but I noticed that this file was missing, so I generated it and restarted my virtual enviroment.

- Unfortunatley I was unable to install it even after making the changes. I tried to skip this step and run other commands like 'makemigrations' but It was unsucessfull. After watching numerous Youtube Videos I was unable to figure out why this was happening and this is where I stopped.

## Conclusion
I will provide images of outputs of my project to show what was implemented as I was unable to deploy. With the information stated in the steps maybe you are able to deploy this and if you do please let me know. I would like to know where i went wrong.

All though I could have reached out for help on this, over the past few weeks, unexpected and challenging circumstances have arisen in my personal life that required my immediate attention and care. These circumstances required a significant amount of my time, making it difficult for me to allocate the necessary focus and effort to the project... I hope you understand.

Once Again, thank you for being apart of my MBA journey at WTAMU and I will be thinking about you and all the professors that have helped me along the way as I walk that stage next week... Go Buffs!

**PS Screenshots will be located in the "screenshots" folder.

## Django Admin Login Information 

###
Username: admin
Password: cidm6325
