fgas-cache-server API Documentation
===================================

The fgas-cache-server API allows a client (BDR) to access cached data fetched
from various sources (FGas Registry, BDR Registry).

The API uses HTTP for transport, JSON as data format and does not require
authentication.

/undertaking/list
-----------------

Returns a list of all undertakings in the system, as fetched from FGR.
    
    [
      {
        "website": "WEBSITE--10085", 
        "status": "VALID", 
        "domain": "FGAS", 
        "users": [
          {
            "username": "nzhouray", 
            "first_name": "fname--9367", 
            "last_name": "lname--9367", 
            "id": 1, 
            "email": "9367email@climaOds2010.yyy"
          }
        ], 
        "date_updated": "10/10/2014", 
        "phone": "+3212310085", 
        "country_code": "CN", 
        "address": {
          "city": "city--7953", 
          "country": {
            "code": "CN", 
            "type": "NONEU_TYPE", 
            "name": "China (excluding Hong Kong and Macao)"
          }, 
          "zipcode": "zipcode--7953", 
          "number": "nrstreet--7953", 
          "street": "street--7953"
        }, 
        "collection_id": null, 
        "types": "FGAS_PRODUCER_IMPORTER_HFCS", 
        "undertaking_type": "FGASUndertaking", 
        "name": "FGAS-NMORGANIZATION--10085", 
        "company_id": 10085, 
        "date_created": "10/10/2014", 
        "vat": null
      },
    ]


/undertaking/[company_id]/details
-------------------------

Returns an undertakings details from the system, as fetched from FGR.
    
    {
      "company_id": 10085, 
      "collection_id": null,      
      "oldcompany_id": null, 
      "@type": "FGASUndertaking", 
      "website": "WEBSITE--10085", 
      "status": "VALID", 
      "domain": "FGAS", 
      "name": "FGAS-NMORGANIZATION--10085", 
      "phone": "+3212310085", 
      "businessprofile": {
        "highleveluses": "", 
        "id": 1
      }, 
      "candidates": [], 
      "representative": {
        "name": "EULEGALNAME44", 
        "contact_last_name": "lname--9853", 
        "vatnumber": "EUVAT44", 
        "contact_email": "9853email@climaOds2010.yyy", 
        "contact_first_name": "fname--9853", 
        "address": {
          "city": "city--7954", 
          "country": {
            "code": "IE", 
            "type": "EU_TYPE", 
            "name": "Ireland"
          }, 
          "zipcode": "zipcode--7954", 
          "number": "nrstreet--7954", 
          "street": "street--7954"
        }
      }, 
      "address": {
        "city": "city--7953", 
        "country": {
          "code": "CN", 
          "type": "NONEU_TYPE", 
          "name": "China (excluding Hong Kong and Macao)"
        }, 
        "zipcode": "zipcode--7953", 
        "number": "nrstreet--7953", 
        "street": "street--7953"
      }, 
      "vat": null, 
      "users": [
        {
          "username": "nzhouray", 
          "first_name": "fname--9367", 
          "last_name": "lname--9367", 
          "email": "9367email@climaOds2010.yyy"
        }
      ]
    }

/user/list
----------

Returns a list of all undertakings in the system, as fetched from FGR.
    
    [
      {
        "username": "user1",
        "first_name": "User 1",
        "last_name": "User 1",
        "email": "user1@mock.ec.europa.eu"
      },
    ]

/user/[username]/companies
--------------------------

Returns the list of undertakings for a user given by its unique username.

    [
      {
        "collection_id": null, 
        "domain": "FGAS", 
        "country": "CN", 
        "company_id": 10085, 
        "name": "FGAS-NMORGANIZATION--10085"
      }
    ]

/candidate/list
---------------

Lists all possible Company candidates for matching with existing Undertakings.

    [
      {
        "undertaking": {
          "website": "WEBSITE--10085", 
          "status": "VALID", 
          "name": "FGAS-NMORGANIZATION--10085", 
          "undertaking_type": "FGASUndertaking", 
          "date_updated": "10/10/2014", 
          "domain": "FGAS", 
          "company_id": 10085, 
          "phone": "+3212310085", 
          "types": "FGAS_PRODUCER_IMPORTER_HFCS", 
          "country_code": "CN", 
          "date_created": "10/10/2014", 
          "vat": null, 
        }, 
        "links": [
          {
            "website": null, 
            "account": "fgas22331", 
            "name": "Airconditioning Group Ltd", 
            "company_id": 4, 
            "date_registered": "07/12/2012", 
            "country_code": "gb", 
            "active": true, 
            "vat_number": "634456631", 
            "eori": null
          }, 
          {
            "website": "", 
            "account": "fgas21484", 
            "name": "Alcan International Network Ltd", 
            "company_id": 5, 
            "date_registered": "07/12/2012", 
            "country_code": "gb", 
            "active": false, 
            "vat_number": "", 
            "eori": ""
          }, 
      },
    ]

/candidate/verify/[company_id]/[collection_id]/
---------------------------------------------------

Verifies a link between an Undertaking (from FGR) and a Company (from BDR
 Registry).

    {
      "verified": true, 
      "company_id": 10085, 
      "collection_id": 4, 
      "date_verified": "24/11/2014", 
      "date_added": "24/11/2014",
    }
    
    
/candidate/unverify/[company_id]/
---------------------------------------------------

Removes any link between an Undertaking (from FGR) and a Company.

    {
        TODO
    }
    
/candidate/verify-none/[company_id]/
------------------------------------

Verifies a company is unlinked with any old companies.

    {
      "verified": true, 
      "company_id": 10085, 
      "collection_id": null, 
      "date_verified": "24/11/2014", 
      "date_added": "24/11/2014",
    }