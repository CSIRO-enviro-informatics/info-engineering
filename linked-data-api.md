# Linked Data APIs: theory and practice

Learning goals:
* Introduce Linked Data concepts
* Introduce Linked Data APIs
* Provide links to reference material and example Linked Data API implementations

## Theory

This section outlines theoretical aspects of Linked Data API design, rationale and related background.


### Background and designs


#### Linked Data

Linked Data is a way of publishing and interlinking structured data on the web using RDF. Resources and links between resources can be described in machine readable syntax along with human labels using RDF, thus allowing both human-readable and machine-readable content/interaction to access data resources and their
descriptive metadata using existing web technologies
simply by dereferencing HTTP URIs. 


https://www.w3.org/wiki/LinkedData
> The term Linked Data refers to a set of best practices for publishing structured data on the Web. These principles have been coined by Tim Berners-Lee in the design issue note Linked Data. The principles are:
>
> 1. Use URIs as names for things
> 2. Use HTTP URIs so that people can look up those names.
> 3. When someone looks up a URI, provide useful information.
> 4. Include links to other URIs. so that they can discover more things.
> 
> The idea behind these principles is on the one hand side, to use standards for the representation and the access to data on the Web. On the other hand, the principles propagate to set hyperlinks between data from different sources. These hyperlinks connect all Linked Data into a single global data graph, similar as the hyperlinks on the classic Web connect all HTML documents into a single global information space. Thus, LinkedData is to spreadsheets and databases what the Web of hypertext documents is to word processor files. The Linked Open Data cloud diagramms give an overview of the linked data sets that are available on the Web.

The _Resource Description Framework (RDF)_ is a W3C standard (Hayes and Patel-Schneider 2014).  Information elements consist of RDF statements. An RDF statement consist of three parts: _Subject_, _Predicate_, and _Object_. This is called a _triple_.

*Identifiers* are a key building block of RDF and _Uniform Resource Identifiers (URIs)_ are used to identify a resource. URIs can appear in each part of a triple, i.e. _Subjects_, _Predicates_ and _Objects_. Where an _Object_ is a _URI_, this may also be a subject for another statement. *Literals* are another key part of RDF and are used to capture basic values other than a URI. e.g. strings such as "Gerald", dates such as "1 April 2019", and numbers such as "4897". Literals are associated with a datatype so that it can be parsed. Literals may only appear in the object part of a RDF statement. 

RDF statements are collected together within an _RDF Graph_. Figure 1 below show an example of an RDF graph encoding information about the singer B.B. King.

![Figure 1. RDF Example: BB king](img/bb-king-rdf-example.png)

Pseudo-RDF statement
```
<B.B. King> <is a> <person>.
<B.B. King> <is born on> <the 16th of September 1925>. 
<B.B. King> <plays instrument> <guitar>
```

Valid RDF Statement expressed via the Turtle serialisation
```
@prefix :   <http://example.org/> .
@prefix foaf:  <http://xmlns.com/foaf/0.1/> .
@prefix rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix xsd:   <http://www.w3.org/2001/XMLSchema#> .

:BBKing  a foaf:Person ;
  :is_born_on "1925-09-16"^^xsd:date ;
  :plays_instrument :Guitar 
.
```

Equivalent RDF/XML serialisation
```
<rdf:RDF
    xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
    xmlns:ex="http://example.org/"
    xmlns:foaf="http://xmlns.com/foaf/0.1/"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema#" > 
  <rdf:Description rdf:about="http://example.org/BBKing">
    <plays_instrument rdf:resource="http://example.org/Guitar"/>
    <is_born_on rdf:datatype="http://www.w3.org/2001/XMLSchema#date">1925-09-16</is_born_on>
    <rdf:type rdf:resource="http://xmlns.com/foaf/0.1/Person"/>
  </rdf:Description>
</rdf:RDF>
```

Equivalent JSON-LD serialization
```
{
  "@id": "http://example.org/BBKing",
  "@type": "http://xmlns.com/foaf/0.1/Person",
  "http://example.org/is_born_on": {
    "@type": "http://www.w3.org/2001/XMLSchema#date",
    "@value": "1925-09-16"
  },
  "http://example.org/plays_instrument": {
    "@id": "http://example.org/Guitar"
  }
}
```

