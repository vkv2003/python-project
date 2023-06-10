# python-project


A PROJECT REPORT
ON
CHITTI: The Personal window Assistant
Submitted in the partial fulfillment of award of the 
Requirement for the award of the degree of
BACHELOR OF SCIENCE (INFORMATION TECHNOLOGY
By
Vipin Kumar Vishwakarma
Under the esteemed guidance of
Mrs Smita dalvi
Mrs Vaishali Kadam
Mrs Snehal Patil
 
DEPARTMENT OF INFORMATION TECHNOLOGY
SHANKAR NARAYAN COLLEGE
Affiliated to University of Mumbai
CITY : MUMBAI , PIN CODE : 401105
MAHARASTRA YEAR : 2022-23

PROFORMA FOR THE APPOROVAL PROJECT PROPOSAL

        PNR No .:                                                                                                              ROLL No.:
1.	Name of the student :- Vipin Kumar Vishwakarma
       2.Tittle of the Project :- CHITTI: The Personal Window Assistant








 ABSTRACT
As we know Python is an emerging language so it becomes easy to write a script for Voice Assistant in Python. The instructions for the assistant can be handled as per the requirement of user. Speech recognition is the process of converting speech into text. This is commonly used   in   voice   assistants   like   Alexa, Siri, etc.   In   Python   there   is   an   API   called Speech Recognition which allows us to convert speech into text. It was an interesting task to   make my own assistant.   It   became   easier   to search query without   typing   any word, searching on Google without opening the browser, and performing many other daily tasks like playing music, opening your favorite IDE with the help of a single voice command. In the current scenario, advancement in technologies are such that they can perform any task with same effectiveness or can say more effectively than us.  By   making   this project, I realized that the concept of AI in every field is decreasing human effort and saving time.
 Functionalities of this project include:
1. It can open command prompt, your favorite IDE, notepad etc.
2. It can play music.
3. It can do Wikipedia searches for you.
4. It can open websites like Google, YouTube, etc., in a web browser.
5. It can give weather forecast.
6. It can have some basic conversation.
7.It can control volume of system.
8.It can search your query on YouTube.

Now the basic question arises in mind that how it is an AI? The virtual assistant that I have created is like if it is not an A.I, but it is the output of a bundle of the statement. 



ACKNOWLEDGEMENT
We had a great experience working on this project and we got to learn a plethora of new skills through this project. We are highly indebted to the teachers and especially Mr Manoranjan Panda for their guidance and constant supervision as well as providing necessary information regarding the project and also for their support in completing the project
Place:  Bhayander
Date:                                                                                                                  Vipin Kumar Vishwakarma



















DECLARATION
	We do hereby declare that the report entitled “Chitti-The personal-Assistant” submitted by me to College of Information and Technology, Bhayandar in partial of the requirement for the award of the degree . To the best  of my knowledge  other than me , no one has submitted to any other university.
	 The project is done in partial fulfillment of the requirement for the award of degree of  BACHELOR OF SCIENCE(INFORMATION TECHNOLOGY) to be submitted as 5th semester project as part of my curriculum.

Vipin Kumar Vishwakarma



                                                                                                                                               












Content
Chapter 1 :Introduction                                                                                                
1.1	Background
1.2	Objective…..
1.3	Purpose and Scope…..
1.2.1 Purpose ….
1.2.2Scope
Chapter 2:System Analysis
1.1	Existing System
1.2	Proposed System
1.3	Requirement analysis
1.4	Hardware Requirements
1.5	Software Requirements
1.6	Justification  of selection of technology
Chapter 3: System Design
3.1 Module Division
3.2 Data Dictionary
3.3 ER Diagram
DFD/UML Diagram
Chapter 4:Implement and Testing 
4.1 Code (Place core segment)
4.2 Testing approach
        4.2.1 Unit Testing (Test cases and Test results)
         4.2.2  Intregration System (Test cases and Test results)
Chapter 5: Result and Discussion (Output screens)
Chapter 6: Conclusion and Future work
Chapter 7 : Reference          
LIST OF TABLE

CHAPTER 1: Introduction	9
1BACKGROUND:.	11
1.2OBJECTIVE:	12
1.3PURPOSE AND SCOPE	12
PURPOSE:	12
SCOPE:	12
2.SYSTEM ANALYSIS	13
2.1 EXISTING SYSTEM:	13
2.2 PROPOSED SYSTEM:	13
2.3 REQUIREMENT ANALYSIS	14
    functional  and non functional requirement…………………………………………………………………………………......14
SYSTEM ANALYSIS:-	14
Microsoft Visual studio :-	14
2.4 HARDWARE REQUIREMENT:	15
2.5 SOFTWARE REQUIREMENT:	15
2.6Justification of plateform:-	15
CHAPTER 3: System Design	16
3.1 Module Division:-	16
3.2DATA DICTIONARY:-	16
3.3 E-R DIAGRAM:-	17
3.4 DATA FLOW DIAGRAM:-	18
Class Diagram:	19
Activity Diagram:	20
Sequence Diagram:	20
Working:	22
Gantt Chart:	23



LIST OF FIGURE
Figure 1 ER DIAGRAM	17
Figure 2 DATA FLOW	18
Figure 3 DATA FLOW	19
Figure 4 ACTIVITY DIAGRAM	20
Figure 5 SEQUENCE DIAGRAM	20
Figure 6 WORKING	22
Figure 7 GANTT CHART	23
















CHAPTER 1: Introduction

	Artificial Intelligence when used with machines, it  shows   us   the capability of thinking like humans. In this, a computer system is designed in such a way that typically requires interaction from human. As we know Python is an emerging language so it becomes easy to write a script for Voice Assistant in Python. The instructions for the assistant can be handled as per the requirement of user. Speech recognition is the Alexa, Siri,  etc.   In   Python   there   is   an  API  called  Speech   Recognition   which  allows  us   to convert speech into text. It was an interesting task to make my own assistant. It become easier to search our query without typing any word, Searching on Google without opening the browser, and performing many other daily t	asks like playing music, opening your favorite   IDE   with   the   help   of   a   single   voice   command.   In   the   current   scenario, advancement   in   technologies   are   such   that   they   can   perform   any   task   with   same effectiveness or can say more effectively than us. By making this project, I realized that the concept of AI in every field is decreasing human effort and saving time.

1.1BACKGROUND:

	As the voice assistant is using Artificial Intelligence hence the result that it is providing  are highly accurate  and efficient. The assistant can help to reduce human effort  and   consumes less  time  while   performing   any   task,   they  removed   the  concept  of typing completely and behave as another individual to whom we are talking and asking to perform task. The assistant is no less than a human assistant but we can say that this is more effective and efficient to perform any task. The libraries and packages used to make this assistant focuses on the time complexities and reduces time.
	The functionalities include , It can control volume, It can open your favorite IDE etc., It can playmusic, It can do Wikipedia searches for you, It can open websites like Google, YouTube, etc., Also it can search your query on youtube in a web browser, It can give weather forecast. It can have some basic conversation
	Tools and technologies used  are Microsoft visual studio IDE for making  this  project. Along with this I used following modules and librariesin my project. pyttsx3, SpeechRecognition, Datetime, Wikipedia, pywhatkit, pyautogui, etc.


1.2OBJECTIVE:	
	The following are the detail objective of the system
•	To manage the taks of desktop .
•	To reduce user effort.
•	To perfom some task in desktop.

1.3PURPOSE AND SCOPE
PURPOSE:
	Chitti virtual assistant is designed to work efficiently on desktop. Virtual assistant improves productivity of user by managing daily routine tasks of the user and provides general information from Internet\online sources to the user. Virtual assistant is now days turning to be smarter & more intelligent than ever.
SCOPE:
	The main aim to provide friendly user interface to every user of desktop.The various other functionality about this project you can search various query . This will help all user of desktop.In this user can perform a task by giving instruction .



	

	



2.SYSTEM ANALYSIS
2.1 EXISTING SYSTEM:
	We are familiar with many existing voice assistants like Alexa, Siri, Google Assistant, Cortana which uses concept of language processing, and voice recognition. They listens the command given by the user as per their requirements and performs that Specific function in a very efficient and effective manner.
	As these voice assistants are using Artificial Intelligence hence the result that they are providing are highly accurate and efficient. These assistants can help to reduce human effort and consumes time while performing any task, they removed the concept of typing completely and behave as another individual to whom we are talking and asking to perform task. These assistants are no less than a human assistant but we can say that they are more effective and efficient to perform any task. The algorithm used to make these assistant focuses on the time complexities and reduces time. But for using these assistants one should have an account (like Google account for Google assistant, Microsoft account for Cortana) and can use it with internet connection only because these assistants are going to work with internet connectivity. 
2.2 PROPOSED SYSTEM:
It is different from other traditional voice assistants in terms that it is specific to desktop and user does not need to make account to use this, it does not require any internet connection while getting the instructions to perform any specific task.
	The IDE used in this project is Microsoft visual studio. All the python files were created in Microsoft visual studio and all the necessary packages were easily installable in this IDE. For this project following modules and libraries were used i.e. pyttsx3,  SpeechRecognition, Datetime, Wikipedia, pywhatkit, pyautogui etc.
	With the advancement Chitti can perform any task with same effectiveness or can say more effectively than us. By making this project, I realized that the concept of AI in every field is decreasing human effort and saving time. Functionalities of this project include, , It can open visual studio, your favorite IDE, notepad etc., It can play music, It can do Wikipedia searches for you, It can open websites like Google, YouTube, etc., in a web  browser,  It   can   give   weather   forecast.

2.3 REQUIREMENT ANALYSIS
SYSTEM ANALYSIS:-
Introduction:-
	 The IDE used in this project is Microsoft visual studio. All the python files were created in Microsoft visual studio and all the necessary packages were easily installable in this IDE. For this project following modules and libraries were used i.e. pyttsx3, SpeechRecognition, Datetime, Wikipedia,  pywhatkit, pyautogui, etc


Microsoft Visual studio :-
	It increase developer agility and productivity. Streamline every stage of development with tools and resources to support developers as they build the next generation of apps.
Collaborate anytime, anywhere. ...
Innovate on the platform of your choice.

	FUNCTIONAL AND NON FUNCTIONAL REQUIREMENT:

FUNCTIONAL REQUIREMENT:
•	The user should be able to give the command for process it properly.
•	The system shall provide appropriate result according to user search as.
•	Every order should be in English language.
NON FUNCTIONAL REQUIREMENT:
•	Having a good working performance.
•	We can keep it in our pc having a less storage.
•	It is easy to use .


2.4 HARDWARE REQUIREMENT:
Computer Equipment:
1. Processor : Intel CORE i5 processor with minimum 2.9 GHz speed. 
2. RAM : Minimum 4 GB.
 3. Hard Disk : Minimum 500 GB.

2.5 SOFTWARE REQUIREMENT:
1.Microsoft Word 2007 
2. Database Storage : Microsoft Excel 
3. Operating System : Windows10


2.6Justification of plateform:-
	The project aims to develop a personal-assistant for window systems. Chitti draws its inspiration from virtual assistants like Cortana for Windows, and Siri for iOS. It has been designed to provide a user-friendly interface for carrying out a variety of tasks by employing certain well-defined commands.



CHAPTER 3: System Design
3.1 Module Division:-
	 In CHITTI following python libraries(module) were used:
	Pyttsx3: It is a python library which converts text to speech. 

	SpeechRecognition: It is a python module which converts speech to text.

	 Wikipedia: It is a python module for searching anything on Wikipedia. 


	PyPDF2: It is a python module which can read, split, merge any PDF.

	Pyjokes: It is a python libararies which contains lots of interesting jokes in it.

	  Web Browser: It provides interface for displaying webbased documents to users.
 
	OS: It represents Operating System related functionality.

	Pywhatkit: PyWhatKit is a Python library with various helpful features. It's easy-to-use and does not require you to do any additional setup....



3.2DATA DICTIONARY:-
	Idely it use mic to take command from user. And that’s converts into text after that it performs on that.It match the command given by user to the written data in condition if the command match with the condition that work in that. 



3.3 E-R DIAGRAM:-
	An entity relationship diagram (ERD), also known as an entity relationship model, is a graphical representation that depicts relationships among people, objects, places, concepts or events within an information technology (IT) system


 
Figure 1 ER DIAGRAM




3.4 DATA FLOW DIAGRAM:-
	A flowchart is a diagram that shows how a workflow or process works. A flowchart is a diagrammatic depiction of an algorithm, or a step-by-step procedure for completing a job. 
The flowchart depicts the stages as various types of boxes, with arrows linking the boxes in a logical order. A solution model for a particular problem is depicted in this diagrammatic representation. 
Flowcharts are used in a variety of industries to analyze, create, record, and manage a process or program. The flow chart depicts the whole operation of the Chitti Chitti.
 
Figure 2 DATA FLOW


Class Diagram:
	A class diagram is an illustration of the relationships and source code dependencies among classes in the Unified Modeling Language (UML). In this context, a class defines the methods and variables in an object, which is a specific entity in a program or the unit of code representing am of 
 that entity.

 
Figure 3 DATA FLOW

Activity Diagram:
	An activity diagram visually presents a series of actions or flow of control in a system similar to a flowchart or a data flow diagram. Activity diagrams are often used in business process modeling. They can also describe the steps in a use case diagram. Activities modeled can be sequential and concurrent. 
 
Figure 4 ACTIVITY DIAGRAM
	
	Sequence diagrams, commonly used by developers, model the interactions between objects in a single use case. They illustrate how the different parts of a system interact with each other to carry out a function, and the order in which the interactions occur when a particular use case is executed.

 
Figure 5 SEQUENCE DIAGRAM

 
 

 
Figure 6 WORKING
Gantt Chart:
	A Gantt chart is used for project planning: it's a useful way of showing what work is scheduled to be done on specific days. It helps project managers and team members view the start dates, end dates and milestones of a project schedule in one simple stacked bar chart.

 
Figure 7 GANTT CHART


	The system is designed using the concept of Artificial Intelligence and with the   help   of   necessary   packages  of  Python.
   Python  provides   many  libraries  and packages to perform the tasks, for example pywhatkit can be used to search query on Youtube.
 The details of these packages are mentioned in Chapter 3 of this report.
The data in this project is nothing but user input, whatever the user says, the assistant performs the task accordingly. 
The user input is nothing specific but the list of tasks which a user wants to get performed in human language i.e. English
















