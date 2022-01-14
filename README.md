# Plant-Disease-Detection-Live-Project-UDEMY-

Plant disease, an impairment of the normal state of a plant that interrupts or modifies its vital functions. All species of plants, wild and cultivated alike, are subject to disease. Although each species is susceptible to characteristic diseases, these are, in each case, relatively few in number.[1] Some of the plant diseases that affect plants are:

##### 1. Black Spot
Black spot is one of the most common diseases found on roses, but it can also occur on other ornamental and garden plants.  This fungal disease causes black, round spots that form on the upper sides of leaves. Black spot spores overwinter in the fallen leaves. [2]

##### 2. Powdery Mildew
Powdery mildew is a fungal disease that affects many of our landscape plants, flowers, vegetables and fruits. Powdery mildew is an easy one to identify. Infected plants will display a white powdery substance that is most visible on upper leaf surfaces, but it can appear anywhere on the plant including stems, flower buds, and even the fruit of the plant.  This fungus thrives during low soil moisture conditions combined with high humidity levels on the upper parts of the plant surface.  It tends to affect plants kept in shady areas more than those in direct sun.[2]

##### 3. Downy Mildew
Downy mildews, are more related to algae and produce grayish fuzzy looking spores on the lower surfaces of leaves.  To identify downy mildew, look for pale green or yellow spots on the upper surfaces of older leaves. Downy mildew occurs during cool, moist weather such as in early spring or late fall.  Spore production is favored by temperatures below 65°F and with a high relative humidity. [2]

##### 4. Blight
Blight affects other plants, particularly potatoes and tomatoes. Blight is a fungal disease that spreads through spores that are windborne.  For this reason, spores can cover large areas and rapidly spread the infection.  Blight can only spread under warm humid conditions, especially with two consecutive days of temps above 50°F, and humidity above 90% for eleven hours or more. No cure exists.  Prevention is the only option.[2]

##### 5. Canker
Canker is often identified by an open wound that has been infected by fungal or bacterial pathogens.  Some cankers are not serious while others can be lethal.  Canker occurs primarily on woody landscape plants.[2]

##### 6. Common Rust
Common corn rust, caused by the fungus Puccinia sorghi, is the most frequently occurring of the two primary rust diseases of corn in the U.S., but it rarely causes significant yield losses in Ohio field (dent) corn. Occasionally field corn, particularly in the southern half of the state, does become severely affected when weather conditions favor the development and spread of the rust fungus. Sweet corn is generally more susceptible than field corn. In years with exceptionally cool summers, and especially on late-planted fields or sweet corn, yield losses may occur when the leaves at and above the ears become severely diseased before grain fill is complete. [3]

This live project app is executed to find out if the image of a leaf of a plant is diseased or not. Here, we are focusing on Common RUst in Corn, Blight in Potatoes and Bacterial Spots (Black Spots) in Tomatoes. The dataset consists of 900 images of plant leaves, 300 each of corn, potatoes and tomatoes. 

### ALGORITHM
Since the problem statement is of image detection, Convolutional Neural Networks will be used for this particular model.

1. Import the necessary libraries, notably for image processing, labelling as well as CNN modelling
2. Plot the images to view the dataset
3. Converting images to 256 * 256 pixelated array, from RGB to Greyscale (as Greyscale has 256 arrays from 0 to 255)
4. Create the labels for the dependent variable. Three labels are created - 0 for Corn with Common Rust, 1 for Early Blight in Potatoes and 2 for Tomato-Bacteria
5. Visualize the number of classes Count (3 for this project). The dataset, possessing equal number of images for all three classes, is a balanced dataset.
6. Check the size of the images by testing it on the first image of the dataset. All images are resized to be the same (256 * 256 * 3)
7. Split the dataset into train and test sets
8. Normalize the values of the array by 255 (as the last value on the grayscale is 255)
9. COnvert the dependent variable to categorical data type for classification
10. Define the model. The model is Convolutional Neural Network (CNN) with the following layers: 
  a. Conv2D layer of 32 neurons and filter size (3, 3) with relu activation function
  b. Max Pooling 2D layer of pool size (3,3)
  c. Conv2D layer of 16 neurons and filter size (2, 2) with relu activation function
  d. Max Pooling 2D layer of pool size (2,2)
  e. Flatten layer
  f. Dense layer of 8 neurons with relu activation function
  g. Dense layer of 3 neurons with softmax activation function, which is used for classification
11. Set the loss function to 'categorical crossentropy' with Adam optimizer.
12. Split the training set into train set and validation set
13. Train the CNN model with 50 epochs and batch size = 128
14. Save the model in h5 and json format in the executable folder of the app
15. Plot the accuracy of the model
16. Calculate the accuracy of the model for the test set. The model of this app gives an accuracy of 98.33333492279053
17. Calculate the prediction values of the depedent label values of the test set
18. Plot the predicted image of one of the leaves from the test set to compare with the actual leaf.
19. Displaying the label of the predicted and actual leaf.

The app is then executed via Streamlit on a local server, where you can upload an image of a leaf of either a potato, tomato or corn to predict.

### References:
1. https://www.britannica.com/science/plant-disease
2. https://earthsally.com/disease-control/common-plant-diseases.html
3. https://ohioline.osu.edu/factsheet/plpath-cer-02
