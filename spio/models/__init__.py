# coding: utf-8

# flake8: noqa
"""
    Statuspage API

    # Code of Conduct Please don't abuse the API, and please report all feature requests and issues to https://help.statuspage.io/help/contact-us-30  # Rate Limiting Each API token is limited to 1 request / second as measured on a 60 second rolling window. To get this limit increased or lifted, please contact us at https://help.statuspage.io/help/contact-us-30  # Basics  ## HTTPS It's required  ## URL Prefix In order to maintain version integrity into the future, the API is versioned. All calls currently begin with the following prefix:    https://api.statuspage.io/v1/  ## RESTful Interface Wherever possible, the API seeks to implement repeatable patterns with logical, representative URLs and descriptive HTTP verbs. Below are some examples and conventions you will see throughout the documentation.  * Collections are buckets: https://api.statuspage.io/v1/pages/asdf123/incidents.json * Elements have unique IDs: https://api.statuspage.io/v1/pages/asdf123/incidents/jklm456.json * GET will retrieve information about a collection/element * POST will create an element in a collection * PATCH will update a single element * PUT will replace a single element in a collection (rarely used) * DELETE will destroy a single element  ## Sending Data Information can be sent in the body as form urlencoded or JSON, but make sure the Content-Type header matches the body structure or the server gremlins will be angry.  All examples are provided in JSON format, however they can easily be converted to form encoding if required.  Some examples of how to convert things are below:      // JSON     {       \"incident\": {         \"name\": \"test incident\",         \"components\": [\"8kbf7d35c070\", \"vtnh60py4yd7\"]       }     }      // Form Encoded (using curl as an example):     curl -X POST https://api.statuspage.io/v1/example \\       -d \"incident[name]=test incident\" \\       -d \"incident[components][]=8kbf7d35c070\" \\       -d \"incident[components][]=vtnh60py4yd7\"  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

# import models into model package
from spio.models.component import Component
from spio.models.delete_pages_page_id_page_access_groups_page_access_group_id_components import DeletePagesPageIdPageAccessGroupsPageAccessGroupIdComponents
from spio.models.delete_pages_page_id_page_access_users_page_access_user_id_metrics import DeletePagesPageIdPageAccessUsersPageAccessUserIdMetrics
from spio.models.error_entity import ErrorEntity
from spio.models.group_component import GroupComponent
from spio.models.incident import Incident
from spio.models.incident_template import IncidentTemplate
from spio.models.incident_update import IncidentUpdate
from spio.models.inline_object import InlineObject
from spio.models.inline_object1 import InlineObject1
from spio.models.metric import Metric
from spio.models.metric_add_response import MetricAddResponse
from spio.models.metric_add_response_metric_id import MetricAddResponseMetricId
from spio.models.metrics_provider import MetricsProvider
from spio.models.page import Page
from spio.models.page_access_group import PageAccessGroup
from spio.models.page_access_user import PageAccessUser
from spio.models.patch_pages import PatchPages
from spio.models.patch_pages_page import PatchPagesPage
from spio.models.patch_pages_page_id_component_groups import PatchPagesPageIdComponentGroups
from spio.models.patch_pages_page_id_components import PatchPagesPageIdComponents
from spio.models.patch_pages_page_id_incidents import PatchPagesPageIdIncidents
from spio.models.patch_pages_page_id_incidents_incident import PatchPagesPageIdIncidentsIncident
from spio.models.patch_pages_page_id_incidents_incident_id_incident_updates import PatchPagesPageIdIncidentsIncidentIdIncidentUpdates
from spio.models.patch_pages_page_id_incidents_incident_id_incident_updates_incident_update import PatchPagesPageIdIncidentsIncidentIdIncidentUpdatesIncidentUpdate
from spio.models.patch_pages_page_id_metrics import PatchPagesPageIdMetrics
from spio.models.patch_pages_page_id_metrics_metric import PatchPagesPageIdMetricsMetric
from spio.models.patch_pages_page_id_metrics_providers import PatchPagesPageIdMetricsProviders
from spio.models.patch_pages_page_id_metrics_providers_metrics_provider import PatchPagesPageIdMetricsProvidersMetricsProvider
from spio.models.patch_pages_page_id_page_access_groups import PatchPagesPageIdPageAccessGroups
from spio.models.patch_pages_page_id_page_access_groups_page_access_group_id_components import PatchPagesPageIdPageAccessGroupsPageAccessGroupIdComponents
from spio.models.patch_pages_page_id_page_access_users_page_access_user_id_metrics import PatchPagesPageIdPageAccessUsersPageAccessUserIdMetrics
from spio.models.patch_pages_page_id_status_embed_config import PatchPagesPageIdStatusEmbedConfig
from spio.models.patch_pages_page_id_status_embed_config_status_embed_config import PatchPagesPageIdStatusEmbedConfigStatusEmbedConfig
from spio.models.post_organizations_organization_id_users import PostOrganizationsOrganizationIdUsers
from spio.models.post_organizations_organization_id_users_user import PostOrganizationsOrganizationIdUsersUser
from spio.models.post_pages_page_id_component_groups import PostPagesPageIdComponentGroups
from spio.models.post_pages_page_id_component_groups_component_group import PostPagesPageIdComponentGroupsComponentGroup
from spio.models.post_pages_page_id_components import PostPagesPageIdComponents
from spio.models.post_pages_page_id_components_component import PostPagesPageIdComponentsComponent
from spio.models.post_pages_page_id_incidents import PostPagesPageIdIncidents
from spio.models.post_pages_page_id_incidents_incident import PostPagesPageIdIncidentsIncident
from spio.models.post_pages_page_id_incidents_incident_components import PostPagesPageIdIncidentsIncidentComponents
from spio.models.post_pages_page_id_incidents_incident_id_subscribers import PostPagesPageIdIncidentsIncidentIdSubscribers
from spio.models.post_pages_page_id_metrics_data import PostPagesPageIdMetricsData
from spio.models.post_pages_page_id_metrics_metric_id_data import PostPagesPageIdMetricsMetricIdData
from spio.models.post_pages_page_id_metrics_metric_id_data_data import PostPagesPageIdMetricsMetricIdDataData
from spio.models.post_pages_page_id_metrics_providers import PostPagesPageIdMetricsProviders
from spio.models.post_pages_page_id_metrics_providers_metrics_provider import PostPagesPageIdMetricsProvidersMetricsProvider
from spio.models.post_pages_page_id_metrics_providers_metrics_provider_id_metrics import PostPagesPageIdMetricsProvidersMetricsProviderIdMetrics
from spio.models.post_pages_page_id_metrics_providers_metrics_provider_id_metrics_metric import PostPagesPageIdMetricsProvidersMetricsProviderIdMetricsMetric
from spio.models.post_pages_page_id_page_access_groups import PostPagesPageIdPageAccessGroups
from spio.models.post_pages_page_id_page_access_groups_page_access_group import PostPagesPageIdPageAccessGroupsPageAccessGroup
from spio.models.post_pages_page_id_page_access_groups_page_access_group_id_components import PostPagesPageIdPageAccessGroupsPageAccessGroupIdComponents
from spio.models.post_pages_page_id_page_access_users import PostPagesPageIdPageAccessUsers
from spio.models.post_pages_page_id_page_access_users_page_access_user import PostPagesPageIdPageAccessUsersPageAccessUser
from spio.models.post_pages_page_id_page_access_users_page_access_user_id_metrics import PostPagesPageIdPageAccessUsersPageAccessUserIdMetrics
from spio.models.post_pages_page_id_subscribers import PostPagesPageIdSubscribers
from spio.models.post_pages_page_id_subscribers_reactivate import PostPagesPageIdSubscribersReactivate
from spio.models.post_pages_page_id_subscribers_resend_confirmation import PostPagesPageIdSubscribersResendConfirmation
from spio.models.post_pages_page_id_subscribers_subscriber import PostPagesPageIdSubscribersSubscriber
from spio.models.post_pages_page_id_subscribers_unsubscribe import PostPagesPageIdSubscribersUnsubscribe
from spio.models.postmortem import Postmortem
from spio.models.put_pages import PutPages
from spio.models.put_pages_page_id_component_groups import PutPagesPageIdComponentGroups
from spio.models.put_pages_page_id_components import PutPagesPageIdComponents
from spio.models.put_pages_page_id_incidents import PutPagesPageIdIncidents
from spio.models.put_pages_page_id_incidents_incident_id_incident_updates import PutPagesPageIdIncidentsIncidentIdIncidentUpdates
from spio.models.put_pages_page_id_incidents_incident_id_postmortem import PutPagesPageIdIncidentsIncidentIdPostmortem
from spio.models.put_pages_page_id_incidents_incident_id_postmortem_postmortem import PutPagesPageIdIncidentsIncidentIdPostmortemPostmortem
from spio.models.put_pages_page_id_incidents_incident_id_postmortem_publish import PutPagesPageIdIncidentsIncidentIdPostmortemPublish
from spio.models.put_pages_page_id_incidents_incident_id_postmortem_publish_postmortem import PutPagesPageIdIncidentsIncidentIdPostmortemPublishPostmortem
from spio.models.put_pages_page_id_metrics import PutPagesPageIdMetrics
from spio.models.put_pages_page_id_metrics_providers import PutPagesPageIdMetricsProviders
from spio.models.put_pages_page_id_page_access_groups import PutPagesPageIdPageAccessGroups
from spio.models.put_pages_page_id_page_access_groups_page_access_group_id_components import PutPagesPageIdPageAccessGroupsPageAccessGroupIdComponents
from spio.models.put_pages_page_id_page_access_users_page_access_user_id_metrics import PutPagesPageIdPageAccessUsersPageAccessUserIdMetrics
from spio.models.put_pages_page_id_status_embed_config import PutPagesPageIdStatusEmbedConfig
from spio.models.single_metric_add_response import SingleMetricAddResponse
from spio.models.single_metric_add_response_data import SingleMetricAddResponseData
from spio.models.status_embed_config import StatusEmbedConfig
from spio.models.subscriber import Subscriber
from spio.models.subscriber_count_by_state import SubscriberCountByState
from spio.models.subscriber_count_by_type import SubscriberCountByType
from spio.models.subscriber_count_by_type_and_state import SubscriberCountByTypeAndState
from spio.models.user import User
