# SiteReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.site_reference import SiteReference

# TODO update the JSON string below
json = "{}"
# create an instance of SiteReference from a JSON string
site_reference_instance = SiteReference.from_json(json)
# print the JSON string representation of the object
print SiteReference.to_json()

# convert the object into a dict
site_reference_dict = site_reference_instance.to_dict()
# create an instance of SiteReference from a dict
site_reference_form_dict = site_reference.from_dict(site_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


