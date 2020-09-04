"""
This file contains all the HTTP routes for classes used in this service
"""
from flask import Blueprint, request, Response
import _config as config
import pyldapi
import requests
from io import BytesIO
from lxml import etree
from pyldapi import ContainerRenderer
from model.pet import PetRenderer
import json
import os

import pprint

classes = Blueprint('classes', __name__)


dogs = [
    {
        "name": "Rex",
        "breed": "Dachshund",
        "age": 7,
        "color": "brown",
    }, {
        "name": "Micky",
        "breed": "Alsatian",
        "age": 3,
        "color": "black",
    },
    {
        "name": "Lucky",
        "breed": "Terrier",
        "age": 1,
        "color": "white"
    }
]


@classes.route('/pet/dog/<string:dog_id>')
def dog_instance(dog_id):
    instance = None
    for d in dogs:
        if d['name'] == dog_id:
            instance = d
            break
    if instance is None:
        return Response("Not Found", status=404)
    renderer = PetRenderer(request, request.base_url, instance)
    return renderer.render()

@classes.route('/pets/')
def pets():
    """
    The Register of Pets
    :return: HTTP Response
    """

    # get the total register count from the XML API
    try:
        no_of_items = int(len(dogs))
        page = request.values.get('page') if request.values.get('page') is not None else 1
        per_page = request.values.get('per_page') if request.values.get('per_page') is not None else 20
        items = _get_pet_items(page, per_page)
    except Exception as e:
        print(e)
        print(no_of_items)
        return Response('The Pets Register is offline', mimetype='text/plain', status=500)

    r = pyldapi.ContainerRenderer(
        request,
        request.url,
        'My Awesome Pets Register',
        'A register of Pets',
        "http://example.org/def/Animal",
        "Animal",
        items,
        no_of_items
    )
    return r.render()

def _get_pet_items(page, per_page):
   #TODO:pagination
   arr_items = []
   for item in dogs:
      name = item['name']
      print(request.url_root)
      arr_items.append( ("{}pet/dog/{}".format(request.url_root, name), name, "pet") )  
   return arr_items

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