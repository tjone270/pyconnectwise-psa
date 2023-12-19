# ClassificationReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.classification_reference import ClassificationReference

# TODO update the JSON string below
json = "{}"
# create an instance of ClassificationReference from a JSON string
classification_reference_instance = ClassificationReference.from_json(json)
# print the JSON string representation of the object
print ClassificationReference.to_json()

# convert the object into a dict
classification_reference_dict = classification_reference_instance.to_dict()
# create an instance of ClassificationReference from a dict
classification_reference_form_dict = classification_reference.from_dict(classification_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


