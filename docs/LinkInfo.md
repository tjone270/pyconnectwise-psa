# LinkInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**screen_link** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.link_info import LinkInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LinkInfo from a JSON string
link_info_instance = LinkInfo.from_json(json)
# print the JSON string representation of the object
print LinkInfo.to_json()

# convert the object into a dict
link_info_dict = link_info_instance.to_dict()
# create an instance of LinkInfo from a dict
link_info_form_dict = link_info.from_dict(link_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


