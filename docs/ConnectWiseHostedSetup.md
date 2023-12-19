# ConnectWiseHostedSetup


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**client_id** | **str** | Only required if not already set. Max length: 36; | [optional] 
**created_by** | **str** |  | [optional] 
**date_created** | **str** |  | [optional] 
**description** | **str** |  Max length: 50; | 
**disabled_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**location_ids** | **List[int]** |  | [optional] 
**locations_enabled_flag** | **bool** |  | [optional] 
**origin** | **str** |  Max length: 100; | [optional] 
**pod_height** | **int** |  | [optional] 
**screen_id** | **int** | Can be obtained via ConnectWiseHostedApiScreen report. | 
**toolbar_button_dialog_height** | **int** |  | [optional] 
**toolbar_button_dialog_width** | **int** |  | [optional] 
**toolbar_button_icon_document_id** | **int** |  | [optional] 
**toolbar_button_text** | **str** | Only required for ToolbarButtons. Max length: 50; | [optional] 
**toolbar_button_tool_tip** | **str** |  Max length: 50; | [optional] 
**type** | **str** |  | 
**url** | **str** |  Max length: 1024; | 

## Example

```python
from connectwise_psa.models.connect_wise_hosted_setup import ConnectWiseHostedSetup

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectWiseHostedSetup from a JSON string
connect_wise_hosted_setup_instance = ConnectWiseHostedSetup.from_json(json)
# print the JSON string representation of the object
print ConnectWiseHostedSetup.to_json()

# convert the object into a dict
connect_wise_hosted_setup_dict = connect_wise_hosted_setup_instance.to_dict()
# create an instance of ConnectWiseHostedSetup from a dict
connect_wise_hosted_setup_form_dict = connect_wise_hosted_setup.from_dict(connect_wise_hosted_setup_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


