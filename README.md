# Pattern Recognition
This is attemp to solve kaggle problem of recognizing character in google street's picture.
http://www.kaggle.com/c/street-view-getting-started-with-julia

#Step
1. Extract feature as every single pixel and build training matrix
2. Reduce feature by taking linear combination of pixel and minimize projection error. Cut the new feature but we can still have 90% of data
3. Apply the matrix data to ML algorithma such as Random Forest or SVM

#Future Plan
Currently library is written in python and utulize scikit as machine learning Library. Future plan is to build in Java and use neural network/deep leaning library such as Encog etc

Thanks for coming
