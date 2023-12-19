# ContactRelationship


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 

## Example

```python
from connectwise_psa.models.contact_relationship import ContactRelationship

# TODO update the JSON string below
json = "{}"
# create an instance of ContactRelationship from a JSON string
contact_relationship_instance = ContactRelationship.from_json(json)
# print the JSON string representation of the object
print ContactRelationship.to_json()

# convert the object into a dict
contact_relationship_dict = contact_relationship_instance.to_dict()
# create an instance of ContactRelationship from a dict
contact_relationship_form_dict = contact_relationship.from_dict(contact_relationship_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


