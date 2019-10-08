# Social Influence Graph

The idea is to define an **Influence Artist Graph**, which is built using [DBpedia Ontology](https://wiki.dbpedia.org/). 

Basically, we start with a bunch of well-known artist (taken from a [Wikiart's dataset](https://www.kaggle.com/c/painter-by-numbers/data)), who will be our seed to navigate through the ontology. 

In our case, we use the *"influence by"* relationship to link the artists.

With the **Influence Artist Graph** it is possible to calculate some metrics (such as centrality, dispersion, etc.) that will be useful to materialize the impact that some artists have over others. 
