# RDF vocabularies you can trust

These vocabularies are well maintained and widely used, so elements from them can reasonably be adopted in new ontologies. 

Note, however, that they were not all designed as part of a consistent suite, so if it is planned to use them in applications involving _inferencing_ or _reasoning_, then it is wise to check whether axioms or entailments have any clashes or inconsistencies between modules.  

## Descriptive metadata

vocabulary | scope | prefix | namespace URI 
--- | --- | --- | ---
[Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) | General purpose metadata | `dcterms:` `dct:` | http://purl.org/dc/terms/ 
[Data Catalog Vocabulary](https://www.w3.org/TR/vocab-dcat-2/) | Descriptions of datasets and data-services | `dcat:` | http://www.w3.org/ns/dcat# 
[Schema.org](https://schema.org/) | General purpose metadata, used mostly for web-pages and the (often commercial) services that they describe | `schema:` `sdo:` | https://schema.org/ 
[DDI-RDF Discovery Vocabulary](https://ddialliance.org/Specification/RDF/Discovery) | discovery of statistical and social science research and survey data | `disco:` | http://rdf-vocabulary.ddialliance.org/discovery#
[Data Quality Vocabulary](https://www.w3.org/TR/vocab-dqv/) | Data quality descriptions and metrics | `dqv:` | http://www.w3.org/ns/dqv# 
[Provenance Ontology](https://www.w3.org/TR/prov-o/) | High-level model for provenance of items, usually digital - activity-centric | `prov:` | http://www.w3.org/ns/prov# 

## Utilities
### Terminology, controlled vocabularies

vocabulary | scope | prefix | namespace URI 
--- | --- | --- | ---
[SKOS](https://www.w3.org/TR/skos-reference/) | terms+definitions organized in a hierarchy | `skos:` |  http://www.w3.org/2004/02/skos/core# 

### Space and Time

vocabulary | scope | prefix | namespace URI 
--- | --- | --- | ---
[GeoSPARQL](https://portal.opengeospatial.org/files/?artifact_id=47664) | geometry & basic topology | `geo:` | http://www.opengis.net/ont/geosparql#
[GeoSPARQL Extensions](http://linked.data.gov.au/def/geox) | geometry metrics | `geox:` | http://linked.data.gov.au/def/geox#
[OWL-Time](https://www.w3.org/TR/owl-time/) | Temporal entities and relationships | `time:` | http://www.w3.org/2006/time# 
[Time aggregates](https://w3c.github.io/sdw/time-aggregates/) | Temporal aggregates | `time:` | http://www.w3.org/2006/time# 
[Temporal relations](https://w3c.github.io/sdw/time-entity-relations/) | The missing relationships | `time:` | http://www.w3.org/2006/time# 

### Organizations and people

vocabulary | scope | prefix | namespace URI 
--- | --- | --- | ---
[Friend of a friend](http://xmlns.com/foaf/spec/) | agents, persons, organizations - the original social-network ontology | `foaf:` | http://xmlns.com/foaf/0.1/ 
[Organization Ontology](https://www.w3.org/TR/vocab-org/) | organizational structures and affiliations | `org:` | http://www.w3.org/ns/org#
[vcard](https://www.w3.org/TR/vcard-rdf/) | People, organizations, addresses | `vcard:` `v:` | http://www.w3.org/2006/vcard/ns# 

## Encoding data 

vocabulary | scope | prefix | namespace URI 
--- | --- | --- | ---
[Darwin Core](https://dwc.tdwg.org/terms/) | biodiversity observations, esp. occurrences | `dwc:` <br/> `dwciri:` | http://rs.tdwg.org/dwc/terms/ <br/> http://rs.tdwg.org/dwc/iri/
[OBO Foundry](http://www.obofoundry.org/) | Open Biological and Biomedical Ontology | `obo:` | http://purl.obolibrary.org/obo/ 
[RDF Data Cube](https://www.w3.org/TR/vocab-data-cube/) | Tabular ('rectangular') data, surveys and statistics (SDMX) | `qb:` |   http://purl.org/linked-data/cube#
[Semantic Sensor Network Ontology](https://www.w3.org/TR/vocab-ssn/) | Metadata for observations and samples | `sosa:` <br/> `ssn:` | http://www.w3.org/ns/sosa/ <br/> http://www.w3.org/ns/ssn/ 
[Extensions to SSN](https://www.w3.org/TR/vocab-ssn-ext/) | Observation Collections, samples and feature-of-interest links | `sosa:` <br/> `ssn:` | http://www.w3.org/ns/sosa/ <br/> http://www.w3.org/ns/ssn/ 
[Semantic Web for Earth and Environmental Terminology (SWEET) Ontologies](https://github.com/ESIPFed/sweet) | earth & environmental science | `so{xxx}:` |  http://sweetontology.net/{ontology} <br/> &gt; 200 distinct modules - see the [ESIP Community Ontology Repository](http://www.sweetontology.org/ont/)