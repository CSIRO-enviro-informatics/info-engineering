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
        'Pets Register',
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

