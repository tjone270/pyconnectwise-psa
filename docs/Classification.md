# Classification


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**company_flag** | **bool** |  | [optional] 
**default_flag** | **bool** |  | [optional] 
**employee_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**multiplier** | **float** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.classification import Classification

# TODO update the JSON string below
json = "{}"
# create an instance of Classification from a JSON string
classification_instance = Classification.from_json(json)
# print the JSON string representation of the object
print Classification.to_json()

# convert the object into a dict
classification_dict = classification_instance.to_dict()
# create an instance of Classification from a dict
classification_form_dict = classification.from_dict(classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


