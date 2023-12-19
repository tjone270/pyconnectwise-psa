# LinkResolveUrlInfo


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_id** | **int** |  | 
**url** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.link_resolve_url_info import LinkResolveUrlInfo

# TODO update the JSON string below
json = "{}"
# create an instance of LinkResolveUrlInfo from a JSON string
link_resolve_url_info_instance = LinkResolveUrlInfo.from_json(json)
# print the JSON string representation of the object
print LinkResolveUrlInfo.to_json()

# convert the object into a dict
link_resolve_url_info_dict = link_resolve_url_info_instance.to_dict()
# create an instance of LinkResolveUrlInfo from a dict
link_resolve_url_info_form_dict = link_resolve_url_info.from_dict(link_resolve_url_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


