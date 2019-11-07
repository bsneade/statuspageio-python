# Incident

Get an incident
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Incident Identifier | [optional] 
**components** | [**list[Component]**](Component.md) | Incident components | [optional] 
**created_at** | **datetime** | The timestamp when the incident was created at. | [optional] 
**impact** | **str** | The impact of the incident. | [optional] 
**impact_override** | **str** | value to override calculated impact value | [optional] 
**incident_updates** | [**list[IncidentUpdate]**](IncidentUpdate.md) | The incident updates for incident. | [optional] 
**metadata** | [**Json**](Json.md) | Metadata attached to the incident. Top level values must be objects. | [optional] 
**monitoring_at** | **datetime** | The timestamp when incident entered monitoring state. | [optional] 
**name** | **str** | Incident Name | [optional] 
**page_id** | **str** | Incident Page Identifier | [optional] 
**postmortem_body** | **str** | Body of the Postmortem. | [optional] 
**postmortem_body_last_updated_at** | **datetime** | The timestamp when the incident postmortem body was last updated at. | [optional] 
**postmortem_ignored** | **bool** | Controls whether the incident will have postmortem. | [optional] 
**postmortem_notified_subscribers** | **bool** | Indicates whether subscribers are already notificed about postmortem. | [optional] 
**postmortem_notified_twitter** | **bool** | Controls whether to decide if notify postmortem on twitter. | [optional] 
**postmortem_published_at** | **bool** | The timestamp when the postmortem was published. | [optional] 
**resolved_at** | **datetime** | The timestamp when incident was resolved. | [optional] 
**scheduled_auto_completed** | **bool** | Controls whether the incident is scheduled to automatically change to complete. | [optional] 
**scheduled_auto_in_progress** | **bool** | Controls whether the incident is scheduled to automatically change to in progress. | [optional] 
**scheduled_for** | **datetime** | The timestamp the incident is scheduled for. | [optional] 
**scheduled_remind_prior** | **bool** | Controls whether to remind subscribers prior to scheduled incidents. | [optional] 
**scheduled_reminded_at** | **datetime** | The timestamp when the scheduled incident reminder was sent at. | [optional] 
**scheduled_until** | **datetime** | The timestamp the incident is scheduled until. | [optional] 
**shortlink** | **str** | Incident Shortlink. | [optional] 
**status** | **str** | Incident status | [optional] 
**updated_at** | **datetime** | The timestamp when the incident was updated at. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


