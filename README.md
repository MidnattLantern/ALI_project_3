![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

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

Wireframes
======
- lucidchart

Technology
======
- Development for all parts was done through a computer running macOS.
- All code was written in MS Visual Studio.
- Debugging was done trough MS Visual Studio.


Testing
======
- pep8 validator
- The code was checked for validation trough the pep8 validator
- As of version 22 october, there are no errors

Unsolved bugs:
------
- The mathmatical programs will be run twice.

Solved bugs:
------
- The mathmatical programs can be run more than once for each runtime.
- The input library will be reset rather than appended for each run.

Deployment:
======
- The code was deployed on Heroku and stored on Github.
- Live link: https://my-math-pilot-6200b0c88074.herokuapp.com