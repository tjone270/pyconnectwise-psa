# AgreementSite


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_id** | **int** |  | [optional] 
**company** | [**CompanyReference**](CompanyReference.md) |  | [optional] 
**custom_fields** | [**List[CustomFieldValue]**](CustomFieldValue.md) |  | [optional] 
**id** | **int** |  | [optional] 
**site** | [**SiteReference**](SiteReference.md) |  | [optional] 

## Example

```python
from connectwise_psa.models.agreement_site import AgreementSite

# TODO update the JSON string below
json = "{}"
# create an instance of AgreementSite from a JSON string
agreement_site_instance = AgreementSite.from_json(json)
# print the JSON string representation of the object
print AgreementSite.to_json()

# convert the object into a dict
agreement_site_dict = agreement_site_instance.to_dict()
# create an instance of AgreementSite from a dict
agreement_site_form_dict = agreement_site.from_dict(agreement_site_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


