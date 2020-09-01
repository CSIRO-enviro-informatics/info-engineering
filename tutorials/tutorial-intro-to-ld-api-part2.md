# Tutorial: Introduction to LD APIs Part 2


A tutorial to introduce LD APIs using pyldapi.

In this tutorial, we will learn to:
1. Extend an existing pyldapi implementation
2. Add a new LD API


<!-- TOC depthFrom:2 -->

- [1. Learning Objectives](#1-learning-objectives)
- [2. Pre-requisites and assumptions](#2-pre-requisites-and-assumptions)
- [3. Introducing the Pet LD API](#3-introducing-the-pet-ld-api)
    - [3.1. Basic layout of a pyLDAPI implementation](#31-basic-layout-of-a-pyldapi-implementation)
    - [3.2 Pets Register](#32-pets-register)
    - [3.3. Pets Viewer](#33-pets-viewer)
    - [Exercise 1: Dive into the MVC framework for the Pet register](#exercise-1-dive-into-the-mvc-framework-for-the-pet-register)
    - [Exercise 2. Add a new pet](#exercise-2-add-a-new-pet)
    - [Exercise 3. Let's add a new Pet view](#exercise-3-lets-add-a-new-pet-view)
    - [Summary](#summary)
- [4. Adding a Pizza registry based on DBPedia resources](#4-adding-a-pizza-registry-based-on-dbpedia-resources)
    - [4.1. Explore DBPedia and query Pizza resources](#41-explore-dbpedia-and-query-pizza-resources)
    - [4.2. Add the Pizza register](#42-add-the-pizza-register)
        - [4.2.1. Add a route for the Pizza Register](#421-add-a-route-for-the-pizza-register)
        - [4.2.2. Add a function that will fetch the items for the response](#422-add-a-function-that-will-fetch-the-items-for-the-response)
    - [4.3. Add the Pizza item views](#43-add-the-pizza-item-views)
        - [4.3.1. Query DBPedia for RDF content](#431-query-dbpedia-for-rdf-content)
        - [4.3.2. Add the Pizza instance model and views](#432-add-the-pizza-instance-model-and-views)
        - [4.3.3. Add a PizzaRenderer class in a new pizza model](#433-add-a-pizzarenderer-class-in-a-new-pizza-model)
        - [4.3.4. Update controller/classes.py to query for the pizzas](#434-update-controllerclassespy-to-query-for-the-pizzas)
        - [4.3.5. Add a basic view template for pizza](#435-add-a-basic-view-template-for-pizza)
        - [4.3.6. Modify the Pizza view template and model to render abstract and thumbnail](#436-modify-the-pizza-view-template-and-model-to-render-abstract-and-thumbnail)
    - [Summary](#summary-1)

<!-- /TOC -->

## 1. Learning Objectives

Attendees will:
* Be exposed to a pyLDAPI example and gain an understanding of the elements of a Linked Data API
* Learn how to exLearn basic elements of information modelling using OWL
* Gain hands-on experience with ontology development and querying using Topbraid Composer tools
* Learn the facets of the SPARQL language and how to query using SPARQL

## 2. Pre-requisites and assumptions

We will use the `/example-code/pyldapi` directory as a starting point and a template for an implementation of a 
pyLDAPI service.

* Code checked out from https://github.com/CSIRO-enviro-informatics/info-engineering 
* Python coding experience
* Python environment setup following instructions from [example README.md](https://github.com/CSIRO-enviro-informatics/info-engineering/blob/master/example-code/pyldapi/README.md)
* Familiarity with Linked Data concepts


## 3. Introducing the Pet LD API

See presentation slides for overview of the Pet LD API.

### 3.1. Basic layout of a pyLDAPI implementation

The recommended layout of a pyLDAPI implementation is using the Model-View-Controller pattern and 
creating directories to suit. See below:

```
/
-- model/
    -- pet.py
-- view/
    -- static/
        ...
    -- templates/
        ...
        page_pet.html        
-- controller/
    -- classes.py
    -- pages.py
-- app.py
-- _config.py
...
```

Let's run the example pyLDAPI. If you haven't run the code yet, run the following
```
$ virtualenv venv
$ source venv/bin/activate
# Or on a windows bash client
$ source venv/Scripts/activate
$ pip install -r requirements.txt
$ export FLASK_APP=app.py
$ export FLASK_ENV=development
$ flask run --port=3000 --host=0.0.0.0
```

### 3.2 Pets Register

Let's look at the Pets register at `http://localhost:3000/pets/`.

We can see the pets listed in the register. The Pet Register functionality is defined in the code base in the following file:
 `/controller/classes.py` (just glance at it - we'll look at it in more detail later).


### 3.3. Pets Viewer

Let's click on one of the Pets - Rex, and take a look at the view of a Pet instance.

We can see a basic landing page for the Pet Rex. 

The information used to populat the Pet instance view comes from:
- `/controller/classes.py`
- `/model/pet.py`

The Jinja template is used to render the view of the information for Rex. THis is located at:
- `/view/templates/page_pet.html`

### Exercise 1: Dive into the MVC framework for the Pet register

Take a closer look at these files and draw a map of how the files are connected to render the Pet view.
- `/controller/classes.py`
- `/model/pet.py`
- `/view/templates/page_pet.html`


### Exercise 2. Add a new pet

Now let's add a new pet. 

Which file and where in the file would we add the required information?

What do you notice about the information model?


### Exercise 3. Let's add a new Pet view

Based on the template that exists, develop some code to add a new Pet view.


### Summary

We have covered how the Pet section of the Example pyLDAPI works using a very basic (JSON) dataset 
and how to extend it for different LD Views.


## 4. Adding a Pizza registry based on DBPedia resources

In this next part of the tutorial, we will work on adding a new Register - a Pizza register.
We will reuse definitions from DBPedia and expose them as Linked Data resources.


### 4.1. Explore DBPedia and query Pizza resources

Go to https://dbpedia.org/sparql and put in the SPARQL query text shown below in the Query editor.
This will query all Pizza types and their label.

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX dbo: <http://dbpedia.org/ontology/>
select distinct ?p ?label 
where {
    ?p dbo:type <http://dbpedia.org/resource/Pizza> .
    ?p rdfs:label ?label .
    FILTER(LANG(?label) = "" || LANGMATCHES(LANG(?label), "en")) 
} LIMIT 100
```

We can use this query as the basis for the Pizza Register we will now implement.

### 4.2. Add the Pizza register

To implement the Pizza Register, we need to:
- Add a route for the Pizza Register and implement the function to serve a response for that route
- Add a function that will fetch the items for the response

#### 4.2.1. Add a route for the Pizza Register

```python
from SPARQLWrapper import SPARQLWrapper, JSON

@classes.route('/pizza/')
def pizza():
    """
    The Register of Pizzas
    :return: HTTP Response
    """
    # prepare items for the ContainerRenderer response instance
    no_of_items = 0
    try:
        page = request.values.get('page') if request.values.get('page') is not None else 1
        per_page = request.values.get('per_page') if request.values.get('per_page') is not None else 20
        items = _get_pizza_items(page, per_page)
        no_of_items = len(items)
    except Exception as e:
        print(e)
        return Response('The Pizza Register is offline', mimetype='text/plain', status=500)    
    
    # create the ContainerRenderer response instance
    r = pyldapi.ContainerRenderer(
        request,
        request.url,
        'Pizza Register',
        'A register of Pizza',
        "http://example.org/def/Pizza",
        "Pizza",
        items,
        no_of_items
    )
    return r.render()
```

pyLDAPI provides the Register function via `ContainerRenderer`. `ContainerRenderer` expects these inputs:
- flask request object
- request url
- Label
- Comment/description
- URL
- parent_container_uri,
- parent_container_label,
- container members,
- container member count


#### 4.2.2. Add a function that will fetch the items for the response

We will now implement the `_get_pizza_items()` function from the above and using the .
The SPARQL Endpoint is located at http://dbpedia.org/sparql.

The [SPARQLWrapper](https://github.com/RDFLib/sparqlwrapper) library is used to issue the remote queries in python.

```python
def _get_pizza_items(page, per_page):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX dbo: <http://dbpedia.org/ontology/>
        select distinct ?p ?label 
        where {
            ?p dbo:type <http://dbpedia.org/resource/Pizza> .
            ?p rdfs:label ?label .
            FILTER(LANG(?label) = "" || LANGMATCHES(LANG(?label), "en")) 
        } LIMIT 100
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    arr_items = []
    for result in results["results"]["bindings"]:
        label = result["label"]["value"]
        uri = result["p"]["value"]
        tokens = uri.split("http://dbpedia.org/resource/")
        pizza_name = tokens[1]
        # Format array of items the way pyldapi requires
        arr_items.append( ("{}pizza/{}".format(request.url_root, pizza_name), label, "pizza") )
    return arr_items  
```

pyldapi expects the array of items in the register to have a particular structure. It requires (URI, URI, label) or (URI, label).

You should now have a working pizza registry at http://localhost:3000/pizza/

### 4.3. Add the Pizza item views

We now want to enable users to be able to view each Pizza and some details, as well as content negotiate by media type.

#### 4.3.1. Query DBPedia for RDF content

DBPedia has a specific way of providing RDF content via the URL template (text/turtle):
```
http://dbpedia.org/data/{Name of the Resource}.ttl
```

We want to load this into our environment and render the information in a tailored way.

#### 4.3.2. Add the Pizza instance model and views

We will create 2 new files - the `PizzaRenderer` class in the `/model/pizza.py` file and a Jinja view template file in `/view/templates/page_pizza.html`

```
/
-- model/
    -- pizza.py
-- view/
    -- templates/
        page_pizza.html        
```


#### 4.3.3. Add a PizzaRenderer class in a new pizza model

```python
{% raw %}
from flask import Response, render_template
from pyldapi import Renderer, Profile
from datetime import datetime
from io import StringIO
import requests
from rdflib import Graph, URIRef, RDF, RDFS, XSD, OWL, Namespace, Literal, BNode
import json
from rdflib.plugin import register, Serializer, Parser
register('json-ld', Serializer, 'rdflib_jsonld.serializer', 'JsonLDSerializer')
register('json-ld', Parser, 'rdflib_jsonld.parser', 'JsonLDParser')

MyPizzaView = Profile("http://example.org/def/mypizzaview", "PizzaView", "A profile of my pizza.", ['text/html', 'text/turtle', 'application/ld+json'], 'text/html')

class PizzaRenderer(Renderer):
    def __init__(self, request, uri, instance, pizza_html_template, **kwargs):
        self.profiles= {'mypizzaview': MyPizzaView}
        self.default_profile_token = 'mypizzaview'
        super(PizzaRenderer, self).__init__(
            request, uri, self.profiles, self.default_profile_token, **kwargs)
        self.instance = instance
        self.instance['_context'] = {
           "request" : request,
           "uri" : uri,
        }
        self.instance['_data'] = {}
        self._populate_instance_from_rdf()
        self.pizza_html_template = pizza_html_template

    def _render_mypizzaview(self):
        self.headers['Profile'] = 'http://example.org/def/mypizzaview'
        if self.mediatype == "text/html":
            return Response(render_template(self.pizza_html_template, **self.instance))
        elif self.mediatype == "text/turtle":
            return Response(self.instance['graph'].serialize(format='turtle').decode('utf-8'),
                            mimetype="text/turtle", status=200)
        elif self.mediatype == "application/ld+json":
            return Response(self.instance['graph'].serialize(format='json-ld', indent=4).decode('utf-8'),
                            mimetype="application/ld+json", status=200)

    def _get_rdf_mimetype(self, rdf_mime):
        return self.RDF_SERIALIZER_TYPES_MAP[rdf_mime]

    def _populate_instance_from_rdf(self):
        query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            select distinct ?abstract ?thumbnail
            where {{
                ?pizza dbo:abstract ?abstract .
                ?pizza dbo:thumbnail ?thumbnail .
                FILTER(LANG(?abstract) = "" || LANGMATCHES(LANG(?abstract), "en")) 
            }} LIMIT 100
            """.format(self.instance["_context"]['uri'])
        print(query)
        qres = self.instance['graph'].query(query)       
        for row in qres:
            self.instance['_data']['abstract'] = row[0]
            self.instance['_data']['thumbnail'] = row[1]

    # All `Renderer` subclasses _must_ implement render
    def render(self):
        response = super(PizzaRenderer, self).render()
        if not response and self.profile == 'mypizzaview':
            response = self._render_mypizzaview()
        elif self.profile == 'alt':
            return response
        else:
            raise NotImplementedError(self.profile)
        return response

if __name__ == '__main__':
    pass
{% endraw %}
```

#### 4.3.4. Update controller/classes.py to query for the pizzas

```python  
from model.pizza import PizzaRenderer
from rdflib import Graph
@classes.route('/pizza/<string:pizza_name>')
def pizza_instance(pizza_name):
    instance = None
    pizza_ttl_url = "http://dbpedia.org/data/{}.ttl".format(pizza_name)
    print(pizza_ttl_url)

    #get the Turtle format for the pizza
    r = requests.get(pizza_ttl_url)
    print(r.status_code)
    print(r.text)
    rdf_data = r.text
    #load into RDFLib
    g = Graph()
    g.parse(data=rdf_data, format="turtle")
    instance = {"graph" : g}
    if instance is None:
        return Response("Not Found", status=404)
    renderer = PizzaRenderer(request, request.base_url, instance, 'page_pizza.html')
    return renderer.render()
```

#### 4.3.5. Add a basic view template for pizza
Create a file called `/view/templates/page_pizza.html` with the following lines in (the following file in this link)[ld-api-intro-p2/pizza-1.txt].

Add the following links top in (the following file in this link)[ld-api-intro-p2/pizza-2.txt]

#### 4.3.6. Modify the Pizza view template and model to render abstract and thumbnail

Add this function to `/model/pizza.py` 
```python
    def _populate_instance_from_rdf(self):
        query = """
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
            PREFIX dbo: <http://dbpedia.org/ontology/>
            select distinct ?abstract ?thumbnail
            where {{
                ?pizza dbo:abstract ?abstract .
                ?pizza dbo:thumbnail ?thumbnail .
                FILTER(LANG(?abstract) = "" || LANGMATCHES(LANG(?abstract), "en")) 
            }} LIMIT 100
            """.format(self.instance["_context"]['uri'])
        print(query)
        qres = self.instance['graph'].query(query)       
        for row in qres:
            self.instance['_data']['abstract'] = row[0]
            self.instance['_data']['thumbnail'] = row[1]
```

Modify the `__init__` function to add these lines to call the above function in `/model/pizza.py`:
```python
        self.instance['_data'] = {}
        self._populate_instance_from_rdf()
```

Update `/view/templates/page_pizza.html` with the following lines in (the following file in this link)[ld-api-intro-p2/pizza-2.txt].


### Summary

We have covered how the Pet section of the Example pyLDAPI works using a very basic (JSON) dataset 
and how to extend it for different LD Views.
