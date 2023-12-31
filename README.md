![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

IMPORTANT!!
======
- My Math Pilot is incompatible with Safari,
- It is recomended that you use Chrome or Firefox.
![first%20thing%20you%20see.png](https://raw.githubusercontent.com/MidnattLantern/ALI_project_3/main/readme_photos/first%20thing%20you%20see.png)

User stories
======
- As a visitor, I expect to be able to automatically calculate a 2-point equation.
- As a visitor, I expect to be able to automatically calculate the derivative of a given input.
- As a visitor, I expect My Math Pilot to understand, make sense of, and clean up my messy input.
- As a visitor, I expect my input to be stored for later use so that calculations are fast and convenient.
- As a visitor, I expect My Math Pilot to slice my input into appropriate chunks for mathematical tasks.
- As a visitor, I expect to have a stockpile of information about every mathematical task that My Math Pilot can perform.

Features
======
- The user is provided with a menu containing six programs, each with a designated index number. To run a program, the user can either enter the program's index number or name. 
- Program 1 is a text file that provides guidance on how My Math Pilot handles and processes mathematical inputs from the user.
- Program 2 is where the user can enter or re-enter their equation. Upon pressing enter, the user can see how their input is being stored by My Math Pilot.
- Program 3 is a text file that teaches the user the basics of Derivate in mathematics.
- Program 4 prompts the user to input two values in order to calculate the derivative of their input. This program asks the user for input in the same line as Program 2.
- Program 5 is a text file that teaches the user the basics of finding the value K in a 2-point equation.
- Program 6 prompts the user to input four values in order to calculate the K-value of their input. This program asks the user for input in the same line as Program 2.
- Program 99 is hidden and is designed to stop the Python runtime. The user will not be able to do anything unless they refresh the deployment page.

Future features
======
- My Math Pilot currently has only two programs for mathematical tasks, but the possibilities of mathematics are endless. More programs could be added for a vast variety of mathematical tasks, such as expression reduction, for example, from (+3x − (x+5)) to (+2x - 5).
- At present, the programs can store polynomials with variables and exponents, but they only accept polynomials with positive or negative whole numbers. In the future, My Math Pilot could accept decimals, and variables and process them in a way appropriate for mathematics.
- Monomials with exponents are rejected currently, but in the future, they could be processed to a number, for example, +2^3 could return +8.
- Inputs to mathematical tasks need to be entered again each time. But in the future, they could load the storage that was updated by the input program (2).
- Outputs from mathematical tasks could be stored for other advanced mathematical tasks, such as outputs from derivatives to be used for integrals.

Flowchart
======
![flowchart%202.png](https://raw.githubusercontent.com/MidnattLantern/ALI_project_3/main/readme_photos/flowchart%202.png)
![flowchart%201.png](https://raw.githubusercontent.com/MidnattLantern/ALI_project_3/main/readme_photos/flowchart%201.png)

Technology
======
- The flowchart(s) was sketched on Affinity Designer 2
- Development for all parts was done through a computer running macOS.
- All code was written in MS Visual Studio.
- Debugging was done through MS Visual Studio.

Testing
======
- pep8 validator: https://pep8ci.herokuapp.com 
- The code was checked for validation through the pep8 validator
- As of version 24:th October, there are no errors
![derivate_coefficient.py.png](https://raw.githubusercontent.com/MidnattLantern/ALI_project_3/main/readme_photos/pep8%204%20derivate_coefficient.py.png)
![linear_2p_equation.py.png](https://raw.githubusercontent.com/MidnattLantern/ALI_project_3/main/readme_photos/pep8%204%20linear_2p_equation.py.png)
![polynomial_input.py.png](https://raw.githubusercontent.com/MidnattLantern/ALI_project_3/main/readme_photos/pep8%204%20polynomial_input.py.png)
![run.py.png](https://raw.githubusercontent.com/MidnattLantern/ALI_project_3/main/readme_photos/pep8%204%20run.py.png)
![input_recognition.py.png](https://raw.githubusercontent.com/MidnattLantern/ALI_project_3/main/readme_photos/pepp8%204%20input_recognitioninput_recognition.py.png)

Unsolved bugs:
------
- There are no discovered bugs for ver 1.0

Solved bugs:
------
- The mathematical programs (4 and 6) can be run more than once for each runtime.
- The input library will be reset rather than appended for each run.
- The mathematical programs (4 and 6) will no longer be run twice in a row.

Deployment:
======
- The code was deployed on Heroku and stored on GitHub.
- My Math Pilot is founded on a template provided by Code Institute: https://github.com/Code-Institute-Org/python-essentials-template
- in the provided link, click "use this template", then "create new repository", My Math Pilot was named ALI_project_3 for the repository name
- A local folder copy for My Math Pilot was stored on OneDrive
- In MS Visual Studio, the extension: "GitHub Pull Requests and Issues" was used to conviniently link the repository to the OneDrive folder.
- In MS Visual Studio, click Open Folder, then navigate to where you stored the local folder.
- If the extension is installed, click the branch icon, then "initialize repository" and type the name of the repository.
- to acces the console to make Git Pushes, press CMD + J on Mac.
- To deploy on Heroku, create an account, you can request the student offer to keep the app running for free if you link to your Github account: https://www.heroku.com/github-students/signup 
- You need to provide a credit card information for your Heroku account.
- On this link, click create app: https://dashboard.heroku.com/apps
- Give the app a name. This app was named my-math-pilot
- Click "settings", then "reveal config vars"
- Type "PORT" inside "key" and "8000" inside "value"
- Add two buildpacks: Python and Nodejs, in that order
- Click settings, then "connect to Github"
- type the name of the repository name inside "repo.name", in this instance, "ALI_project_3", then search, then select the repository
- Further down, click Deploy branch. There's an automatic option, but My Math Pilot was deployed manually
- The deployment will be built, and a live link will be provided if the build was successful.
- Live link: https://my-math-pilot-4e8514124918.herokuapp.com

Developed by Alma Isaksson ('AlI' or 'midnatt lantern') October 2023