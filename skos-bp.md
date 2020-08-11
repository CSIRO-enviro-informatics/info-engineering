---
permalink: /skos-bp.html
---

# Best practice in formalizing a SKOS vocabulary
_This page was originally developed as part of the [SEEGrid website](https://confluence.csiro.au/display/VOCAB/Best+practice+in+formalizing+a+SKOS+vocabulary)._

Some best practices have been developed that will assist in the preparation of a well-behaved, maintainable vocabulary.

(SKOS) is based on a vocabulary/thesaurus model, and was designed primarily to formalize existing vocabularies using the semantic web tools, and also smooth the transition towards the richer logic-based tools from ontology modeling. The aim of SKOS is to enable pre-existing controlled vocabularies to be consumed on the web and to allow vocabulary creators to publish born-digital vocabularies on the web.  To understand SKOS you have to have a basic understanding of controlled vocabularies (hierarchical relationships, broader and narrower terms where each node has a relationship)

SKOS was built on RDF, and thus SKOS (a data sharing standard for formal logic and structure) data are represented as RDF triples.  This standard expresses data in a manner that is easily amenable to  computation and hence the usefulness. 

- [SKOS Simple Knowledge Organization System Primer](https://www.w3.org/TR/skos-primer/)
- [SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/) 
- [SKOS Play!](http://labs.sparna.fr/skos-play/convert) - convert Excel to SKOS
- [SKOS Quality Checker](https://qskos.poolparty.biz/) based on qSKOS
- [Key choices in the design of Simple Knowledge Organization System (SKOS)](https://doi.org/10.1016/j.websem.2013.05.001) - paper in Journal of Web Semantics

## Syntax

RDF examples on this page are shown using [Turtle](http://www.w3.org/TeamSubmission/turtle/) which is the most human readable syntax, though it is sometimes recommended that the maintenance versions are stored in [RDF/XML](http://www.w3.org/TR/REC-rdf-syntax/) which is the only format that is mandatory for RDF applications.

Resource identifiers in Turtle may be shown as either

*   full URIs, enclosed in angle-brackets,
    *   example: `<http://www.opengis.net/def/waterml/2.0/medium/GroundWater>`
*   abbreviated URIs or CURIEs, with no angle-brackets
    *   example: `medium:GroundWater` where the namespace prefix `medium:` stands for `http://www.opengis.net/def/waterml/2.0/medium/`

## Vocabulary content

Get the current vocabulary content from the organization responsible for its maintenance. Tell them about your intention to provide a web service to deliver it. Verify that they do not already provide such a service. Find out their versioning and maintenance policy. If possible, give them a formal role in the project, at least to ensure that you are notified of changes to vocabulary content. Discuss governance mechanisms, in particular how changes will be managed, and what the versioning policy is.

For each item in the vocabulary, make sure you have the following information:

*   text definition, or URL where that is available
*   all terms used conventionally to denote the item, including synonyms and multi-lingual synonyms
*   any symbols or abbreviations used to denote the item

If possible, also get

*   link to the authoritative definition
*   relationships with other items in the vocabulary - especially broader/narrower terms

## URIs and namespaces
### RDF Namespace

URIs for vocabulary elements (concepts, collections, concept schemes) should be **in a domain whose HTTP server can be configured** to either

*   serve the vocabulary elements directly, or
*   host a resolver or redirection service.

The URIs should be owned by, or at least acknowledge, the **vocabulary governance** body.

Namespace examples:

*   http://resource.geosciml.org/classifier/ics/ischart/
*   http://www.opengis.net/def/
*   http://vocab.nerc.ac.uk/collection/
*   http://registry.it.csiro.au/def/isotc211/MD_RestrictionCode/
*   http://registry.it.csiro.au/def/isotc211/MD_ScopeCode/
*   http://environment.data.gov.au/water/quality/def/property/
*   http://environment.data.gov.au/water/quality/def/object/

### URIs are case sensitive

Except for the domain name (i.e. the part between `http://` and the first single `/`) URIs are **case-sensitive**. It is often suggested that any URI which you expect people to enter by typing at a keyboard should be all lower-case. It also allows a server to be easily configured to be case-insensitive, using a simple rule to fold mixed-case into a single (lower) case.

### Vocabulary elements

All elements in a [SKOS](http://www.w3.org/TR/skos-reference/) vocabulary are denoted with URIs.

#### Ontology document

An "Ontology Document" packages descriptions of the elements of the vocabulary and dependencies.

Ontology URI examples:

*   http://registry.it.csiro.au/def/isotc211/MD_RestrictionCode?_format=ttl
*   http://resource.geosciml.org/vocabulary/timescale/isc-2012
*   http://resource.geosciml.org/vocabulary/cgi/201202/faulttype
*   http://www.w3.org/2002/07/owl
*   http://rdfs.org/ns/void

The Ontology URI plays no specific role in a vocabulary, but is involved with OWL dependency management, using the [`owl:imports`](http://www.w3.org/TR/owl-primer/#Ontology_Management) property. This mechanism essentially assumes that the complete ontology can be obtained from the ontology URI, in the [RDF/XML format](http://www.w3.org/TR/REC-rdf-syntax/). To enable this, the ontology document should be designated by an Ontology URI or location on a HTTP server where either

1.  an RDF/XML file can be placed, so that it can subsequently be downloaded by a simple HTTP request, or
2.  a suitable redirection or content generation operation can be triggered.

The Ontology URI may also name a 'graph' of content in a triple-store, which is derived from a single source.

#### Concepts

Vocabulary terms are associated with [SKOS Concepts](http://www.w3.org/TR/skos-primer/#secconcept).

Concept URIs are generally **unversioned**. The rationale for this is that a _concept is an abstract resource_ which does not in principle change. What we _know about a concept_ may change, and this will be captured in a _document describing the concept_ (also known as a 'graph')_._ The concept is not itself on the web, while the description is. The description is a concrete resource which should be denoted by a different URI to the concept, and may be versioned if what we know about the abstract resource changes. On the other hand, if a _concept_ has "changed", then it is a different concept and should be given a different URI, but the change will generally not be just by incrementing a number.

Concept URI examples:

*   http://resource.geosciml.org/classifier/ics/ischart/Furongian
*   http://resource.geosciml.org/classifier/ics/ischart/Silurian
*   http://www.opengis.net/def/nil/OGC/0/unknown
*   http://www.opengis.net/def/crs/EPSG/0/5711
*   http://www.opengis.net/def/waterml/2.0/medium/GroundWater
*   http://vocab.nerc.ac.uk/collection/A02/current/Wastewater/
*   http://vocab.nerc.ac.uk/collection/C17/current/31EK/
*   http://registry.it.csiro.au/def/isotc211/MD_RestrictionCode/patentPending
*   http://registry.it.csiro.au/def/isotc211/MD_RestrictionCode/trademark
*   http://environment.data.gov.au/water/quality/def/property/biochemical_oxygen_demand

(The version numbers in these URIs generally apply to the source of the definition, rather than concept identity.)

Several 'standard' patterns have been proposed to map the URI for an off-web resource to a URI for a document describing it.

*   In [DBpedia](http://dbpedia.org) the primary identifier for a real-world- or conceptual-thing contains the token _/resource/_, while the URI for the document that describes it replaces _/resource/_ with _/page/_,
    *   e.g. http://dbpedia.org/resource/Cambrian is described by http://dbpedia.org/page/Cambrian.
*   [W3C Cool URIs](http://www.w3.org/TR/cooluris/) advocates a similar pattern using the tokens _/id/_ and _/doc/_.
    *   e.g. http://www.example.com/ **id**/alice is described by http://www.example.com/ **doc**/alice
*   In SISSvoc the pattern is more explicit: the concept URI is an argument in the URI that identifies the description
    *   https://vocabs.ands.org.au/repository/api/lda/csiro/international-chronostratigraphic-chart/2018-revised-corrected/resource?uri=http%3A%2F%2Fresource.geosciml.org%2Fclassifier%2Fics%2Fischart%2FJurassic is the description of the concept `http://resource.geosciml.org/classifier/ics/ischart/Jurassic` according to the service `https://vocabs.ands.org.au/repository/api/lda/csiro/international-chronostratigraphic-chart/2018-revised-corrected/`.

#### Collections

[Collections](http://www.w3.org/TR/skos-primer/#seccollections) can be used for various purposes.

One application is to support partial URIs, treating the **concept URI as a path** so that each URI created by trimming a path element from the concept URI is realized as a skos:Collection. This provides entry points for exploring a vocabulary similar to browsing a traditional hierarchical file-system. Collections should be matched to every partial URI that the provider expects users to attempt to resolve.

Collection URI examples:

*   http://resource.geosciml.org/classifier/ics/ischart/
*   http://resource.geosciml.org/classifier/ics/ischart/Eras
*   http://resource.geosciml.org/classifier/ics/ischart/Boundaries
*   http://www.opengis.net/def/waterml/2.0/medium/
*   http://www.opengis.net/def/nil/OGC/0/
*   http://vocab.nerc.ac.uk/collection/A02/current/
*   http://vocab.nerc.ac.uk/collection/C17/current/
*   http://environment.data.gov.au/water/quality/def/property/

A useful convention is that URIs with a trailing '/' denote fully described collections, and aliases without the trailing '/' ensure that every possible path still resolves. 

Collections can also be used to group concepts along thematic grounds, perhaps as part of a facetted classification, if desired. In these cases the collection URI may not be the parent of the member concept URIs.

#### Concept-schemes

[Concept-schemes](http://www.w3.org/TR/skos-primer/#secscheme) provide another kind of container. In terms of semantics, a concept-scheme collects a set of concepts with a consistent set of hierarchical and other semantic relationships.

Membership in a concept scheme is explicit (through the `skos:inScheme` property) so the URI for a concept scheme might not use the same stem as the URIs for the member concepts. If the same URI stem is used, then the keyword 'scheme' may be used as the local identifier to distinguish the concept scheme from collections and concepts.

Concept-scheme URI examples:

*   http://resource.geosciml.org/classifierscheme/ics/2012/ischart
*   http://www.opengis.net/def/scheme
*   http://environment.data.gov.au/water/quality/def/property/scheme

### Slash or Hash

There are different views on whether the RDF namespace is separated from the local name using a / or #. Currently we recommend use of / namespaces in vocabularies on pragmatic grounds.

Vocabulary items may be members of very large sets. Furthermore, vocabulary items are commonly accessed one-at-a-time, and not only in the context of the complete set. For those reasons **'slash-URIs' are recommended for vocabulary items**, in which the local-name appears after a "/", as shown in the examples above. Slash URIs allow access to individual items over HTTP.

In contrast, 'hash-URIs' in which the local-name appears _after_ the # fragment separator, do not allow individual access because the HTTP protocol does not transmit the fragment to the server. A request for an item identified by a hash-URI, such as http://www.w3.org/2000/01/rdf-schema#Class, will get the entire vocabulary, regardless of whether the secondary resource is even present in it. For some important use-cases this behaviour is undesirable, because (a) it requires additional processing on the client side to extract the secondary resource (b) it is not possible to rely on HTTP 404 to discover that a concept does not exit.

### URI stability and patterns

If the vocabulary is intended to be used for a long period (and what vocabulary isn't?) the **URIs must be stable and persistent**. For this reason the URI domain and pattern should not be based on something temporary, like the current deployment technology (e.g. .asp, .jsp, .cfm) or the current organizational structure of the deploying agency.

Intuitive URIs, including words rather than opaque identifiers, are more memorable and therefore more user- and developer-friendly. Nevertheless, URIs in which the localname is a number or code are fine, as long as a label is provided.

**Do not over-design URI patterns**. Elaborate path structures are unwieldy and may become outdated. Shorter paths and flatter hierarchies are generally more scalable and flexible. **Do not rely on URI structure to capture semantics**: semantics and relationships are better provided explicitly, in the resource descriptions.

Also see Tim Berners-Lee's note from 1998 on the [dangers of embedding too much information in URIs](http://www.w3.org/Provider/Style/URI.html).

## Vocabulary properties
### Ontology metadata

The Ontology resource provides a hook primarily for metadata relating to the document. In addition to standard RDFS and Dublin Core terms, OWL provides the following important properties:

*   `owl:imports` carries references to the ontology dependencies
*   `owl:versionIRI` carries a URI that identifies the fine-grained version information, for example an SVN tag for the source file
*   `owl:priorVersion` allows you to identify a previous version

```turtle
<http://resource.geosciml.org/vocabulary/timescale/isc-2010>
       a       owl:Ontology ;
       rdfs:label "Ontology document containing the International Stratigraphic Chart (2010)"@en ;
       rdfs:seeAlso <http://resource.geosciml.org/classifierscheme/ics/2010/ischart> ;
       dc:creator "Simon J D COX"@en ;
       dc:rights "RDF version Copyright © 2012 CSIRO, Arizona Geological Survey, IUGS"@en ,
           "Original version Copyright © 2010 International Commission on Stratigraphy"@en ,
           <http://opendatacommons.org/licenses/by/1.0> ,
           "This Ontology is made available under the Open Data Commons Attribution License: http://opendatacommons.org/licenses/by/1.0"^^xsd:string ;
       dcterms:isReplacedBy               <http://resource.geosciml.org/vocabulary/timescale/isc-2012> ;
       dcterms:replaces <http://resource.geosciml.org/vocabulary/timescale/isc-2009> ;
       owl:imports <http://resource.geosciml.org/ontology/timescale/gts-30> , foaf: , <http://www.opengis.net/ont/geosparql> ;
       owl:priorVersion <https://www.seegrid.csiro.au/subversion/xmml/ontologies/tags/201205-hash-namespaces/GeologicTimeScale/isc-2010.rdf> ;
       owl:versionIRI <https://www.seegrid.csiro.au/subversion/xmml/ontologies/tags/201208-Temporal/GeologicTimeScale/isc-2010.rdf> .
```

### Concept scheme properties

A concept-scheme provides a home for metadata related to the vocabulary content as a whole, including versioning. The description of a concept-scheme may be found by following the `skos:inScheme` property in a concept description.

```turtle
<http://resource.geosciml.org/classifierscheme/ics/2010/ischart>
      a       gts:GeologicTimescale , skos:ConceptScheme ;
      rdfs:isDefinedBy <http://resource.geosciml.org/vocabulary/timescale/isc-2010> ;
      rdfs:label "International Stratigraphic Chart (2010)"@en ;
      rdfs:seeAlso <http://www.stratigraphy.org/upload/ISChart2010.pdf> ;
      dc:contributor "Chinese and Japanese preferred labels from SKOS by Xiaogang Ma, adopted from Asian Multilingual Thesaurus of Geosciences."@en , 
         "OneGeology Europe preferred labels merged in by S.M. Richard."@en , "International Commission on Stratigraphy"@en ;
      dc:creator "Simon J D COX"@en ;
      dc:description "This is an RDF/OWL representation of the 2010 edition of the International Stratigraphic Chart from the International Commission on Stratigraphy."@en ;
      dc:rights "RDF version Copyright © 2012 CSIRO, Arizona Geological Survey, IUGS"@en , "Original version Copyright © 2010 International Commission on Stratigraphy"@en , 
         <http://opendatacommons.org/licenses/by/1.0> , 
         "This Ontology is made available under the Open Data Commons Attribution License: http://opendatacommons.org/licenses/by/1.0"^^xsd:string ;
      dc:source "International Stratigraphic Chart 2010"@en ;
      dc:title "International Stratigraphic Chart (2010)"@en ;
      dcterms:created "2012-01-13"^^xsd:date ;
      dcterms:isReplacedBy
              <http://resource.geosciml.org/classifierscheme/ics/2012/ischart> ;
      dcterms:replaces <http://resource.geosciml.org/classifierscheme/ics/2009/ischart> ;
      skos:hasTopConcept isc:Precambrian , isc:Phanerozoic ;
      skos:prefLabel "International Stratigraphic Chart (2010)"@en .
```

The metadata properties are used as follows:

*   `rdfs:isDefinedBy` links up to the ontology document that contains the definition of this resource
*   `rdfs:seeAlso` links to an online resource that defines the content
*   `dc:source` names the source material
*   `dc:rights` contains descriptions of and links to IP information
*   `dcterms:replaces` and `dcterms:isReplacedBy`identify the predecessor and successor schemes.
    *   Note that this concept _scheme_ is explicitly versioned by year, to reflect the governance arrangements of the community that is responsible for this example. However, the identifiers for the _concepts_ in the scheme are not versioned.
*   `skos:hasTopConcept` links to the Concepts at the top of the hierarchies in the vocabulary

### Concept descriptions

Each concept is described by a set of assertions using RDF properties from the core RDF vocabularies.

1.  each concept should have at least one `skos:prefLabel`. Additional prefLabel properties can support multi-lingual terms, and `skos:altLabel` properties can provide for non-preferred synonyms.
    *   example: `isc:Silurian skos:prefLabel "Силур"@bg , "Silúrcio"@es , "シルル紀"@ja , "Silurian"@en .`
2.  one of the `skos:prefLabel` values should also be recorded as the `rdfs:label`for display in simple clients and IDEs
    *   since `skos:prefLabel rdfs:subPropertyOf rdfs:label` this can be generated with the help of a reasoner
3.  all known synonyms should be recorded using `skos:altLabel`
4.  each concept should have a textual definition recorded using `skos:definition`
5.  the language should be indicated for every text string (`@lang` tag)
6.  where an external source for the individual definition is available, this should be recorded in two ways:
    *   link to an online resource using `rdfs:seeAlso`
    *   the name of the external source of the definition using `dc:source`
7.  use `skos:notation` for any symbolic label or code which is externally recognised
8.  use `skos:broader` and `skos:narrower` relationships between concepts to capture hierarchies in the vocabulary if they exist
    *   example: `isc:Silurian skos:broader isc:Paleozoic .`  
        Note: These terms have sometimes been used to capture partitive as well as hierarchical relationships, such as `my:wheel skos:broader my:car .` However, it is recommended to use `skos:broader` only for _is-a_ relationships, else misleading inferences might be drawn.
9.  transitive hierarchical relationships (`skos:broaderTransitive`, `skos:narrowerTransitive`) should be added as assertions if they are expected to be used in vocabulary queries
    *   these can be generated from the broader/narrower relationships with the help of a reasoner
    *   example: `isc:Silurian skos:broaderTransitive isc:Phanerozoic , isc:Paleozoic .`
10.  non-specific relationships between concepts should be added using `skos:semanticRelation.` Or use skos:related (symmetrical but not transitive).
11.  all inverse relationships (broader/narrower, broaderTransitive/narrowerTransitive) should be added as assertions if they are expected to be used in vocabulary queries
    *   these can be generated from the initial asserted relationships with the help of a reasoner
    *   example: `isc:Paleozoic skos:narrower isc:Silurian .`
12.  `owl:sameAs` should be used to record alternative URIs (aliases) used for the same concept
13.  `skos:closeMatch`, `skos:exactMatch`etc. should be used to link to concepts in other published vocabularies
    *   see [VocabularyHarmonization](https://confluence.csiro.au/wiki/bin/view/Siss/VocabularyHarmonization)
    *   example: `isc:Silurian owl:sameAs <http://dbpedia.org/resource/Silurian> .`
14.  each concept should be `skos:inScheme` a concept-scheme

*   this allows traversal from atomic concepts to the vocabulary as a whole
*   example: `isc:Silurian skos:inScheme <http://resource.geosciml.org/classifierscheme/ics/ischart/2010> .`

```turtle
isc:Silurian
     a      skos:Concept ;
     owl:sameAs      <http://dbpedia.org/resource/Silurian> ;
     rdfs:comment "younger bound-416 +/-2.8"@en , "older bound-443.7 +/-1.5"@en ;
     rdfs:label "Silurian Period"@en ;
     skos:definition "The Silurian is a geologic period and system that extends from the end of the Ordovician Period, about 
         443.7 ± 1.5 million years ago (mya), to the beginning of the Devonian Period, about 416.0 ± 2.8 mya. As with other 
         geologic periods, the rock beds that define the period's start and end are well identified, but the exact dates are 
         uncertain by several million years. The base of the Silurian is set at a major extinction event when 60% of marine 
         species were wiped out."^^xsd:string ;
     rdfs:seeAlso <http://www.stratigraphy.org/ics%20chart/ChronostratChart2012.pdf> ;
     dc:source "International Stratigraphic Chart. International Commission on Stratigraphy, July 2012"^^xsd:string ;
     skos:broader isc:Paleozoic ;
     skos:broaderTransitive isc:Paleozoic , isc:Phanerozoic ;
     skos:inScheme <http://resource.geosciml.org/classifierscheme/ics/2012/ischart> ;
     skos:narrower isc:Llandovery , isc:Ludlow , isc:Wenlock , isc:Pridoli ;
     skos:narrowerTransitive   isc:Aeronian , isc:Llandovery , isc:Sheinwoodian , isc:Ludlow , isc:Wenlock , isc:Gorstian , 
         isc:Telychian , isc:Rhuddanian , isc:Homerian , isc:Pridoli , isc:Ludfordian ;
     skos:notation "a1.1.3.4"^^<http://resource.geosciml.org/schema/cgi/gts/3.0#EraCode>;
     skos:prefLabel "Silúrico"@pt , "Silur"@no , "Silur"@cs , "Silur"@da , "Silur"@de , "Silur"@et , "siluriano"@it , 
         "Silúrcio"@es , "Siluur"@nl , "Silurian"@en , "Siluuri"@fi , "Sylur"@pl , "&#24535;&#30041;&#32426;"@zh , 
         "szilur"@hu , "Sil&#363;ras"@lt , "&#1057;&#1080;&#1083;&#1091;&#1088;"@bg , "silur"@sv , "silur"@sl , 
         "&#12471;&#12523;&#12523;&#32000;"@ja , "Silurien"@fr , "silúr"@sk ;
     foaf:isPrimaryTopicOf <http://sweet.jpl.nasa.gov/2.2/stateTimeGeologic.owl#Silurian> . 
```

### Collection properties

A primary use of `skos:Collection` is to provide a resolvable resource for every partial path in the URI set for the concepts. `skos:Collection` and `skos:OrderedCollection` can also be used for any other grouping, within or across concept-schemes.

1.  a `skos:Concept` or `skos:Collection` can be a member of any number of `skos:Collections`
2.  a `rdfs:label` and `skos:prefLabel` should be provided for display in user interfaces

[Example](http://www.opengis.net/def/nil/OGC/0/):
```turtle
nil:
      a       skos:Collection ;
      rdfs:label "OGC Nils 0" ;
      skos:member nil:AboveDetectionRange , nil:withheld , nil:unknown , nil:missing , nil:inapplicable , nil:template , nil:BelowDetectionRange .
```

[Example](http://resource.geosciml.org/classifier/ics/ischart/Eras):

```turtle
isc:  a       skos:Collection ;
      rdfs:label "Geologic Timescale Elements"^^xsd:string ;
      owl:versionInfo "Created with TopBraid Composer"@en ;
      skos:member isc:Bajocian , isc:Cenozoic , isc:Tournaisian , isc:LowerMississippian , isc:LowerJurassic , 
         isc:BaseKungurian , isc:BaseMaastrichtian , isc:BasePridoli , isc:Proterozoic , isc:BaseMiddleOrdovician , 
         isc:Tithonian , isc:BaseLopingian , isc:Rhyacian , isc:UpperJurassic , isc:BaseOrosirian , isc:BaseFamennian , isc:BaseLudlow ;
      skos:prefLabel "Geologic Timescale Elements"^^xsd:string .

isc:Eras
      a       skos:Collection ;
      rdfs:label "Eras (all ranks) in the International Stratigraphic Chart"@en ;
      skos:member isc:Bajocian , isc:Cenozoic , isc:LowerMississippian , isc:Tournaisian , isc:Wenlock , 
         isc:MiddleJurassic , isc:LowerJurassic , isc:UpperOrdovician , isc:Kimmeridgian , isc:MiddleOrdovician , 
         isc:Cryogenian , isc:Aalenian , isc:Kasimovian , isc:Proterozoic . 
(etc)
```

## Other considerations
### Container patterns

A number of container resources and patterns are available in RDF/OWL/SKOS.

#### rdf:type

Basic RDF provides for resource types. For example:

```turtle
my:ResourceA rdf:type skos:Concept.  
my:ResourceB rdf:type skos:Concept .
```

asserts that the resources are members of the class indicated. The subject resources are _individuals_ and the object resources are _classes_ in this case.

#### rdfs:subClassOf rdfs:subPropertyOf

RDFS adds mechanisms to define subsumption hierarchies at the class level:

```turtle
my:ResourceC rdfs:subClassOf some:ClassN .  
my:ResourceD rdfs:subClassOf some:ClassN .  
my:ResourceE rdfs:subClassOf my:ResourceD .
```

asserts that the resources are specializations of the class indicated. Both subjects and objects of these triples are _classes_, such as `skos:Concept`. RDFS also provides for specialization of properties:

`my:propertyF rdfs:subPropertyOf some:propertyO .`

#### rdfs:isDefinedBy

An OWL Ontology collects a set of classes, properties and axioms. By convention, `rdfs:isDefinedBy` links a resource to the ontology context that contains its definition:

```turtle
my:ResourceD rdfs:isDefinedBy my:OntologyP .  
my:propertyF rdfs:isDefinedBy my:OntologyP .
```

The subject resources may be either _individuals_ (including _properties_) or _classes_.

There is no inverse property to indicate the membership of an owl:Ontology. dct:hasPart has approximately the required semantics. For example:

```turtle
<http://environment.data.gov.au/water/quality/def/op>
      a       owl:Ontology ;
      dct:hasPart wqop:QualityKind , wqop:qualityKind , wqop:constraint , wqop:ScaledQuantityKind , wqop:featureOfInterest , wqop:matrix , wqop:PropertyKind , wqop:propertyKind , wqop:SubstanceOrTaxon , wqop:applicableVocabulary , wqop:objectOfInterest , wqop:procedure .
```

If the ontology is also a void:Dataset or skos:ConceptScheme, then the predicates from those vocabularies are available.

#### skos:ConceptScheme

SKOS introduces the notion of a concept-scheme, which is a set of concepts with a related scope and well defined semantic relationships:

```turtle
my:ConceptH skos:inScheme my:ConceptSchemeQ .  
my:ConceptI skos:inScheme my:ConceptSchemeQ .
```

Both concepts and concept-schemes are _individuals_. In practice `skos:ConceptScheme` resources add little information useful for reasoning, but can provide a convenient point to attach metadata relating to the set of concepts.

SKOS concept-scheme and OWL ontology have a similar intention, to provide a container for a set of related resources. However, while ontologies can contain any kind of resource (axioms related to classes, properties, or individuals), SKOS only supports membership of concept schemes by SKOS concepts (i.e. individuals). The [SKOS Reference indicates that it is consistent with SKOS semantics for the same resource to be typed as both an ontology and a concept-scheme](http://www.w3.org/TR/skos-reference/#L1170), but OWL reasoners may object as this is only consisten with OWL-Full.

#### skos:Collection

SKOS also provides collections:

`my:CollectionR skos:member my:ConceptH , my:ConceptI , my:CollectionS .`

Collections are also _individuals_. Note that collection membership can be either concepts or collections, so a `skos:Collection` can be used to assist navigation through a hierarchy of concepts in a fashion similar to a traditional file-system.

#### skos:narrower (and skos:broader)

Specialized semantic relations in SKOS provide for asserting specialization relations amongst individual concepts within a concept scheme:

```turtle
my:ConceptH skos:broader my:ConceptJ .  
my:ConceptI skos:broader my:ConceptJ .  
my:ConceptJ skos:narrower my:ConceptH , my:ConceptI .
```

and between concepts from different schemes:

```turtle
my:ConceptH skos:broadMatch her:ConceptK .  
my:ConceptH skos:narrowMatch his:ConceptL .
```

and also for approximate and exact matches between concepts from different schemes:

```turtle
my:ConceptH skos:closeMatch her:ConceptM .  
my:ConceptH skos:exactMatch his:ConceptN .
```

Linking back to 4., the top-concept property, and its inverse, provide for entry points at the top of a concept-scheme

```turtle
my:ConceptJ skos:topConceptOf my:ConceptSchemeQ .  
my:ConceptSchemeQ skos:hasTopConcept my:ConceptJ .
```

(As expected: `skos:topConceptOf rdfs:subPropertyOf skos:inscheme .` )

When preparing a specific vocabulary any or all of these patterns may be applicable. The best practice described on this page utilizes patterns 1., 4., 5\. and 6.

### Non-SKOS properties

A vocabulary provided through a SISSvoc service can contain other ontological relationships. For example, this [Geologic Timescale](http://resource.geosciml.org/classifier/ics/ischart/Eras) is represented using SKOS, with Cambrian, Ordovician, Silurian etc modeled as _concepts,_ all 'narrower' than Paleozoic. But the concepts in this vocabulary are also be typed as a _boundary_ or _era_, with additional relationships that reflect topology and semantics of the [timescale model](https://confluence.csiro.au/pages/viewpage.action?pageId=433784765) which has been formalized as an [OWL ontology](https://github.com/CGI-IUGS/timescale-ont).

NOTE:

1.  Additional properties will be reported in SISSvoc results, but a basic SISSvoc service does not expose the non-SKOS properties for query.
2.  SISSvoc will only return resources whose type is skos:Concept, so reasoning must be enabled to also return resources whose type is a subClassOf skos:Concept.

### How many documents/concept-schemes/repositories?

The relationship between concept schemes and vocabularies, ontology documents, and concept repositories is flexible and can be used to support various governance models. Vocabularies provided by SISSvoc services to date use various patterns, including:

*   the OGC Definitions Service
    *   multiple ontology documents - generally one per standard that provides new definitions
    *   one concept-scheme - i.e. continuously evolving ...
    *   [one RDF repository](http://def.seegrid.csiro.au/sparql/ogc-def) (SPARQL endpoint), with a different _context_ or _named graph_ per ontology (explanation below)
*   code-lists from the ISO harmonized model
    *   [multiple ontology documents](http://def.seegrid.csiro.au/isotc211/iso19115/2003/code/) - one per code-list
    *   multiple concept-schemes - one per code-list
    *   [one RDF repository](http://def.seegrid.csiro.au/sparql/isotc211) (SPARQL endpoint), with a different _context_ or _named graph_ per code-list
*   the Geologic Timescale
    *   [multiple ontology documents](http://resource.geosciml.org/vocabulary/timescale/) - one per version of the International (Chrono)stratigraphic Chart, containing different sets and descriptions of mostly the same concepts
    *   multiple concept schemes - one per version of the International (Chrono)stratigraphic Chart, linking to different sets and descriptions of mostly the same concepts
    *   multiple RDF repositories (SPARQL endpoints), each with a single context or named graph, corresponding to a version of the timescale

### Triple-stores, quad-stores and graphs

RDF repositories are commonly referred to as 'triple-stores' but in practice are almost always 'quad-stores', with an extra field associated with each triple. This element holds a URI which can be:

*   an identifier for the triple (to support 'reification')
*   a identifier of the source of the triple ('context')
*   a link to metadata about the triple
*   a name for a set of triples (a 'graph')

Different patterns of usage for the extra field can result in few or many different values in the fourth field within a single repository.

## Complete examples

*   [Geologic Timescale versions](https://github.com/CGI-IUGS/timescale-data)
*   [ISO 19115 Codelists](http://registry.it.csiro.au/def/isotc211)

