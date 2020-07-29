# Linked Data APIs: theory and practice

## Theory

This section outlines theoretical aspects of Linked Data API design, rationale and related background.


### Background and designs

https://support.talis.com/hc/en-us/articles/205860451-Linked-data-API

### "Conneg" (Content-negotiation)

#### By format / media-type

The HTTP protocol allows content-negotiation via 
The Accept request HTTP header advertises which content types, expressed as MIME types, the client is able to understand. Using content negotiation, the server then selects one of the proposals, uses it and informs the client of its choice with the Content-Type response header. Browsers set adequate values for this header depending on the context where the request is done: when fetching a CSS stylesheet a different value is set for the request than when fetching an image, video or a script.

https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html
> The Accept request-header field can be used to specify certain media types which are acceptable for the response. Accept headers can be used to indicate that the request is specifically limited to a small set of desired types, as in the case of a request for an in-line image.


#### By profile

See https://www.w3.org/TR/dx-prof-conneg/


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

