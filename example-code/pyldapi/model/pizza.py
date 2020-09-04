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

MyPizzaView = Profile("http://example.org/def/mypizzaview", 
                "PizzaView", "A profile of my pizza.", 
                [
                        'text/html', 
                        'text/turtle', 
                        'application/ld+json'
                ], 'text/html')

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
            PREFIX prov:	<http://www.w3.org/ns/prov#> 
            select distinct ?abstract ?thumbnail ?derivedFromUri
            where {{
                ?pizza dbo:abstract ?abstract .
                ?pizza dbo:thumbnail ?thumbnail .
                ?pizza prov:wasDerivedFrom	?derivedFromUri .
                FILTER(LANG(?abstract) = "" || LANGMATCHES(LANG(?abstract), "en")) 
            }} LIMIT 100
            """.format(self.instance["_context"]['uri'])
        print(query)
        qres = self.instance['graph'].query(query)       
        for row in qres:
            self.instance['_data']['abstract'] = row[0]
            self.instance['_data']['thumbnail'] = row[1]
            self.instance['_data']['derivedFromUri'] = row[2]

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