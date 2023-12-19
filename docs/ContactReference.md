# ContactReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.contact_reference import ContactReference

# TODO update the JSON string below
json = "{}"
# create an instance of ContactReference from a JSON string
contact_reference_instance = ContactReference.from_json(json)
# print the JSON string representation of the object
print ContactReference.to_json()

# convert the object into a dict
contact_reference_dict = contact_reference_instance.to_dict()
# create an instance of ContactReference from a dict
contact_reference_form_dict = contact_reference.from_dict(contact_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


