## NRQL examples on The Four Golden Signals

The **Four Golden Signals** of monitoring are latency, traffic, errors, and saturation. If you can only measure four metrics of your user-facing system, focus on these signals.

NRQL is New Relic's SQL-like query language. You can use NRQL to retrieve detailed New Relic data and get insight into your applications, hosts, and business-important activity.

This document explains NRQL syntax, clauses, components, and functions.
https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/nrql-syntax-clauses-functions

NRQL allows you to query these New Relic data types. Event data from all New Relic products, including:
- APM events, like Transaction
- Browser monitoring events, like PageView
- Mobile monitoring events, like Mobile
- Infrastructure events, like ProcessSample
- Synthetics events, like SyntheticCheck
- Custom events, like those reported by the Event API

To learn more, see New Relic data types.
https://docs.newrelic.com/docs/query-your-data/nrql-new-relic-query-language/get-started/introduction-nrql-new-relics-query-language/#what-you-can-query

### The Four Golden Signals - Latency  

**Returns the average response time since 7 days ago, group by - hourly**
SELECT average(duration) FROM Transaction WHERE appName = 'XXX' AND httpResponseCode = 'XXX' SINCE 7 days ago limit MAX FACET hourOf(timestamp)

**Returns the 95th percentile response time since 30 days ago, group by - daily**
SELECT percentile(duration, 95) FROM Transaction WHERE appName = 'XXX' AND httpResponseCode = 'XXX' SINCE 30 days ago limit MAX FACET dateOf(timestamp) 

### The Four Golden Signals - Traffic

**Return the rate of change (1min) since 7 days ago, group by - hourly**
SELECT rate(count(*), 1 minute) FROM Transaction WHERE appName = 'XXX' SINCE 7 days ago limit MAX FACET hourOf(timestamp)

**Return the rate of change (1hr) since 30 days ago, group by - daily**
SELECT rate(count(*), 1 hour) FROM Transaction WHERE appName = 'XXX' SINCE 30 days ago limit MAX FACET dateOf(timestamp)

### The Four Golden Signals - Errors 

**Return the percentage of errors for status code 2XX since 7 days ago, group by - hourly**
SELECT percentage(count(*), WHERE httpResponseCode LIKE '2%') FROM Transaction WHERE appName = 'XXX' SINCE 7 days ago limit MAX FACET hourOf(timestamp)

**Return the percentage of errors for status code outside 2XX since 30 days ago, group by - daily**
SELECT percentage(count(*), WHERE httpResponseCode NOT LIKE '2%') FROM Transaction WHERE appName = 'XXX' SINCE 30 days ago limit MAX FACET dateOf(timestamp)

### The Four Golden Signals - Saturation 

**Return the average CPU since 7 days ago, group by - hourly**
SELECT average(cpuPercent) FROM SystemSample WHERE hostname LIKE '%XXX%' SINCE 7 days ago limit MAX FACET hourOf(timestamp)

**Return the average MEM since 30 days ago, group by - daily**
SELECT average(memoryUsedPercent) FROM SystemSample WHERE hostname LIKE '%XXX%' SINCE 30 days ago limit MAX FACET dateOf(timestamp)