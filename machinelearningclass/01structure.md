
Training Data
[name:str,
uploaded:datetime,
tested:datetime]

Tuning
List[Hyperparameter]

Hyperparameter
[
    k:int,
    quantity:float,
    ===============
    classify(s:Sample):str
]

| Training | Testing
List[Known Sample]

Sample
[data fields]


KnownSample
[data fields
+ result ]

The TrainingData class is a container with two lists of data samples, a list used for training our model and a list used for testing our model. Both lists are composed of KnownSample instances. Additionally, we’ll also have a list of alternative Hyperparameter values. In general, these are tuning values that change the behavior of the model. The idea is to test with different hyperparameters to locate the highest-quality model. We’ve also allocated a little bit of metadata to this class:

The name of the data we’re working with
The datetime of when we uploaded the data the first time
The datetime of when we tested the model
Each instance of the Sample class is the core piece of working data.


A KnownSample object is an extended Sample. A KnownSample is a Sample with one extra attribute, the assigned result. This information comes from already labeled,data we can use for training and testing.

The Hyperparameter class has the k used to define how many of the nearest neighbors to consider. (k-neighbors)
 It also has a summary of testing with this value of k. The quality tells us how many of the test samples were correctly classified. We expect to see that small values of k (like 1 or 3) don’t classify well. We expect middle values of k to do better, and very large values of k to not do as well.



