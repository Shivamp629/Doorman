# Doorman-

Instructions to run:
1. Clone github repo
2. Open up 2 terminal windows and run the following commands
  
  Terminal 1:   #opens webcam
  (i) "cd Doorman/new/cv"
  (ii) "python3 cameraCV.py"
  
  Terminal 2:   #runs server
  (i) "cd Doorman/new"
  (ii) "python3 main.py"
  
3. Open "http://localhost:5000" in browser
4. Change your emotion, and enjoy!
  
  
  
Instructions to add new person in classifier:
1. Open the Doorman/new/cv/take_images.py file
2. Change person variable to the name of the person (No spaces, no commas etc)
3. Assign a new unique person_number
4. In the 'training-data' folder, create a new folder whose name is the unique person_number.
5. Run the following commands:
      (i) "cd Doorman/new/cv"
      (ii) "python3 take_images.py"
6. In cameraCV.py, add an entry to the 'people' dictionary with key=unique_number and value=Name of the new person

