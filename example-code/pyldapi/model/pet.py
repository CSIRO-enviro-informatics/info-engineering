from flask import Response, render_template
from pyldapi import Renderer, Profile
from datetime import datetime
from io import StringIO
import requests
from rdflib import Graph, URIRef, RDF, RDFS, XSD, OWL, Namespace, Literal, BNode
import _config as config
import json


MyPetView = Profile("http://example.org/def/mypetview", "PetView", "A profile of my pet.", ['text/html', 'text/turtle'], 'text/html')

class PetRenderer(Renderer):
    def __init__(self, request, uri, instance, pet_html_template, **kwargs):
        self.profiles= {'mypetview': MyPetView}
        self.default_profile_token = 'mypetview'
        super(PetRenderer, self).__init__(
            request, uri, self.profiles, self.default_profile_token, **kwargs)
        self.instance = instance
        self.instance['_context'] = {
           "request" : request,
           "uri" : uri,
        }
        self.pet_html_template = pet_html_template

    def _render_mypetview(self):
        self.headers['Profile'] = 'http://example.org/def/mypetview'
        if self.mediatype == "text/html":
            return Response(render_template(self.pet_html_template, **self.instance))
        elif self.mediatype == "text/turtle":
            return Response(self.export_rdf(self, rdf_mime='text/turtle'),
                            mimetype="application/json", status=200)

    def export_rdf(self, model_view='petview', rdf_mime='text/turtle'):
        g = Graph()
        s  = URIRef(self.instance_uri)
        n = Namespace("http://example.org/pets#")        

        g.add((s, RDF.type, URIRef('http://dbpedia.org/resource/Dog')))
        g.add((s, n.breed, Literal(self.instance['breed'])))
        g.add((s, n.age, Literal(self.instance['age'], datatype=XSD.integer)))
        g.add((s, n.color, Literal(self.instance['color'])))
        return g.serialize(format=self._get_rdf_mimetype(rdf_mime))


    def _get_rdf_mimetype(self, rdf_mime):
        return self.RDF_SERIALIZER_TYPES_MAP[rdf_mime]

    # All `Renderer` subclasses _must_ implement render
    def render(self):
        response = super(PetRenderer, self).render()
        if not response and self.profile == 'mypetview':
            response = self._render_mypetview()
        elif self.profile == 'alt':
            return response
        else:
            raise NotImplementedError(self.profile)
        return response


if __name__ == '__main__':
    pass
