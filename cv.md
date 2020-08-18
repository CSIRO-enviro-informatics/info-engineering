# Registers and controlled vocabularies

<!-- TOC depthFrom:2 -->
## Contents of this page
- [Background](#background)
- [Codelists and controlled vocabularies](#codelists-and-controlled-vocabularies)
  - [General](#general)
  - [Domain specific](#domain-specific)
  - [Spatio-temporal](#spatio-temporal)
- [Vocabulary and ontology services](#vocabulary-and-ontology-services)
- [IANA registers](#iana-registers)
- [Miscellaneous lists](#miscellaneous-lists)
- [Tools and best practices](#tools-and-best-practices)
<!-- /TOC -->

## Background 

A large number of standard 'controlled vocabularies' have been developed covering various general requirements as well as specialised technical disciplines. 
Many are available in forms that are compatible with Linked Data, with a separate persistent URI for every member of the vocabulary. 
These allow for hyper-linking from within datasets using a [URI-reference](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier#URI_references, either as the `rdf:object` in an RDF statement (triple), or as the value of a field in a table or the target of an anchor in other contexts. 

Controlled vocabularies are provided with a variety of expressiveness: 
1. presented as basic web-pages
2. organized as term-definitions in collections and schemes using [SKOS](https://www.w3.org/TR/skos-primer/)
3. axiomatized with rich descriptions using [OWL2](https://www.w3.org/TR/owl2-primer/) or more rigorous semantics such as [OBO](http://www.obofoundry.org/) 

## Codelists and controlled vocabularies
### General
- [ANZ Standard Research Classification, 2020](https://www.abs.gov.au/AUSSTATS/abs@.nsf/Lookup/1297.0Main+Features12020)
  - [Field of Research as linked-data](https://vocabs.ands.org.au/repository/api/lda/anzsrc-for/concept)
- [DCMI Type Vocabulary](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/#section-7)
- [Datacite resource types](https://schema.datacite.org/meta/kernel-4.1/include/datacite-resourceType-v4.1.xsd)
- [ISO/TC 211 metadata](http://registry.it.csiro.au/def/isotc211) - Codelists from the ISO 19115 metadata standards expressed using SKOS
- [MARC Genre Terms List](https://id.loc.gov/vocabulary/marcgt.html)
- [QUDT Quantity Kinds](http://www.qudt.org/doc/2020/08/DOC_VOCAB-QUANTITY-KINDS-ALL-v2.1.html)
- [QUDT Units of Measure](http://www.qudt.org/doc/2020/08/DOC_VOCAB-UNITS-ALL-v2.1.html)
- [re3data subject classification](https://www.re3data.org/browse/by-subject/)
- [UNESCO THesaurus](https://skos.um.es/unescothes/)
- [Wikidata](http://www.wikidata.org) - library of concepts published as linked-data - a useful fall-back where technical vocabularies are not available 

### Domain specific
- [Environment Ontology (ENVO)](http://environmentontology.org/) - strongly axiomatized environment definitions (OBO Foundry)
- [GEMET Thesaurus](https://www.eionet.europa.eu/gemet/en/webservices/) - General Multilingual _Environmental Thesaurus_ 
- [CGI GeoSciML vocabularies](https://geosciml.org/resource/) - a suite of small vocabularies for geological maps
- [GSQ vocabularies](https://github.com/geological-survey-of-queensland/vocabularies/tree/master/vocabularies) - Geology, resources
- [OBO Foundry](http://www.obofoundry.org/) - Open Biological and Biomedical Ontologies
- [Queensland CORVEG Database Vocabularies](https://linkeddata.tern.org.au/viewer/corveg/) - Ecology surveys
- [R2R Controlled Vocabularies](https://www.rvdata.us/about/technical-details/vocabularies) - Oceanography
- [Semantic Web for Earth and Environmental Terminology (SWEET) Ontologies](https://github.com/ESIPFed/sweet) - earth & environmental science 
- UK Centre for Ecology and Hydrology 
  - [Metadata vocabulary](http://vocabs.ceh.ac.uk/edg/tbl/cehmd.editor)
  - [Topic classification](http://vocabs.ceh.ac.uk/edg/tbl/cehmd.editor#http%3A%2F%2Fonto.nerc.ac.uk%2FCEHMD%2Ftopic)
  - [_EnvThes_ Environment thesaurus](http://vocabs.ceh.ac.uk/edg/tbl/EnvThes.editor) 

### Spatio-temporal 
- [EPSG Geodetic Parameters](http://www.epsg-registry.org/)
  - [EPSG Dataset](http://www.epsg.org/EPSGDataset/DownloadDataset.aspx)
  - [epsg.io](http://epsg.io) Slightly slicker ui and shorter URIs, but incomplete and not authoritative
- [Geologic timescale](https://vocabs.ands.org.au/viewById/196)
  - [Geologic timescale linked data service](http://resource.geosciml.org/classifier/ics/ischart)
  - [INTERACTIVE INTERNATIONAL CHRONOSTRATIGRAPHIC CHART](https://kurrawong.net/timescale/)
  - [Geologic Timescale Ontology](https://github.com/CGI-IUGS/timescale-ont)
  - [Geologic Timescale data repository](https://github.com/CGI-IUGS/timescale-data)
- [GeoNames](http://www.geonames.org/)
- [ICSM Place Names](https://placenames.fsdf.org.au/)
- [ISO Geodetic Registry](https://geodetic.isotc211.org/) - coordinate reference systems, datums, etc
- [Location Index](http://loci.cat/) - interlinked Australian geographies

## Vocabulary and ontology services
- [ESIP Community Ontology Repository](http://cor.esipfed.org/ont/#/) 
- [Linked open vocabularies (LOV)](https://lov.linkeddata.es/) - index of ontologies
- [NERC Vocabulary Server](https://www.bodc.ac.uk/resources/products/web_services/vocab/)
  - [list of vocabularies](https://vocab.nerc.ac.uk/collection/)
  - [SPARQL query](http://vocab.nerc.ac.uk/sparql/)
  - [SeaDataNet cache of NVS vocabularies](http://seadatanet.maris2.nl/v_bodc_vocab_v2/welcome.asp)
- [Ontobee](http://www.ontobee.org/) - A linked data server for OBO-foundry ontologies
- [Research Vocabularies Australia](https://vocabs.ands.org.au/)
- [Compendium of vocabularies](https://confluence.csiro.au/display/VOCAB/Compendium+of+vocabularies) - (unmaintained)

## IANA registers
- [Link relations](https://www.iana.org/assignments/link-relations/link-relations.xhtml) - standard relationships for web-links in HTTP headers
- [MIME media types](https://www.iana.org/assignments/media-types/media-types.xhtml) - standard file-formats

## Miscellaneous lists
- [Creative Commons licenses](http://creativecommons.org/licenses/)
- [Virtual International Authority File (VIAF)](http://viaf.org/) - authors and creators
- [Open Researcher and Contributor ID (ORCID)](http://orcid.org/) - research authors
- [Research Organization Registry](https://ror.org/)

## Tools and best practices
- [Clean your SKOS with Skosify](https://github.com/NatLibFi/Skosify/)
- [SKOS quality control](https://github.com/cmader/qSKOS/) - [qSKOS service](https://qskos.poolparty.biz/)
- [Best practice in formalizing a SKOS vocabulary](skos-bp.md) is an extended discussion of best-practices in encoding vocabularies in RDF, primarily SKOS. 

