# Microservices

## Document Legend
* 🔵 - Definition
* 👌 - Good Practice (Do this), 🔴 - Bad practice (Don't do this)
* 👻 - Myth
* 👍 - Advantage, 👎 - Disadvantage
* Other Emoji - These are to **emphasize** what's said in the sentences.

## What are micro services? 🚗🚗
* 👌 Names - should have names that denotes what it does. 👶
* 👌 Has autonomy 🚜
  * 👌 Small autonomous services that work well together.
  * 👌 Ability to change components independently.
  * 👌 When you can take one service, make a change, and deploy it independently into production without having to touch anything else.
* 👌 They communicate predominantly over APIs, or perhaps via events or messages
* Microservices that use database integration - this is a bad practice.
* 👌 Small and focused on doing one thing well. (Unix philosophy) 👴
* 🔵 Service Oriented Architecture (SOA) - overall idea, micro services - implementation of that idea. 🤔
* 🔵 Service Level Agreement(SLA) - contract between service provider and customers on service availability, performance, etc.
* 🔵 Service Level Object(ive) (SLO) - goal of service provider based on SLA.
* 🔵 Service Level Indicator(SLI) - measurement(s) service provider uses to reach the SLO.
* 👻 Microservices is a silver bullet - For smaller companies and projects it might be overkill.

## Advantages
* 👍 Cost effectively scale out.
  * Large collections of small servers are a cost-efficient.
* 👍 Can improve security
  * Allow different segregation models for different types of services.
  * Multiple perimeters can be created.
* 👍 Adapt different technologies easily.
* 👍 Customers access services in multifaceted (having many sides, i.e.: Use Tablet, Desktop & Mobile) manner.
* 👍 Align the architecture to the organization and vise versa.
* 👍 Scale individually.


## Disadvantages
* 👎 Lot of options and may create tension if picking new technological options are bureaucratic.
* 👎 Teething problems at the start, will take some time for micro services change to take off.
* 👎 Testing is more complicated. Might be hard to do e-2-e tests.
* 👎 Complicated monitoring. Need to monitor each service. Manual logging/monitoring no longer works.
* 👎 Distributed systems are generally hard.
* 👎 Resiliency is not free.
