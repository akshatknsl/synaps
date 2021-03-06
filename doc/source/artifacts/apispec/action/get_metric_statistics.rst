.. _get_metric_statistics:

GetMetricStatistics
===================

Description.
------------
Get specific metric's statistic data. SPCS Synaps collect data points which 
are exist within specified Period and return statistic data. 

Synaps holds 30 days of statistics data and you can query up to 1,440 
datapoints which covers a day in 1 minutes resolution and 15 days in 15 minutes 
resolution in a single API call.

Parameters
----------

Following is list of parameters for this action.

.. list-table:: 
   :widths: 20 50 10
   :header-rows: 1

   * - Name
     - Description
     - Mandatory
   * - Dimensions.member.N
     - Dimension list in respect of Metric.

       Data type: :ref:`dimension` list

       Length limitation: 0 ~ 10 items
     - No
   * - EndTime	
     - End of the period for which data point will be returned.
       
       Data type: DateTime
       
       Limitation: The time period between StartTime and EndTime should not be
       over 15 days.
     - Yes
   * - MetricName
     - Metric name.

       Data Type: String

       Length limitation: 1 ~ 255 bytes
              
       Type limitation: Value consisting of only numbers can not be used.
     - Yes
   * - Namespace	
     - namespace of Metric.

       Data Type: String

       Length limitation: 1 ~ 255 bytes
              
       Type limitation: Value consisting of only numbers can not be used.
     - Yes
   * - Period
     - Period to apply data point Statistic. (sec) It has to be always multiple
       of 60. Minimum, and default value is 60.
          
       Data Type: Integer
       
       Valid value : 60(1 minute) ~ 86400(24 hours), multiple of 60.
       
       "(Total seconds between StartTime and EndTime) / Period" should be less 
       than or equal to 1,440.
     - Yes
   * - StartTime
     - End of the period for which data point will be returned.

       Data type: DateTime
       
       Limitation: The time period between StartTime and EndTime should not be
       over 15 days. 
     - Yes
   * - Statistics.member.N
     - Metric statistics to return. 

       Valid value: Average | Sum | SampleCount | Maximum | Minimum

       Data type: String list

       Length limitation: 1 ~ 5 items 
     - Yes
   * - Unit
     - Metric's unit.
     
       Data type: String

       Valid value: Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | 
       Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | 
       Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | 
       Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | 
       Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | 
       Count/Second | None
     - Yes

see also :ref:`common_query_parameters`        
       
Response
--------

Following elements are structured in GetMetricStatisticsResult and returned.

.. list-table:: 
   :widths: 20 40
   :header-rows: 1

   * - Name
     - Description
   * - Datapoints
     - Data points of Metric.

       Data type: :ref:`datapoint` list
     
Error
-----

Following is list of errors for this action.

.. list-table:: 
   :widths: 20 50 10
   :header-rows: 1
   
   * - Error
     - Description
     - HTTP Status Code
   * - InvalidParameterValue
     - Invalid Input Parameter.
     - 400

see also :ref:`common_errors` 