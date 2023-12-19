# CustomReport


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**info** | **Dict[str, str]** |  | [optional] 
**agreement_flag** | **bool** |  | [optional] 
**agreement_override** | **str** |  | [optional] 
**agreement_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Agreement parameter. | [optional] 
**agreement_type_flag** | **bool** |  | [optional] 
**agreement_type_override** | **str** |  | [optional] 
**agreement_type_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Agreement Type parameter. | [optional] 
**company_flag** | **bool** |  | [optional] 
**company_override** | **str** |  | [optional] 
**company_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Company parameter. | [optional] 
**department_default_flag** | **bool** |  | [optional] 
**department_flag** | **bool** |  | [optional] 
**department_override** | **str** |  | [optional] 
**department_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Department parameter. | [optional] 
**description** | **str** |  Max length: 150; | 
**end_date_flag** | **bool** |  | [optional] 
**end_date_override** | **str** |  | [optional] 
**end_date_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s End Date parameter. | [optional] 
**generated_flag** | **bool** |  | [optional] 
**id** | **int** |  | [optional] 
**invoice_flag** | **bool** |  | [optional] 
**invoice_override** | **str** |  | [optional] 
**invoice_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Invoice Type parameter. | [optional] 
**location_default_flag** | **bool** |  | [optional] 
**location_flag** | **bool** |  | [optional] 
**location_override** | **str** |  | [optional] 
**location_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Location parameter. | [optional] 
**marketing_campaign_flag** | **bool** |  | [optional] 
**marketing_campaign_override** | **str** |  | [optional] 
**marketing_campaign_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Marketing Campaign parameter. | [optional] 
**member_flag** | **bool** |  | [optional] 
**member_override** | **str** |  | [optional] 
**member_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Member parameter. | [optional] 
**module** | **str** | The Module Name. | 
**name** | **str** |  Max length: 100; | 
**opp_type_flag** | **bool** |  | [optional] 
**opp_type_override** | **str** |  | [optional] 
**opp_type_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Opportunity Type parameter. | [optional] 
**opportunity_flag** | **bool** |  | [optional] 
**opportunity_override** | **str** |  | [optional] 
**opportunity_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Opportunity parameter. | [optional] 
**parameter_name_separator** | **str** |  Max length: 50; | [optional] 
**parameter_prefix** | **str** |  Max length: 50; | [optional] 
**parameter_separator** | **str** |  Max length: 50; | [optional] 
**parameter_suffix** | **str** |  Max length: 50; | [optional] 
**project_flag** | **bool** |  | [optional] 
**project_override** | **str** |  | [optional] 
**project_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Project parameter. | [optional] 
**project_type_flag** | **bool** |  | [optional] 
**project_type_override** | **str** |  | [optional] 
**project_type_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Project Type parameter. | [optional] 
**report_link** | **str** |  | 
**service_board_default_flag** | **bool** |  | [optional] 
**service_board_flag** | **bool** |  | [optional] 
**service_board_override** | **str** |  | [optional] 
**service_board_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Service Board parameter. | [optional] 
**service_status_flag** | **bool** |  | [optional] 
**service_status_override** | **str** |  | [optional] 
**service_status_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Service Status parameter. | [optional] 
**service_type_flag** | **bool** |  | [optional] 
**service_type_override** | **str** |  | [optional] 
**service_type_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Service Type parameter. | [optional] 
**start_date_flag** | **bool** |  | [optional] 
**start_date_override** | **str** |  | [optional] 
**start_date_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Start Date parameter. | [optional] 
**territory_default_flag** | **bool** |  | [optional] 
**territory_flag** | **bool** |  | [optional] 
**territory_override** | **str** |  | [optional] 
**territory_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Terriroty parameter. | [optional] 
**work_role_flag** | **bool** |  | [optional] 
**work_role_override** | **str** |  | [optional] 
**work_role_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Work Role parameter. | [optional] 
**work_type_flag** | **bool** |  | [optional] 
**work_type_override** | **str** |  | [optional] 
**work_type_param_id** | **int** | Parameter unique identifier for the Custom Report&#39;s Work Type parameter. | [optional] 

## Example

```python
from connectwise_psa.models.custom_report import CustomReport

# TODO update the JSON string below
json = "{}"
# create an instance of CustomReport from a JSON string
custom_report_instance = CustomReport.from_json(json)
# print the JSON string representation of the object
print CustomReport.to_json()

# convert the object into a dict
custom_report_dict = custom_report_instance.to_dict()
# create an instance of CustomReport from a dict
custom_report_form_dict = custom_report.from_dict(custom_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


