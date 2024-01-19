# SkyNet-Reachability-Study

# Learning from Networks Project

This project was developed as part of the course "Learning from Networks" for the Masters of Computer Engineering program. The goal of this project is to analyze network data and perform different algorithms on the data.

This project was developed as part of the course "Learning from Networks" for the Masters of Computer Engineering program. The goal of this project is to analyze a transportation reachability network for cities in the United States and Canada and perform different graph related algorithms on the data.

## Dataset

The dataset used in this project is a transportation reachability network for cities in the United States and Canada. The network consists of nodes representing cities and weighted edges indicating the estimated airline travel time between cities. The network is asymmetric due to factors like headwinds. The dataset includes the following information:

- Number of Nodes: 456
- Number of Edges: 71,959

Additionally, the dataset provides the following metadata for each city:

- Metropolitan Population
- Latitude
- Longitude

### Source (Citation)

- For the network:
  - Brendan J. Frey and Delbert Dueck. "Clustering by passing messages between data points." Science 315.5814 (2007): 972-976.

- For the city metadata (metropolitan population, latitude, and longitude):
  - Austin R. Benson, David F. Gleich, and Jure Leskovec. "Higher-order Organization of Complex Networks." Science, 353.6295 (2016): 163–166.

## Instructions to Replicate Experiments

To replicate the experiments and obtain the same output, follow these steps:

1. Download the dataset from the provided link: [Reachability Dataset](https://snap.stanford.edu/data/reachability.html)

2. Extract the dataset files to a directory on your local machine.

    2.1. To get the information about the country, we have used `get_country_info.py`

3. Install the required dependencies by running the following command:
`pip install -r requirements.txt`

4. Open the main script file, `main.py`, and modify the file paths to point to the location of the downloaded dataset files.

5. Run the main script using the following command:
`python main.py`

6. The script will perform network analysis and clustering using message passing algorithms on the dataset.

7. The output of the experiments will be saved to the specified output directory.

## Results

The results of the experiments can be found in the output directory. The output includes various visualizations and analysis of the network data, as well as the clustering results.

## License

This project is licensed under the [Apache License](LICENSE).

## Contact Information

For any questions or inquiries, please contact:

- Name: Reihaneh Baghishani
- Email: reihaneh.baghishani@gmail.com