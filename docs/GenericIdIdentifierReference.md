# GenericIdIdentifierReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.generic_id_identifier_reference import GenericIdIdentifierReference

# TODO update the JSON string below
json = "{}"
# create an instance of GenericIdIdentifierReference from a JSON string
generic_id_identifier_reference_instance = GenericIdIdentifierReference.from_json(json)
# print the JSON string representation of the object
print GenericIdIdentifierReference.to_json()

# convert the object into a dict
generic_id_identifier_reference_dict = generic_id_identifier_reference_instance.to_dict()
# create an instance of GenericIdIdentifierReference from a dict
generic_id_identifier_reference_form_dict = generic_id_identifier_reference.from_dict(generic_id_identifier_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


