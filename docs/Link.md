# Link


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 50; | 
**screen_link** | **str** |  | [optional] 
**table_reference_id** | **int** |  | [optional] 
**url** | **str** |  Max length: 1000; | [optional] 

## Example

```python
from connectwise_psa.models.link import Link

# TODO update the JSON string below
json = "{}"
# create an instance of Link from a JSON string
link_instance = Link.from_json(json)
# print the JSON string representation of the object
print Link.to_json()

# convert the object into a dict
link_dict = link_instance.to_dict()
# create an instance of Link from a dict
link_form_dict = link.from_dict(link_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


