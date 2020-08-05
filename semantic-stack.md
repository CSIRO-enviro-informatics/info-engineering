# Introduction to the semantic web stack

Web 1.0 - pages/browser
Web 2.0 - forms, services, social
Web 3.0 - linked data, semantic web, web-scale data linkages

Background of semantic web - tagging meets logic

tagging ~= metadata

flexibility and scalability
persistent identifiers
Entity-Attribute-Value model (traditionally considered an anti-pattern) - sacrifices performance for flexibility ... 
- performance comes with limitations, very use-case specific


Logic: 
RDF - URIs, statements, directed-labeled-graph (knowledge graph), type, reification
RDFS - sub-class, sub-property, domain/range - property-centric constraints ('global')
OWL - object vs datatype properties, annotation-, inverse-, functional-, symmetric-, transitive properties ... disjoint, equivalent-class, -property, sameAs, union class, class-centric constraints ('guarded' or 'restricted), 
SKOS - concepts(individuals) vs. classes; *match

t-box (~classes & properteis) vs a-box (individuals) ontologies
All expressed in RDF
i.e. mix schema & instance-level in same place


Processing:
SPARQL - query
Shapes - validation


Mappings - https://douroucouli.wordpress.com/2019/05/27/never-mind-the-logix-taming-the-semantic-anarchy-of-mappings-in-ontologie/ 

[OWL Reference for Humans](https://www.cambridgesemantics.com/blog/semantic-university/learn-owl-rdfs/owl-references-humans/)