As you can see from the above, the RDF statements have not changed, however, they can be encoded or *serialised* via different content types - JSON-LD, RDF/XML or Turtle (and more). This provides more options for developing applications for users and consumers of this data. Some consumers implementing web browser applications may prefer the JSON-LD serialisation as there are compatible web front-end libraries to consume the data. Others may prefer the other content types (RDF/XML, Turtle, N-Triples) which may be supported by programming languages such as Java and Python.

The last thing to note about the above examples is the use of *namespaces*. As a general principle, we encourage the re-use of defined properties and well-known types as this enables greater data integration opportunities and leveraging common tools to parse/render the data with. `foaf` (or Friend-of-a-Friend) is an example of a namespace with well-known properties and types, and is used in the above example to express that B.B. King is a person. It allows that piece of data to be integrated with other data that use `foaf:Person`. This applies to other defined types and properties, e.g. namespaces include `rdfs:`, `skos:`, `owl:`, `dc:`. There may be a number of domain-specific namespaces for binding context to the data using relevant well-known properties and types in the respective domains e.g, [`sweet:`](http://sweetontology.net/) for the earth sciences, and [`envo:`](http://environmentontology.org/) for environment.


### "Conneg" (Content-negotiation)

#### By format / media-type

The HTTP protocol allows content-negotiation via headers (as key-value pair values) which accompany the request. The Accept request HTTP header advertises which content types, expressed as MIME types, the client is able to understand. Using content negotiation, the server then selects one of the proposals, uses it and informs the client of its choice with the Content-Type response header. Browsers set adequate values for this header depending on the context where the request is done: when fetching a CSS stylesheet a different value is set for the request than when fetching an image, video or a script.

https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html
> The Accept request-header field can be used to specify certain media types which are acceptable for the response. Accept headers can be used to indicate that the request is specifically limited to a small set of desired types, as in the case of a request for an in-line image.

The following example shows the `Accept` field that accompanies the HTTP request, i.e. *For this HTTP request, I would like (to Accept) this response format (`text/plain`)*:

```
    Accept: text/plain
```

Often browsers will have default Accept headers such as this:
```
text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
```

For Linked Data applications, these are generally the mime-types that are accomodated:
* `application/rdf+xml`	(RDF XML serialisation)
* `text/turtle`	(Turtle serialisation)	
* `application/ld+json` (JSON-LD serialisation)	
* `text/n3` (N3 serialisation)
* `application/n-triples` (N-Triples serialisation)



#### By profile

See https://www.w3.org/TR/dx-prof-conneg/

### Linked Data APIs

Linked Data relies on existing web standards and approaches - URIs, HTTP and content types and REST. However, other than that, there is currently is no standard patterns for delivering data resources on the web, i.e. middleware to publish Linked Data resources and APIs for making it easy for developing applications while adhering to Linked Data principles and approaches. 

Linked Data APIs (LD-APIs) and implementation software enable the publication of data as Linked Data. The implementation code libraries provide an important bridge between the data and Linked Data consumers by implementing features. Features include Content Negotiation by media type (HTML vs. JSON-LD vs. Turtle vs. RDF/XML) and more recently, Content negotiation by profile, which allows users to query different views of the data. 


## Practice

This section outlines practical aspects of applying Linked Data APIs in implementations as well
as examples deployed.

### Code libraries

pyLDAPI
https://pypi.org/project/pyldapi/

ELDA
http://epimorphics.github.io/elda/current/index.html

SKOSMOS
http://www.skosmos.org/

Linked Data Registry
http://ukgovld.github.io/ukgovldwg/guides/registry.html 

### Implementations/instances



https://www.geo.admin.ch/en/geo-services/geo-services/linkeddata.html

Geoscience Australia
http://pid.geoscience.gov.au/sample/

#### pyLDAPI


Loc-I Dataset APIs
https://asgsld.net/

G-NAF Dataset APIs
https://gnafld.net/



#### SISSVoc/ELDA


ARDC's RVA 
https://documentation.ardc.edu.au/display/DOC/Linked+Data+API

#### SKOSMOS

http://vocabularies.unesco.org/browser/thesaurus/en/
http://aims.fao.org/vest-registry/vocabularies/agrovoc
http://finto.fi/en/

#### Linked Data Registry

Ordnance Survey Linked Data Platform
http://data.ordnancesurvey.co.uk/

Environment Registry
http://environment.data.gov.uk/registry/

WMO codes registry
http://codes.wmo.int/

CSIRO Linked DAta Registry
http://registry.it.csiro.au/?_browse=true

