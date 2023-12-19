# RelationshipReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.relationship_reference import RelationshipReference

# TODO update the JSON string below
json = "{}"
# create an instance of RelationshipReference from a JSON string
relationship_reference_instance = RelationshipReference.from_json(json)
# print the JSON string representation of the object
print RelationshipReference.to_json()

# convert the object into a dict
relationship_reference_dict = relationship_reference_instance.to_dict()
# create an instance of RelationshipReference from a dict
relationship_reference_form_dict = relationship_reference.from_dict(relationship_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


