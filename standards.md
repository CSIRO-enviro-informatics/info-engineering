# Standards for Linked Data and the Semantic Web 

<!-- TOC depthFrom:2 -->
## Contents of this page
- [Standard namespaces - RDF vocabularies that you can trust](#standard-namespaces---rdf-vocabularies-and-ontologies-that-you-can-trust)
  - [RDF infrastructure](#rdf-infrastructure)
  - [Descriptive metadata](#descriptive-metadata)
  - [Space and Time](#space-and-time)
  - [Organizations and people](#organizations-and-people)
  - [Encoding data](#encoding-data)
- [W3C semantics stack - references](#w3c-semantics-stack---references)
  - [RDF - the Resource Description Framework](#rdf---the-resource-description-framework)
  - [OWL - the Web Ontology Language](#owl---the-web-ontology-language)
  - [SKOS - the Simple Knowledge Organization System](#skos---the-simple-knowledge-organization-system)
  - [SPARQL - the SPARQL RDF Query Language](#sparql---the-sparql-rdf-query-language)
  - [RDF Shapes](#rdf-shapes)
- [Miscellaneous related non-RDF resources](#miscellaneous-related-non-rdf-resources)
  - [Geospatial metadata](#geospatial-metadata)
  - [Other metadata](#other-metadata)
<!-- /TOC -->

[International standards context](standards-organizations.md) is a brief listing of the main standards organizations involved. 

## Standard namespaces - RDF vocabularies and ontologies that you can trust
These ontologies and vocabularies of RDF terms are well maintained and widely used, so elements from them can reasonably be adopted in new ontologies. 

Note, however, that they were not all designed as part of a consistent suite, so if it is planned to use them in applications involving _inferencing_ or _reasoning_, then it is wise to check whether axioms or entailments have any clashes or inconsistencies between modules.  

### RDF infrastructure

vocabulary | scope | prefix | namespace URI 
--- | --- | --- | ---
[RDF](https://www.w3.org/TR/rdf11-concepts/) | Basic RDF elements | `rdf:` |  http://www.w3.org/1999/02/22-rdf-syntax-ns# 
[RDF Schema](https://www.w3.org/TR/rdf-schema/) | RDF Schema elements | `rdfs:` |  http://www.w3.org/2000/01/rdf-schema# 
[Web Ontology Language (OWL)](https://www.w3.org/TR/owl2-overview/) | OWL elements | `owl:` |  http://www.w3.org/2002/07/owl# 
[SKOS](https://www.w3.org/TR/skos-reference/) | SKOS elements | `skos:` |  http://www.w3.org/2004/02/skos/core# 
[SHACL](https://www.w3.org/TR/shacl/) | SHACL elements | `sh:` | http://www.w3.org/ns/shacl# 
 
### Descriptive metadata

vocabulary | scope | prefix | namespace URI | resources
--- | --- | --- | --- | ---
[Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) | General purpose metadata | `dcterms:` `dct:` | http://purl.org/dc/terms/ | 
[Data Catalog Vocabulary (DCAT)](https://www.w3.org/TR/vocab-dcat-2/) | Descriptions of datasets and data-services | `dcat:` | http://www.w3.org/ns/dcat# | 
[DCAT-AP 2.0.0](https://joinup.ec.europa.eu/solution/dcat-application-profile-data-portals-europe/release/200) | DCAT Application Profile for data portals in Europe | `dcat:` | | [RDFS representation](https://joinup.ec.europa.eu/sites/default/files/distribution/access_url/2019-11/ba9416ac-e755-4f3d-935d-3269dbbef190/dcat-ap_2.0.0%20%281%29.rdf)<br/> [SHACL representation](https://joinup.ec.europa.eu/sites/default/files/distribution/access_url/2019-11/d6cbf5d1-b4b1-4000-8560-864baa84a6e2/dcat-ap_2.0.0_shacl_shapes.ttl)
[GeoDCAT-AP 1.0.1](https://joinup.ec.europa.eu/release/geodcat-ap/101) | GeoDCAT Application Profile for data portals in Europe | `dcat:` | | 
[Schema.org](https://schema.org/) | General purpose metadata, used mostly for web-pages <br/>and the (often commercial) services that they describe | `schema:` `sdo:` | https://schema.org/ | 
[Science on Schema.org](https://github.com/ESIPFed/science-on-schema.org) | 'science profile' of Schema.org (EarthCube project) | `schema:` `sdo:` | | [Shape graphs](https://github.com/ESIPFed/science-on-schema.org/tree/master/validation/shapegraphs)
[DDI-RDF Discovery Vocabulary](https://ddialliance.org/Specification/RDF/Discovery) | statistical and social science research and survey data | `disco:` | http://rdf-vocabulary.ddialliance.org/discovery# | [RDF Representation](https://github.com/linked-statistics/disco-spec/blob/master/discovery.ttl)
[Data Quality Vocabulary](https://www.w3.org/TR/vocab-dqv/) | Data quality descriptions and metrics | `dqv:` | http://www.w3.org/ns/dqv# | 
[Provenance Ontology](https://www.w3.org/TR/prov-o/) | High-level model for provenance of items - activity-centric | `prov:` | http://www.w3.org/ns/prov# | 

### Space and Time

vocabulary | scope | prefix | namespace URI 
--- | --- | --- | ---
[GeoSPARQL](https://portal.opengeospatial.org/files/?artifact_id=47664) | geometry & basic topology | `geo:` | http://www.opengis.net/ont/geosparql#
[GeoSPARQL Extensions](http://linked.data.gov.au/def/geox) | geometry metrics | `geox:` | http://linked.data.gov.au/def/geox#
[OWL-Time](https://www.w3.org/TR/owl-time/) | Temporal entities and relationships | `time:` | http://www.w3.org/2006/time# 
[Time aggregates](https://www.w3.org/TR/vocab-owl-time-agg/) | Temporal aggregates | `time:` | http://www.w3.org/2006/time# 
[Temporal relations](https://www.w3.org/TR/vocab-owl-time-rel/) | The missing relationships | `time:` | http://www.w3.org/2006/time# 

### Organizations and people

vocabulary | scope | prefix | namespace URI 
--- | --- | --- | ---
[Friend of a friend](http://xmlns.com/foaf/spec/) | agents, persons, organizations - the original social-network ontology | `foaf:` | http://xmlns.com/foaf/0.1/ 
[Organization Ontology](https://www.w3.org/TR/vocab-org/) | organizational structures and affiliations | `org:` | http://www.w3.org/ns/org#
[vcard](https://www.w3.org/TR/vcard-rdf/) | People, organizations, addresses | `vcard:` `v:` | http://www.w3.org/2006/vcard/ns# 

### Encoding data 

vocabulary | scope | prefix | namespace URI 
--- | --- | --- | ---
[Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/) | Metadata for observations and samples | `sosa:` <br/> `ssn:` | http://www.w3.org/ns/sosa/ <br/> http://www.w3.org/ns/ssn/ 
[Extensions to SSN](https://www.w3.org/TR/vocab-ssn-ext/) | Observation Collections, samples and feature-of-interest links | `sosa:` <br/> `ssn:` | http://www.w3.org/ns/sosa/ <br/> http://www.w3.org/ns/ssn/ 
[Darwin Core](https://dwc.tdwg.org/terms/) | biodiversity observations, esp. occurrences | `dwc:` <br/> `dwciri:` | http://rs.tdwg.org/dwc/terms/ <br/> http://rs.tdwg.org/dwc/iri/
[QUDT](http://www.qudt.org/2.1/catalog/qudt-catalog.html) | Quantities, Units, Dimensions and Data Types | `qudt:` | http://qudt.org/2.1/schema/qudt 
[RDF Data Cube](https://www.w3.org/TR/vocab-data-cube/) | Tabular ('rectangular') data, surveys and statistics (SDMX) | `qb:` |   http://purl.org/linked-data/cube#

## W3C semantics stack - references

![semantic web stack](https://www.ontotext.com/wp-content/uploads/2018/03/Semantic-Web-Technology-Stack_01.png)

### RDF - the Resource Description Framework
- [RDF 1.1](https://www.w3.org/TR/rdf11-concepts/) - Concepts and Abstract Syntax
- [RDF Schema 1.1](https://www.w3.org/TR/rdf-schema/)
- [RDF 1.1 Turtle](https://www.w3.org/TR/turtle/) - Terse RDF Triple Language
- [JSON-LD 1.1](https://www.w3.org/TR/json-ld11/) - A JSON-based Serialization for Linked Data
- [Best Practice Recipes for Publishing RDF Vocabularies](https://www.w3.org/TR/swbp-vocab-pub/) - including '#' vs '/' URI patterns

### OWL - the Web Ontology Language
Basic description logic
- [OWL 2 Web Ontology Language Document Overview](https://www.w3.org/TR/owl2-overview/)
- [OWL 2 Web Ontology Language Primer](https://www.w3.org/TR/owl2-primer/)
- [OWL 2 Web Ontology Language Quick Reference Guide](https://www.w3.org/TR/owl2-quick-reference/)

### SKOS - the Simple Knowledge Organization System
Collections of terms+definitions organized in a hierarchy
- [SKOS Simple Knowledge Organization System Primer](https://www.w3.org/TR/skos-primer/) 
- [SKOS Simple Knowledge Organization System Reference](https://www.w3.org/TR/skos-reference/) 
- [Best practice in formalizing a SKOS vocabulary](skos-bp.md)
- [Clean your SKOS with Skosify](https://github.com/NatLibFi/Skosify/)
- [SKOS quality control](https://github.com/cmader/qSKOS/) - [qSKOS service](https://qskos.poolparty.biz/)

### SPARQL - the SPARQL RDF Query Language 
- [SPARQL 1.1 Overview](https://www.w3.org/TR/sparql11-overview/)
- [SPARQL 1.1 Query Language](https://www.w3.org/TR/sparql11-query/)
- [SPARQL 1.1 Protocol](https://www.w3.org/TR/sparql11-protocol/)
- [SPARQL 1.1 Service Description](https://www.w3.org/TR/sparql11-service-description/)

### RDF Shapes
RDF validation 
- [Shapes Constraint Language (SHACL)](https://www.w3.org/TR/shacl/) 
- [Shapes Expressions (ShEx)](http://shex.io/shex-primer/)

## Miscellaneous related non-RDF resources
### Geospatial metadata 
- [FGDC](https://www.fgdc.gov/metadata)
- [ISO 19115](https://en.wikipedia.org/wiki/Geospatial_metadata)
  - [ANZLIC metadata](https://www.anzlic.gov.au/resources/asnzs-iso-1911512015-metadata) - code, guidelines, validator - XML oriented
  - [FGDC summary of ISO 191** suite](https://www.fgdc.gov/metadata/iso-suite-of-geospatial-metadata-standards)
  - [NASA index of ISO metadata standards](https://earthdata.nasa.gov/esdis/eso/standards-and-references/iso-19115)
  - [DCC list of ISO 19115 profiles and implementations](http://www.dcc.ac.uk/resources/metadata-standards/iso-19115)

### Other metadata
- [DCC list of metadata profiles](http://www.dcc.ac.uk/resources/metadata-standards/extensions)
- [Metadata Schema for the Description of Research Data Repositories : version 3.0](https://doi.org/10.2312/re3.008) - the metadata schema for the [re3data registry](https://www.re3data.org/) 
  - [XML Schema](http://schema.re3data.org/3-0/re3dataV3-0.xsd)



