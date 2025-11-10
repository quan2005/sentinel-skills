E2B实践交流

罗伟潮
亚马逊云科技 解决方案架构师

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

Agenda

• Manus简介

• E2B简介与工作流程

• E2B on AWS

• Free Talk

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

2

Manus on AWS

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

3

3

Leave it to Manus

Manus 是一款通用型 AI 助手，能将想法转化为行动：不止于思考，更注重成果。Manus 擅长处理工作与生活中的各类任务，
在你安心休息的同时，一切都能妥善完成。

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

44

Manus 是一个怎样的产品

M A N U S 处 于 L 2 - > L 3 转 变 的 阶 段

Agent 自治级别

描述

1

2

3

4

5

基于规则的自动化

所有系统和流程都基于规则和脚本。它们是反应式的，具有预先确定的行动。

机器学习辅助的自动化 基于机器学习的代理协助完成特定的确定性任务。系统展现出受限的决策能力。

部分自动化

基于大型语言模型(LLM)的代理为明确定义的用例提供自主规划。代理创建并执行计划。

高度自动化

完全自主

AI代理大部分情况下自主运行，并能访问传感器进行观察。它们从经验中学习并基于上下
文进行泛化。

代理无需人类干预完全自主运行，展现原创思维，体现个性和情感。它们能解决初始训练
时未预见的问题。

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

5
5

LLM Agent system architecture

LLM Agent= 1+4 （大语言模型 + 观察 + 思考 + 行动 + 记忆）

⼯程实现上可以拆分出四⼤块核⼼模块：规划、记忆、⼯具、⾏动

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

6
6

Multi-Agent Orchestrator

主要特点：
- 灵活编排模式
• 任务路由模式，分发至单个Agent
• 通过Supervisor Agent自动编排多个子Agent完成复杂任务。
• 支持顺序编排形成固定工作流
• 支持混合编排形成多层级的Agents系统。

- 自带Session记忆管理
• 支持In-Memory，SQL DB或者DynamoDB做Session管理工具

- 自带外部知识库集成接口
• 支持Bedrock Knowledge Base集成

• 模块化设计
• 用户可以使轻松定制系统，包括自定义Agent、工具、知识检索工

具，内存和模型。

• 统一的Agent抽象设计，可以同时支持编排在云上托管的Bedrock

Agent和本地运行的 LLM Agent，保持相同的代码结构。

- 企业生产级别Serverless部署
支持在AWS Lambda上部署运行环境，同时支持编排云上托管的
Bedock Agent服务

- 高并发支持
异步消息接口，支持session并发，支持构建面向多用户的生产级应用

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

7
7
https://awslabs.github.io/multi-agent-orchestrator/general/introduction/

丰富的AWS 服务集成简化开发

Bedrock LLM Agent

直接配置Model Id 调用Bedrock上的各种LLM,支持配置guardrail

Bedrock Agent

直接配置Agent Id 调用Bedrock上的托管Agent 服务

Bedrock
Flow Agent

直接配置Flow Id 调用Bedrock上的托管Agent Flow服务

Lambda Agent

直接配置Function Name调用AWS Lambda

Comprehend
Filter Agent

可以直接使用 Amazon Comprehend 服务来做情感、（PII） 和毒性来分析和
内容过滤。

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

8
8

LLM Agent system architecture

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

9
9

E2B

E2B: Open-Source Sandbox Infrastructure

开源的 AI 代码解释基础设施，基于 Nomad 集群

E2B功能特性

系统构建基础设施，使用 Firecracker MicroVM 创

建隔离环境，为 AI 代码提供全托管执行环境。

E2B用户群体

该项目面向需要安全执行和解释代码的AI系统开发

者、研究人员以及希望自托管此基础设施的组织。

E2B操作流程

用户通过 E2B 提供的 SDK 和 CLI 来自定义和管理

代码执行环境，可以使用 Terraform 在支持的云提

供商上部署整个基础设施。

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

10

AI Code Execution Challenges

AI 模型执行环境挑战

虚拟机和容器化解决方案

AI 模型需安全环境执行，传统方案存隐患，

虚拟机高隔离，高开销

系统完整性受威胁

容器开销低，有跨容器攻击风险

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

11

Scaling AI Code Execution

01

02

03

环境管理与可复现性挑战

随着AI模型发展，环境状态管理和可复现性面临

着复杂性挑战

AI基建的复杂性与需求

AI基础设施需具备处理复杂性并能有效扩展以适

应代码执行的需求

入门AI的基础设施障碍

复杂的基础设施需求成为许多组织进入AI领域的

重大障碍

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

12

Code Execution, Made Effortless

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

13

Deployment Components

Server Cluster

运行Consul和
Nomad，负责控制

平面，服务器模式

核心

Build Cluster

管理模板，Docker

反向代理，构建环

境管理

API Cluster

处理外部请求，用
户管理，API接口中

心

Client Cluster

运行沙盒环境，提

供实际服务，客户

端访问集中地

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

14

E2B Infrastructure

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

15

15

E2B Sandbox Requirements

• Secure à 允许LLM生成的代码获得特权访问权限

• Fast startup à 亚秒级的冷启动时间

• Pause and resume à 用户可以随时暂停和继续任务

• High density à 一个实例可以启动数千个沙盒

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

16

16

Firecracker

• 基于KVM的硬件虚拟化 à secure

• 150ms启动时间 à fast startup

• 快照恢复 à Pause and resume

• 底开销及超卖 à High density

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

17

17

E2B Architecture on AWS

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

18

18

实践痛点

No any knowledge of the E2B Infra open source project at the start of the project.

Can not find any document on E2B Infra.

The E2B Infra code contains a significant amount of redundant logic.

E2B Infra does not abstract cloud vendor service calls.

Project timeline is urgent.

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

19

19

实施工作

Cloud Services(Storage, Artifact Registry, IAM, Secret Manager) call in Terraform.

Adapt Consul and Nomad to AWS.

Cloud Services call in E2B API, Template Manager, Orchestrator and Envd module.

Firecracker snapshot mechanism optimization（SSA）

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

20

20

扶上马 送一程 打通“最后三公里”

发现用例

动手培训

解决方案架构师

产品技术专家

人工智能实验室

联合创新实验室

快速原型开发团队

专业服务团队

培训与认证讲师

开发原型

试验迭代

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

21

Thank You

© 2025, Amazon Web Services, Inc. or its affiliates. All rights reserved

