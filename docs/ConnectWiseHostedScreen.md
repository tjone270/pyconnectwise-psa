# ConnectWiseHostedScreen


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**screen_id** | **str** |  | [optional] 

## Example

```python
from connectwise_psa.models.connect_wise_hosted_screen import ConnectWiseHostedScreen

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectWiseHostedScreen from a JSON string
connect_wise_hosted_screen_instance = ConnectWiseHostedScreen.from_json(json)
# print the JSON string representation of the object
print ConnectWiseHostedScreen.to_json()

# convert the object into a dict
connect_wise_hosted_screen_dict = connect_wise_hosted_screen_instance.to_dict()
# create an instance of ConnectWiseHostedScreen from a dict
connect_wise_hosted_screen_form_dict = connect_wise_hosted_screen.from_dict(connect_wise_hosted_screen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


