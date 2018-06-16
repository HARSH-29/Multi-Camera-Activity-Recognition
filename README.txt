This project detects the Single Person Human Activity in a Multi Camera Environment.
Assumptions - No other object , Single Person
Camera Setup - Any

Requirements - 

Python 3.5 or above
Environment - Anaconda
Libraries - scikit , matplotlib , dill , tkinter , subprocess 
Dataset - 
IXMAS download link - 'http://4drepository.inrialpes.fr/public/viewgroup/6"
IXMAS Feature Vectors are included in IXMAS Folder.
For testing download Hedlena(1,2,3), julien(1,2,3) & Nicolas(1,2,3) 
Then make a folder named 'final_folder' and then make 5 folders for 5 different cameras named " cam0, cam1, cam2, cam3, cam4 ".
Then arrange the downloaded frames camera wise and number then starting from index 0 to total number of images present.  


How to execute - 
Use Anaconda Prompt.
Run minimal_gui.py
Click Training button to execute main_code.py which will train on the dataset(IXMAS) and save the results in train1.db.
Click Testing button to visualise the Frames for testing and get predicted output.
 
For Code- 
Use only jupyter notebook to use or edit .ipynb files.