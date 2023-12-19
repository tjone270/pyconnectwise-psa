# KBCategoryReference


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.kb_category_reference import KBCategoryReference

# TODO update the JSON string below
json = "{}"
# create an instance of KBCategoryReference from a JSON string
kb_category_reference_instance = KBCategoryReference.from_json(json)
# print the JSON string representation of the object
print KBCategoryReference.to_json()

# convert the object into a dict
kb_category_reference_dict = kb_category_reference_instance.to_dict()
# create an instance of KBCategoryReference from a dict
kb_category_reference_form_dict = kb_category_reference.from_dict(kb_category_reference_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


