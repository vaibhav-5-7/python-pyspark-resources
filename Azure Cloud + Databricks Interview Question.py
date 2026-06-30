1. Difference between On-premise vs Cloud:
==========================================================
i. On-premise:
=========================
a. In case of on-premise we will procure virtual machine and setup the cluster and also manually we will maintain the cluster.
b. In case of on-premise we require upfront cost to maintain the infrastructure ans establish that so it is a example of capex which means capital expenditure.
   CAPEX : Capex stand for Capital Expenditure which means upfront cost is required to maintain the infrastructure.
c. On-premise is not so agile.
d. On-premise is not scalable so scale up and down it requires lot of expenditure.
e. On-premise is not fault tolerant in case of system failure everything will go down.
f. Upfront cost is high in case of on-premise .
e. Ongoing cost is low in case of on-premise.
f. In case of disasater like natoral calamities and human error it will go down.
g. on-premise does not support elasticity which means it cannot automatically scale up and down.\
   Elasticity means system can automatically scale up and down.
   Scalibilty means syststem cannot automatically scale up and scale down , we have to maually scale up and down.
h. Maintainence cost is high in case of on-premise.
i. For ex: Hortonwork, Cloudera.
j. Availibilty is not high.



ii. Cloud:
===========================\
a. In case of cloud we can procure any services by a single click of button  and it is maintained by cloud.
b. In case of cloud upfront cost is not required , it requires on-going cost so its a example of apex which means operational cost.
   APEX : Apex stands for operational cost which means ongoing cost not upfront cost.
c. Cloud is fast and agile.
d. Cloud is scalable , it can easily scale up and scale down.
e. Cloud is fault tolerant using replication factor.
f. Upfront cost is low in case of cloud.
e. Ongoing cost is high in case of cloud.
f. In case of natural disaster like natural calamities it will still be up and running.
g. Cloud  support elasticity which means it can automatically scale up and down.
   Elasticity means system can automatically scale up and down.
   Scalibilty means syststem cannot automatically scale up and scale down , we have to maually scale up and down. 
h. Maintainence cost is low in case of cloud.
i. For ex: AWS/AZURE/GCP.
j. Availibilty is high.


2. Difference b/t Vertical Scaling vs Horizontal Scaling:
========================================================================
i. Horizontal Scaling:
================================
a. In case of horizontal scaling we try to increase the cluster that is no of nodes.
b. Here performance will be high.
c. It also means scaling in/scaling out.
d. For example if we are using 2 nodes currently and if more resources are required than more nodes will be increased that is 4 ,5 ,6 based on usecase.
e. It is mostly recommended in case of production.


ii. Vertical Scaling:
==================================
a. In case of Vertical Scaling we will try to increase more resources on a single machine.
   Resources means:
   ==========================
   CPU cores 
   Memory RAM.

b. Here performace will be low.
c. It also means Scaling Up/Scaling Down.
d. For ex if we are currently  using 64 GB Ram + 16 CPU cores and if more resources are required we can increase the resources to 128 GB RAM.
e. It is not so recommended in production cluster.


3. Difference b/t Scaling vs Elasticity:
=======================================================
i. Scaling : In case of scaling we have to manually increase the cluster, it will not automatically scale up and scale down.
ii. Elasticity: In case of Elasticity system will automatically scale up and scale down.
    Cloud supports Elasticity.
    
    
    
4. Diffrence b/t IAAS vs PAAS vs SAAS:
====================================================
Cloud services are divided into 3 categories :
============================================================
i. IAAS (Infrastructure AS A SERVICE) -: 
===========================================================
a. In case of IAAS we mainly talk about hardwares not operating system and softwares.
b. Example : VM's.
c. It is cheaper.
d. It is mainly used by admins.
e. It is mostly used when we are migrating from on-premise to cloud.

ii. PASS (Platform As A Service):
==================================================
a. In case of PAAS we are takling mainly about operating system.
b. Example : Azure SQL DB, ATHENA, ADF.
c. It is costly than IAAS .
d. It is mainly used by developers who are aware about coding.


iii. SAAS (Software As A Service):
===========================================
a. In case of SAAS we want software installed also along with Infrastructure + Platform.
b. Example: OUTLOOK, SLACK, MICROSFT TEAMS , OFFICE 365 , GOOGLE DRIVE.
C. It is costliest among 3.
d. It is mostly used by end user who are not aware of coding .



5. Public cloud vs Private Cloud vs Hybrid cloud:
===============================================================
i. Public cloud:
=====================
a. It is open to all anyone can use it which means it is available publically.
b. It is cheaper.
c. It is not so secured so we cannot keep confidential data here.
d. Example : AWS/AZURE/GCP.


ii. Private cloud:
==============================
a. It is only used by company, outside people cannot access it.
b. It is mostly used when there is confidential data.
c. It is costly.
d. It is secured and compliant.
e. Example : Solix cloud.
f. It requires lot of in house talent.


iii. Hybrid cloud:
==============================
a. It is combination of both public + private cloud.
b. It is costly + it requires lot of in house talent.

