# Tutorial: Linked Data APIs Part 1 

A tutorial introducing content negotiation and RDF software libraries via 
a python-based Jupyter notebook.

In this tutorial, we will learn to:
1. Build a very simple Pizza ontology from scratch
2. Import an ontology into the Topbraid editor
3. Begin querying data using RDF and OWL

<!-- TOC depthFrom:2 -->

- [Tutorial: Linked Data APIs Part 1](#tutorial-linked-data-apis-part-1)
  - [Learning Objectives](#learning-objectives)
  - [Pre-requisites and assumptions](#pre-requisites-and-assumptions)
  - [Part 1. RDF Graphs (20-30mins)](#part-1-rdf-graphs-20-30mins)
    - [Exercise 1](#exercise-1)
      - [For discussion](#for-discussion)
  - [Part 2.  HTTP Content Negotiation (Conneg) (20-30mins)](#part-2-http-content-negotiation-conneg-20-30mins)
    - [Exercise 2.A. Content Negotiation By Media type](#exercise-2a-content-negotiation-by-media-type)
      - [For discussion](#for-discussion-1)
    - [Exercise 2.B. Content Negotiation By Profile](#exercise-2b-content-negotiation-by-profile)
      - [For discussion](#for-discussion-2)
  - [References](#references)

<!-- /TOC -->

## Learning Objectives

Attendees will:
* 

## Pre-requisites and assumptions

* Access to a Jupyter notebook server with the following python libraries installed:
  * RDFlib
  * requests
* Familiarity with the HTTP protocol
* Familiarity with RDF


## Part 1. RDF Graphs (20-30mins)

Objective: Understand how to work with RDF graphs and output different serialisations

In this part of the tutorial, we will be parsing an RDF file and loading it in using the RDFLib python 
module.

You'll need to open up this Jupyter notebook: [Linked Data Example 1.ipynb](https://github.com/CSIRO-enviro-informatics/info-engineering/blob/master/notebooks/ld-api/Linked%20Data%20Example%201.ipynb)


### Exercise 1

Run through Section 1 of `Linked Data Example 1.ipynb`.


#### For discussion
* 

## Part 2.  HTTP Content Negotiation (Conneg) (20-30mins)


Objective: Understand how to issue HTTP Content Negotiation mediated calls using python 

In this part of the tutorial, we will be parsing an RDF file and loading it in using the RDFLib python 
module.


You'll need to open up this Jupyter notebook: [Linked Data Example 2.ipynb](https://github.com/CSIRO-enviro-informatics/info-engineering/blob/master/notebooks/ld-api/Linked%20Data%20Example%202.ipynb)


### Exercise 2.A. Content Negotiation By Media type

Run through Part 1 of `Linked Data Example 2.ipynb` .

#### For discussion
* 

### Exercise 2.B. Content Negotiation By Profile

Run through Part 2 of `Linked Data Example 2.ipynb`.

#### For discussion
* 

## References

Check out the [Learning resources](../learning-resources.md) section for more material.

Other related pages:

* Content negotiation by media type: [W3C SPARQL Specification](https://www.w3.org/TR/rdf-sparql-query/)
* Content negotiation by profile: [W3C SPARQL Specification](https://www.w3.org/TR/rdf-sparql-query/)
* [Getting started with rdflib](https://rdflib.readthedocs.io/en/stable/gettingstarted.html)

