# PortalReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**custom_flag** | **bool** |  | [optional] 
**display_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  Max length: 255; | 
**open_same_window_flag** | **bool** |  | [optional] 
**portal_configuration** | [**PortalConfigurationReference**](PortalConfigurationReference.md) |  | [optional] 
**url** | **str** |  Max length: 255; | 

## Example

```python
from connectwise_psa.models.portal_report import PortalReport

# TODO update the JSON string below
json = "{}"
# create an instance of PortalReport from a JSON string
portal_report_instance = PortalReport.from_json(json)
# print the JSON string representation of the object
print PortalReport.to_json()

# convert the object into a dict
portal_report_dict = portal_report_instance.to_dict()
# create an instance of PortalReport from a dict
portal_report_form_dict = portal_report.from_dict(portal_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


