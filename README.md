# Personal_Notebook
This App helps the user keep track of his studying progress, for each subject he attends (studying is organized in weeks of breaking down the course's material). 
The App :
-Build upon an SQLite3 database, it stores all your data locally. For each user, it created a new row on the "Users" Table, which is used for the log in/sign up function, and the studying progress data 
are stored in another table , which is named after the user's username.

Based on this way of storing data, each PC, can host more than 1 users.
Some functions that are included are : 
-if its the first time the app opens on a pc (meaning no data stored yet) you can only sign-up. Log in is no option at this phase.
-If its not the first time, you can either log-in, or create another account.
-Studying progress is based on weeks of dividing a yearful of the subject's material, so the maximum progress (a.k.a. week of completed studying) is 34 (about the number of weeks most UNI's operate at)
-Documentation is absent due to exams rn. Will be added shortly.
-Input check is a thing. You cant enter letters,symbols etc, just numbers.
-You can see your progress overall history, if there are no subjects, a suitable message appears.
-You can delete IF you dont want to appear anywhere. SQLITE doesnt allow actual deletion , so what happens is the value of the attribute is set to "DELETED",and this wont appear in history.
-You can add new subjects, with any name you choose. Recommended is max of 10 letters. Proper checking of this will be added soon.
Any recommendations you may have, feel free to message.



1) If you DONT want to build it, you just need to run "notebook_main.py" (make sure to include all files in the same directory)
2) To build it through Pyinstaller.
-You will need to use CMD, so make sure python is added to PATH.
first install pyinstaller using : pip install pyinstaller.

Then, use : cd directory_of_files_that_contains_the_py_files
Then the cmd command is this exact one pyinstaller --onefile --windowed --icon=notebook_icon.ico --add-data "center_window.py;." --add-data "data_correctness.py;." --add-data "forget_retrieve.py;." --add-data "login.py;." --add-data "sign_up.py;." --add-data "subject_history.py;." --add-data "subjects_update.py;." --add-data "update_existing_subjects.py;." --add-data "welcome_message.py;." notebook_main.py. Just copy paste it.

If the installation is complete, go to the original directory (where the .py files are saved), and you will see a filed named "dist". In this file, you will find the executable app. Due to the parameter --onefile, the executable is a bit slower to start. If you want that to change, you can replace it with --onefolder


